localectl set-locale LANG=en_US.UTF-8
xinput --set-prop 12 'libinput Natural Scrolling Enabled' 1
xsetroot -cursor_name left_ptr
xrdb -merge ~/.Xresources
eval "$(ssh-agent -s)" &
exec i3 > ~/.config/i3/i3.log 2>&1
