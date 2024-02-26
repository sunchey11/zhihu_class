import appbuilder
import os

os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-mifXZj0j0D9KZTGjwkJy9/6d0a29e67d86f6ba3ff3dcf9dce981e78f2ffdee"
# 空模版组件
template_str = "你扮演{role}, 请回答我的问题。\n\n问题：{question}。\n\n回答："
playground = appbuilder.Playground(prompt_template=template_str, model="eb-turbo-appbuilder")

# 定义输入，调用空模版组件
input = appbuilder.Message({"role": "java工程师", "question": "java语言的内存回收机制是什么"})
print(playground(input, stream=False, temperature=1e-10))