'''
Global configurations of the project.
e.g. URL, path, and header.
'''

# Base URL for diferent websites
SITES = ['xchuxing', 'diandong', 'cheyun', 'autohome', 'xincheping', '12365auto', 'd1ev']

BASE_URL = {
    'xchuxing': 'https://xchuxing.com',                     # 新出行
    'diandong': 'https://www.diandong.com',                 # 电动邦
    'cheyun': 'http://www.cheyun.com',                      # 车云
    'autohome': 'https://www.autohome.com.cn/beijing',      # 汽车之家
    'xincheping': 'https://www.xincheping.com',             # 新车评
    '12365auto': 'http://www.12365auto.com',                # 车质网
    'd1ev': 'https://d1ev.com',                             # 第一电动
}

# Data path
DATA_PATH = './data'
TASKS = ['task1', 'task2', 'task3']

# An example header
HEADER = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}