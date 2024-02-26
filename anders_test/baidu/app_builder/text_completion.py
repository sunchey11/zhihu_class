import appbuilder
import os

os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-mifXZj0j0D9KZTGjwkJy9/6d0a29e67d86f6ba3ff3dcf9dce981e78f2ffdee"
# 相似问生成组件
similar_q = appbuilder.SimilarQuestion(model="eb-turbo-appbuilder")

# 定义输入，调用相似问生成
input = appbuilder.Message("我想吃冰淇淋，哪里的冰淇淋比较好吃？")
print(similar_q(input))