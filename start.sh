#!/bin/bash
cd /home/pi/yaaasss_bitch
export DISPLAY=:0
echo Getting Updates From Repository
git pull
echo Starting View!
python /home/pi/yaaasss_bitch/main.py