import subprocess
import time
import os
from subprocess import check_output
import signal

python_path = "/usr/bin/python3"
bot_folder = "/home/pi/python/"
bot_filename = "bot_script.py"
bot_path = bot_folder + bot_filename

update_command = 'wget https://raw.githubusercontent.com/Zaboodable/discronzo/main/bot_script.py -q -O ' + bot_path

pid = -1


def bot_start():
    global pid
    process = subprocess.Popen([python_path, bot_path])
    pid = process.pid
    print("Bot started (%s)" % (str(pid)))

def bot_stop():
    print("Killing bot (%s)" % (str(pid)))
    os.kill(int(pid), signal.SIGTERM)

def update_bot():    
    print("Updating Bot File")
    os.system(update_command)
    time.sleep(5)

def restart_and_update():
    bot_stop()
    time.sleep(2)
    update_bot()


# get file
os.system(update_command)

# loop
restart_delay = 14400
while True:
    bot_start()
    time.sleep(restart_delay)
    restart_and_update()

