#!/bin/bash

echo "raspberry" | sudo -S xset s off
echo "raspberry" | sudo -S xset -dpms
echo "raspberry" | sudo -S xset s noblank

cd /home/pi/yaaasss_bitch
export DISPLAY=:0
echo Getting Updates From Repository
git pull
echo Starting View!
python /home/pi/yaaasss_bitch/main.py