import json
from sys import displayhook
import time
from openai import OpenAI
import os


def show_json(obj):
    displayhook(json.loads(obj.model_dump_json()))


api_key = 'sk-YHK6UyHwbOzUnn9DgUyZJCF1u52qROP3mXCFVp5PG3olGpZX'
base_url = "https://api.fe8.cn/v1"

# 初始化 OpenAI 服务
client = OpenAI(api_key=api_key, base_url=base_url)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions=
    "You are a personal math tutor. Answer questions briefly, in a sentence or less.",
    model="gpt-4-1106-preview",
)
show_json(assistant)
thread = client.beta.threads.create()
show_json(thread)

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?",
)
show_json(message)
# 创建OpenAI的run
run = client.beta.threads.runs.create(thread_id=thread.id,
                                      assistant_id=assistant.id)

while True:
    try:
        # 如果在队列中或还在执行中，则等待并轮询更新run状态
        if run.status == 'queued' or run.status == 'in_progress':
            print(f'等待run完成，now：{run.status}')
            time.sleep(3)
            run = client.beta.threads.runs.retrieve(thread_id=thread.id,
                                                    run_id=run.id)
            print(run)

        # 如果需要action，则依次执行本地方法并返回结果
        elif run.status == 'requires_action':
            print('need action')

        # 如果完成
        elif run.status == 'completed':
            print('run完成')
            # 从OpenAI获取完整messages列表
            messages = client.beta.threads.messages.list(
                thread_id=thread.id)
            # 获取最新一条消息对象
            first_message = client.beta.threads.messages.retrieve(
                thread_id=thread.id, message_id=messages.first_id)
            # 获取消息对象中的文本内容
            msg = first_message.content[0].text.value
            # 将assistant的回复（即最新一条消息）添加到st的messages列表中
            print("assistant:", msg)
            break
    except Exception as e:
        print(e)
        print("assistant", '我好像出错了，请重试')
        continue
