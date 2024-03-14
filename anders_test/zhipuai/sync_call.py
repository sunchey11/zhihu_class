
from zhipuai import ZhipuAI

# https://github.com/zhipuai/zhipuai-sdk-python-v4
# 同步调用的例子
print('start')
client = ZhipuAI(api_key="27ac77433ad33b671a0f298cd29afc2e.YT0mNTzsb4j4y0Xy") 
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    # model="glm-3-turbo",  # 根据输入的自然语言指令完成多种语言类任务，推荐使用 SSE 或异步调用方式请求接口
    messages=[
        {"role": "system", "content": "你是一个人工智能助手，你叫小红。你回答问题要简短一点"},
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "我是人工智能助手"},
        {"role": "user", "content": "你叫什么名字"},
        {"role": "assistant", "content": "我叫小红"},
        {"role": "user", "content": "你叫什么名字"},
        # {"role": "user", "content": "你都可以做些什么事"}
    ],
    top_p=0.7,
    temperature=0.95,
    max_tokens=1024,
)
print(response.choices[0].message)