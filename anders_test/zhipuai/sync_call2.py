
from zhipuai import ZhipuAI

# https://github.com/zhipuai/zhipuai-sdk-python-v4
# 同步调用的例子
print('start')
client = ZhipuAI(api_key="27ac77433ad33b671a0f298cd29afc2e.YT0mNTzsb4j4y0Xy") 
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "system", "content": "你是一个人工智能助手，你叫小红"},
        {"role": "user", "content": "你好！你叫什么名字"},
    ],
    top_p=0.7,
    temperature=0.95,
    max_tokens=1024,
)
message = response.choices[0].message
print(message.content)