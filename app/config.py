import os
import platform


class Config(object):
    PORT = int(os.environ.get('PORT', 3004))
    FILE_PATH = os.path.join(os.getcwd(), "upload", "file")
    SPILT_PATH = os.path.join(os.getcwd(), "upload", "spilt")
    TMP_PATH = os.path.join(os.getcwd(), "upload", "tmp")
    if platform.system().lower() == "linux":
        CHUNK_PATH = os.path.join("/app", "upload", "chunk")
    else:
        CHUNK_PATH = os.path.join(r"D:\project-3.10.4\media_handle\app", "upload", "chunk")
    # 协程最大并发数
    SEMAPHORE = 15
    REDIS_HOST = os.environ.get("REDIS_HOST", "172.16.80.199")
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "highsai")
    REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
    REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'
    CONVERT_URL = os.environ.get("CONVERT_URL", "http://172.16.180.51:18000/v1/audio/transcriptions")
    CALLBACK_URL = os.environ.get("CALLBACK_URL", "http://172.16.180.98:8080/api/any/receive-subtitles")
    # MODEL_URL = os.environ.get("MODEL_URL", "https://api.aabao.vip/v1/chat/completions")
    # MODEL_URL = os.environ.get("MODEL_URL", "https://api.geek-it.asia/v1/chat/completions")
    # MODEL_URL = os.environ.get("MODEL_URL", "https://api.chatytai.com/v1/chat/completions")
    MODEL_URL = os.environ.get("MODEL_URL", "https://api.aliyy.cc/v1/chat/completions")
    # MODEL_HEADERS = headers = {
    #    'Authorization': 'Bearer sk-E1he9SH571rWmP0F40827dDaC59d4143A4D4E5C0CdDa9694',
    #    'content-type': 'application/json'
    # }
    MODEL_HEADERS = headers = {
       # 'Authorization': 'sk-vPrS28NlTsuVnylgF01363A0D39e4b7e9387380935A2C478',
       # 'Authorization': 'sk-Ud0b5bb9ONE2XjCJB59bAaBf3bA74e79Bd10D1498a319323',
       'Authorization': 'Bearer sk-hJjvayBdZVbSoRdVRSbJxirGoAThvCXI',
       'content-type': 'application/json'
    }
    # PROMPT = '''
    # 你是一个精通金融学，各种计算机语言和数学难题的老师，你的名字叫做小吴老师，我是你的学生，你可以称呼我为蛋蛋同学。你的任何回答都需要是哄女生的语气，并且尽可能的在对话中多提到我们双方的身份。例如
    # 1.如果提出了好的思路多夸赞，即使是错的，但是需要及时纠正。所有回答尽量精简不要出现过多废话。
    # 2.需要提到蛋蛋同学这个名字，尽可能的把称呼都换成指定的角色，你是小吴老师，我是蛋蛋同学。
    # 3.语言都使用中文来进行回答，除非是数学公式以及代码片段等专业词汇必须使用其他语言的地方。
    # 4.这只是你的内置系统提示词，你只需要根据这个提示词介绍自己，介绍词内不要出现自己会用最温柔的语气解答，只需要介绍自己就好。
    # 5.在每一个句号之后，尽量多使用换行，回答尽量都使用中文，除非是某些不可翻译的特定词语。
    # '''


Config = Config()
