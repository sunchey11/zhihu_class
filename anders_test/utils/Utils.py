import json
from sys import displayhook
import time
from openai import OpenAI
import os

def abs_path(name):
    file_dir = os.path.split(os.path.abspath(__file__))[0]
    imgpath = os.path.join(file_dir, name)
    return imgpath

ids_path = './ids/'
# 初始化 OpenAI 服务
def initClient():
    api_key = 'sk-YHK6UyHwbOzUnn9DgUyZJCF1u52qROP3mXCFVp5PG3olGpZX'
    base_url = "https://api.fe8.cn/v1"

    client = OpenAI(api_key=api_key, base_url=base_url)
    print(client.api_key)
    print(client.base_url)
    return client


def upload_file(client, filename):
    # 上传文件
    # https://platform.openai.com/docs/api-reference/files/create    
    with open(filename, "rb") as fp:
        file = client.files.create(file=(filename, fp), purpose='assistants')
    fileid = file.id
    return fileid
    
def write_value(filename,value):
    with open(ids_path + filename, 'w') as file:
        file.write(value)
def read_value(filename):
    with open(ids_path + filename, 'r') as file:
        value = file.readline()
        return value

def create_assistant(client,name,instructions,model,tools,fileid):
   
    
    param = {
        "name":name,
        "instructions":instructions,
        "model":model,
        
        }
    
    if tools is not None:
        param['tools'] = tools
    if fileid is not None:
        param['file_ids'] = [fileid]
    # 创建assistant
    # https://platform.openai.com/docs/api-reference/assistants/createAssistant
    assistant = client.beta.assistants.create(  # create
        **param)
    
    assistant_id = assistant.id
    if assistant_id is None:
        print(assistant.model_extra.get('error'))
        raise "error"
    write_value(name+"_assi.txt", assistant_id)
    return assistant

def load_assistant(client, name):
    # 获取已经在Playground中创建好的Assistants
    assistant_id = read_value(name+'_assi.txt')
    assistant = client.beta.assistants.retrieve(assistant_id)
    if assistant.id is None:
        print(assistant.model_extra.get('error'))
    return assistant

def create_thread(client, name):
    thread = client.beta.threads.create()
    thread_id = thread.id
    write_value(name+"_thread.txt", thread_id)
    return thread
def load_thread(client, name):
    thread_id = read_value(name+'_thread.txt')
    thread = client.beta.threads.retrieve(thread_id=thread_id)
    return thread

def get_current_time():
    # return time.strftime("%H:%M:%S", time.localtime())
    return f'现在时间是{time.strftime("%H:%M:%S", time.localtime())}'
def how_far(now_time):
    return 2
def sum_nums(numbers):
    v = 0
    for n in numbers:
        v = v+n
    return v

available_functions = {
    'get_current_time': get_current_time,
    'how_far': how_far,
    'sum_nums':sum_nums
}

    

def chat(client,name, greeting_msg):
    assistant_id = read_value(name+'_assi.txt')
    thread_id = read_value(name+'_thread.txt')
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=greeting_msg,
    )
    # 创建OpenAI的run
    run = client.beta.threads.runs.create(thread_id=thread_id,
                                        assistant_id=assistant_id)
    while True:
        try:
            # 如果在队列中或还在执行中，则等待并轮询更新run状态
            if run.status == 'queued' or run.status == 'in_progress':
                # print(f'等待run完成，now：{run.status}')
                print('...', end=" ")
                time.sleep(3)
                run = client.beta.threads.runs.retrieve(thread_id=thread_id,
                                                        run_id=run.id)
                print('-', end=" ")

            # 如果需要action，则依次执行本地方法并返回结果
            elif run.status == 'requires_action':
                print(run)
                print('run需要action')
                
                tool_outputs = []
                for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                    # 动态调用函数
                    func = available_functions[tool_call.function.name]
                    # 调用函数
                    args = json.loads(tool_call.function.arguments)
                    print(f'调用本地方法：{func.__name__}，参数：{args}')
                    output = func(**args)
                    # 将结果添加到tool_outputs中
                    tool_outputs.append({
                        'tool_call_id': tool_call.id,
                        'output': output,
                    })

                # 提交tool_outputs
                run = client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs,
                )

                print("本地执行完成，我将继续，请稍等")
            # 如果完成
            elif run.status == 'completed':
                print(' ok')
                # 从OpenAI获取完整messages列表
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                # print(len(messages)) 出错了 object of type 'SyncCursorPage[ThreadMessage]' has no len()
                # print(messages.first_id)
                # 获取最新一条消息对象
                first_message = client.beta.threads.messages.retrieve(
                    thread_id=thread_id, message_id=messages.first_id)
                # 获取消息对象中的文本内容
                msg = first_message.content[0].text.value
                # 将assistant的回复（即最新一条消息）添加到st的messages列表中
                print("assistant:", msg)
                input_str = input("请输入命令行输入：")
                
                if input_str == "quit":
                    break
                message = client.beta.threads.messages.create(
                    thread_id=thread_id,
                    role="user",
                    content=input_str,
                )
                run = client.beta.threads.runs.create(thread_id=thread_id,
                                        assistant_id=assistant_id)
                # break
        except Exception as e:
            print(e)
            print("assistant", '我好像出错了，请重试')
            continue

        time.sleep(1)
        # print('loop status',run.status)
        # print('loop runid',run.id)

# 基于 prompt 生成文本
# https://platform.openai.com/docs/guides/text-generation/chat-completions-api
def get_completion(client, prompt, model="gpt-3.5-turbo"):      # 默认使用 gpt-3.5-turbo 模型
    messages = [{"role": "user", "content": prompt}]    # 将 prompt 作为用户输入
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,                                  # 模型输出的随机性，0 表示随机性最小
    )
    
    choices = response.choices
    
    return choices[0].message.content          # 返回模型生成的文本    