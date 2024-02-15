from utils.Utils import abs_path,upload_file, create_assistant, create_thread, chat, read_value, write_value, initClient

b_upload_file = False
b_create_assistant = False
b_create_thread = False

assi_name = 'GuessNum'


instructions = """

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