# env: dict = {}

# with open('env.txt', 'r') as envfile:
#     env = {
#         var_str.split('=')[0]: var_str.split('=')[1] 
#         for var_str 
#         in envfile.read().split('\n')
#     }

import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ)

try:
    TOKEN = os.environ.get('TOKEN')
    BOT_USERNAME = os.environ.get('BOT_USERNAME')
except KeyError:
    print('env.txt файл не содержит данных переменных')
