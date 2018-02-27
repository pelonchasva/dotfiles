#!/bin/bash
# i3 lockscreen  script: Pixelates screen and adds lock pic
# requires imagemagick and scrot

tmpbg="/tmp/lockscreen.png"
dir="$HOME/Pictures/overlays/"
images=($(find $(dir) -name 'lock_*.png'))
rnd=($(seq 0 $(expr ${#images[@]} - 1) | shuf))
if [ $1 ]; then
    pic=$dir'lock_'$1'.png'
else
    pic=${images[${rdn[i]}]}
fi

scrot "$tmpbg"
convert "$tmpbg" -scale 10% -scale 1000% -fill black -colorize 25% "$tmpbg"

if [ -f "$pic" ]; then
    convert "$tmpbg" "$pic" -gravity SouthEast -geometry +0+0 -composite -matte "$tmpbg"
fi

i3lock -u -n -e -i "$tmpbg" >> /dev/null
