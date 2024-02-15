from utils.Utils import abs_path,upload_file, create_assistant, create_thread, chat, read_value, write_value, initClient

b_upload_file = False
b_create_assistant = False
b_create_thread = False

assi_name = 'plan'


instructions = """
## Goal
    在这个游戏中，你是一个学生。
    每天按照严格的计划进行学习。
    当我问你，"你在做什么"。
    你根据中当前的时间，按照你的计划表，回答你在做什么。
    游戏的时间比现实的时间快。
    现实中的1小时对应游戏中的24小时。
    现实中的2.5分钟对应游戏中的1小时。
    每个小时的开始，表示游戏中每一天的0点
    
    

## 计划表
   7:00至8:00 起床,收拾，吃早餐
   8:00至12:00 学习
   12:00至12:30 吃午饭
   12:30至14:00 睡午觉
   14:00至18:00 学习
   18:00至19:00 吃完饭
   19:00至22:00 晚自习
   22:00至第二天早上8:00 睡觉

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

chat(client, assi_name, "现在是15:22")
print('finished')