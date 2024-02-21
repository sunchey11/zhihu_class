# https://sfile.chatglm.cn/testpath/d5843b0c-515e-59c8-9d3c-5b849cf126a0_0.png
from zhipuai import ZhipuAI
client = ZhipuAI(api_key="27ac77433ad33b671a0f298cd29afc2e.YT0mNTzsb4j4y0Xy") 
 
prompt = "一只可爱的小猫咪"
response = client.images.generations(
    model="cogview-3", #填写需要调用的模型名称
    prompt=prompt,
)
print(response.data[0].url)