#!/bin/bash
# bash trap command
trap bashtrap INT
pid=$!
./hello_world.sh &
sleep 2
# Kill it
kill $PID
# bash clear screen command
# bash trap function is executed when CTRL-C is pressed:
# bash prints message => Executing bash trap subrutine !
bashtrap()
{
    echo "CTRL+C Detected !...executing bash trap !"
}
# for loop from 1/10 to 10/10
for a in `seq 1 3`; do
    cat pi | python BotRun.py
    echo $a
    sleep 1;
    kill -INT $pid
done
echo "Exit Bash Trap Example!!!" 