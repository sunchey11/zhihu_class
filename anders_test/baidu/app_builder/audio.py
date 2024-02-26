import appbuilder
import requests
import os 

os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-mifXZj0j0D9KZTGjwkJy9/6d0a29e67d86f6ba3ff3dcf9dce981e78f2ffdee"
# 语音识别组件
audio_file_url = "https://bj.bcebos.com/v1/appbuilder/asr_test.pcm?authorization=bce-auth-v1" \
                   "%2FALTAKGa8m4qCUasgoljdEDAzLm%2F2024-01-11T10%3A56%3A41Z%2F-1%2Fhost" \
                   "%2Fa6c4d2ca8a3f0259f4cae8ae3fa98a9f75afde1a063eaec04847c99ab7d1e411"
print(audio_file_url)
audio_data = requests.get(audio_file_url).content
# 短语音识别-极速版 (Automatic Speech Recognition)
# https://console.bce.baidu.com/ai_apaas/componentCenter/asr/detail?tabKey=interfaceDoc
# 需要开通，送了5w次调用
asr = appbuilder.ASR()
inp = appbuilder.Message(content={"raw_audio": audio_data})
asr_out = asr(inp)
print(asr_out.content)