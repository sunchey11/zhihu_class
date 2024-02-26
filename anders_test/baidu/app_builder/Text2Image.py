import os
import appbuilder

# 设置环境变量和初始化
# 请前往千帆AppBuilder官网创建密钥，流程详见：https://cloud.baidu.com/doc/AppBuilder/s/Olq6grrt6#1%E3%80%81%E5%88%9B%E5%BB%BA%E5%AF%86%E9%92%A5
os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-mifXZj0j0D9KZTGjwkJy9/6d0a29e67d86f6ba3ff3dcf9dce981e78f2ffdee"

text2Image = appbuilder.Text2Image()
content_data = {"prompt": "西安的街头", "width": 1024, "height": 1024, "image_num": 1}
msg = appbuilder.Message(content_data)
out = text2Image.run(msg)
print(out.content)