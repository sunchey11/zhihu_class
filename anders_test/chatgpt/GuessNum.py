from utils.Utils import abs_path,upload_file, create_assistant, create_thread, chat, read_value, write_value, initClient

b_upload_file = False
b_create_assistant = True
b_create_thread = True

assi_name = 'GuessNum'


instructions = """
    你现在是一个猜数字的游戏。
    你(assistant)随机生成一个数字，1到100之间的整数。然后我(user)来猜这个数字。
    如果我猜大了，你就告诉我猜大了。
    如果我猜小了，你就告诉我猜小了。
    如果我猜对了，你就告诉我，猜对了。游戏就结束了。
    我说重新开始，那就重新开始这个游戏。
"""

client = initClient()
if b_create_assistant:
    create_assistant(client, assi_name, 
                     instructions,
                     "gpt-4-1106-preview",
                     None,
                     None)

if b_create_thread:
    create_thread(client, assi_name)

chat(client, assi_name, "你好")
print('finished')