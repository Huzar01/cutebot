#!/bin/bash
cd /home/huzar/Projects/discord_py_bot/
#source bot-env/bin/activate
python3.7 discord_bot.py > /dev/null 2>&1 &
cd /home/huzar/Projects/discord_js_bot/
node . > /dev/null 2>&1 &

