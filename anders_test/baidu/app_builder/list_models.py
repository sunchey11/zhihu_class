import appbuilder
import os
# https://github.com/baidubce/app-builder?tab=readme-ov-file
os.environ["APPBUILDER_TOKEN"] = "bce-v3/ALTAK-mifXZj0j0D9KZTGjwkJy9/6d0a29e67d86f6ba3ff3dcf9dce981e78f2ffdee"
models = appbuilder.get_model_list(api_type_filter=["chat"], is_available=True)
print(", ".join(models))
# 我的组件
# https://console.bce.baidu.com/ai_apaas/component