env: dict = {}

with open('env.txt', 'r') as envfile:
    env = {
        var_str.split('=')[0]: var_str.split('=')[1] 
        for var_str 
        in envfile.read().split('\n')
    }

try:
    TOKEN = env.get('TOKEN')
    BOT_USERNAME = env.get('BOT_USERNAME')
except KeyError:
    print('env.txt файл не содержит данных переменных')
