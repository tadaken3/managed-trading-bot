import os
import subprocess
from slackbot.bot import respond_to     # @botname: で反応するデコーダ

@respond_to('ドテンくん起動')
def start_doten(message):
    message.reply('立ち上がれドテンくん！しっかり稼ぐのじゃ！')
    script_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = os.path.join(script_dir, "start_doten.sh")
    result = subprocess.call(['sh',cmd])

@respond_to('ドテンくん停止')
def stop_doten(message):
    message.reply('ドテンくんゆっくり休むのじゃ')
    script_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = os.path.join(script_dir, "stop_doten.sh")
    result = subprocess.call(['sh',cmd])
