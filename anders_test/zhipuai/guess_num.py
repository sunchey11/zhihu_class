
from zhipuai import ZhipuAI

# https://github.com/zhipuai/zhipuai-sdk-python-v4
# 同步调用的例子
print('start')
client = ZhipuAI(api_key="27ac77433ad33b671a0f298cd29afc2e.YT0mNTzsb4j4y0Xy") 

instruction = """
    你现在是一个猜数字的游戏。
    你(assistant)随机生成一个数字，1到100之间的整数。然后我(user)来猜这个数字。
    你生成数字以后，可以偷偷告诉我，方法是在最后加上"__hidden:"+数字
    如果我猜大了，你就告诉我猜大了。
    如果我猜小了，你就告诉我猜小了。
    如果我猜对了，你就告诉我，猜对了。游戏就结束了。
    我说重新开始，那就重新开始这个游戏。
"""
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "system", "content": instruction},
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": """好的 ， 我已经 为你 生 成了一个 1 到 100 之间的 随机 整数 。 我们现在 开始 猜 数字 游戏 。

__ hidden : 64 

请 开始 猜 数字 吧 ！"""},
        {"role": "user", "content": "50"},
        {"role": "assistant", "content":"猜 小 了 ！ 继续 猜 。"},
        {"role": "user", "content": "70"},
    ],
    top_p=0.7,
    temperature=0.95,
    max_tokens=1024,
    stream=True,
)
for trunk in response:
    print(trunk.choices[0].delta.content, end=' ')