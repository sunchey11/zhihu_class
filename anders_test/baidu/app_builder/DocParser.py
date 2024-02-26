# https://console.bce.baidu.com/ai_apaas/componentCenter/doc_parser/detail?tabKey=interfaceDoc

from appbuilder.core.components.doc_parser.doc_parser import DocParser
from appbuilder.core.message import Message
import os
import requests

# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-mifXZj0j0D9KZTGjwkJy9/6d0a29e67d86f6ba3ff3dcf9dce981e78f2ffdee"

# 进行文档内容解析
file_url = "https://agi-dev-platform-bos.bj.bcebos.com/ut_appbuilder/test.pdf?authorization=bce-auth-v1/e464e6f951124fdbb2410c590ef9ed2f/2024-01-25T12%3A56%3A15Z/-1/host/b54178fea9be115eafa2a8589aeadfcfaeba20d726f434f871741d4a6cb0c70d"
file_data = requests.get(file_url).content
file_path = "./test.pdf"  # 待解析的文件路径
with open(file_path, "wb") as f:
    f.write(file_data)
msg = Message(file_path)
parser = DocParser()
parse_result = parser(msg)
print(parse_result.content)