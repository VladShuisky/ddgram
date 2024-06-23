env_str = None

with open('env.txt', 'r') as envfile:
    env_str = envfile.read()


TOKEN = env_str.split('=')[1]


