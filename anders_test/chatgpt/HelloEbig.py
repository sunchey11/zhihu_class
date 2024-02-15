from utils.Utils import abs_path,upload_file, create_assistant, create_thread, chat, read_value, write_value, initClient

b_upload_file = False
b_create_assistant = False
b_create_thread = False

assi_name = 'answer_about_ebig'
if b_upload_file:
    fileid = upload_file(abs_path("ebig.txt"))
    write_value(assi_name + '_fileid.txt', fileid)
    

client = initClient()
if b_create_assistant:
    fileid = read_value(abs_path(assi_name + '_fileid.txt'))
    create_assistant(client, assi_name, 
                     "请根据上传文件中的内容回答问题",
                     "gpt-4-1106-preview",
                     [{"type": "code_interpreter"}],
                     fileid)

if b_create_thread:
    create_thread(client, assi_name)

chat(client, assi_name, "请介绍下广州以大计算机科技有限公司")
print('finished')