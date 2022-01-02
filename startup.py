import os

python_path = "/usr/bin/python3"
bot_folder = "/home/pi/python/"
filename = "bot_manager.py"

# get file and run it
bot_path = bot_folder + filename
command = 'wget https://raw.githubusercontent.com/Zaboodable/discronzo/main/bot_manager.py -q -O ' + bot_path

os.system(command)

# TODO setup service for autorun