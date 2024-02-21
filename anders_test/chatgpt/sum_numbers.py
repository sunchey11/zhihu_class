from utils.Utils import abs_path,upload_file, create_assistant, create_thread, chat, read_value, write_value, initClient

b_upload_file = False
b_create_assistant = True
b_create_thread = True

assi_name = 'sum_number'


instructions = """
你是一个计算器，我告诉你一组数字，你计算出这些数字的和
"""

client = initClient()
tools = [{  # 用 JSON 描述函数。可以定义多个。由大模型决定调用谁。也可能都不调用
            "type": "function",
            "function": {
                "name": "sum_nums",
                "description": "加法器，计算一组数的和",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numbers": {
                            "type": "array",
                            "items": {
                                "type": "number"
                            }
                        }
                    }
                }
            }
        }]
if b_create_assistant:
    create_assistant(client, assi_name, 
                     instructions,
                     "gpt-4-1106-preview",
                     tools,
                     None)

if b_create_thread:
    create_thread(client, assi_name)

chat(client, assi_name, "桌上有 2 个苹果，四个桃子和 3 本书，一共有几个水果")
# prompt = "桌上有 2 个苹果，四个桃子和 3 本书，一共有几个水果？"
# prompt = "1+2+3...+99+100"
# prompt = "1024 乘以 1024 是多少？"   # Tools 里没有定义乘法，会怎样？
# prompt = "太阳从哪边升起？"           # 不需要算加法，会怎样？
print('finished')