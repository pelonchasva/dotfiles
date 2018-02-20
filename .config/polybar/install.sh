# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar > /dev/null; do sleep 1; done

# Launch bars
polybar top -c /home/andy/.config/polybar/config.top &
polybar bottom -c /home/andy/.config/poybar/config.bottom &
