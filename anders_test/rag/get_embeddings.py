from openai import OpenAI
from utils.Utils import initClient
import numpy as np
from numpy import dot
from numpy.linalg import norm
client = initClient()
def get_embeddings(texts, model="text-embedding-ada-002",dimensions=None):
    '''封装 OpenAI 的 Embedding 模型接口'''
    if model == "text-embedding-ada-002":
        dimensions = None
    if dimensions:
        data = client.embeddings.create(input=texts, model=model, dimensions=dimensions).data
    else:
        data = client.embeddings.create(input=texts, model=model).data
    return [x.embedding for x in data]

test_query = ["测试文本"]
vec = get_embeddings(test_query)[0]
print(vec[:10])
print(len(vec)) #1536
"""
2024年1月25日，OpenAI 新发布了两个 Embedding 模型

text-embedding-3-large
text-embedding-3-small
"""
# 默认大小
vec = get_embeddings(test_query, model='text-embedding-3-large')[0]
print(len(vec)) #3072

vec = get_embeddings(test_query, model='text-embedding-3-small')[0]
print(len(vec)) #1536
# 128
dimensions = 128
vec = get_embeddings(test_query,model='text-embedding-3-large',dimensions=dimensions)[0]
print(len(vec)) #128

vec = get_embeddings(test_query,model='text-embedding-3-small',dimensions=dimensions)[0]
print(len(vec)) #128

# query = "国际争端"

# 且能支持跨语言
query = "global conflicts"

documents = [
    "联合国就苏丹达尔富尔地区大规模暴力事件发出警告",
    "土耳其、芬兰、瑞典与北约代表将继续就瑞典“入约”问题进行谈判",
    "日本岐阜市陆上自卫队射击场内发生枪击事件 3人受伤",
    "国家游泳中心（水立方）：恢复游泳、嬉水乐园等水上项目运营",
    "我国首次在空间站开展舱外辐射生物学暴露实验",
]

query_vec = get_embeddings([query])[0]
doc_vecs = get_embeddings(documents)

def cos_sim(a, b):
    '''余弦距离 -- 越大越相似'''
    return dot(a, b)/(norm(a)*norm(b))


def l2(a, b):
    '''欧式距离 -- 越小越相似'''
    x = np.asarray(a)-np.asarray(b)
    return norm(x)

# 余弦距离 -- 越大越相似
print("Cosine distance:")
print(cos_sim(query_vec, query_vec))
for vec in doc_vecs:
    print(cos_sim(query_vec, vec))
# 欧式距离 -- 越小越相似
print("\nEuclidean distance:")
print(l2(query_vec, query_vec))
for vec in doc_vecs:
    print(l2(query_vec, vec))