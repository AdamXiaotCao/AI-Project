#!/bin/bash                                                                     
# bash trap command                                                             
clear;
# bash clear screen command                                                     
# bash trap function is executed when CTRL-C is pressed:                        
# bash prints message => Executing bash trap subrutine !                       
# python genetic_algorithm.py



echo $1 $2 $3 $4 $5
for a in `seq 1 2`; do
    java -cp bin com.theaigames.blockbattle.Blockbattle "python ../BotRun.py ${1} ${2} ${3} ${4} ${5}" "python ../../../AI-Project-Random/blockbattle-starterbot-python/BotRun.py" 2>err${a}.txt 1>out${a}.txt 
    echo $a
    sleep 1;
done
echo "Exit Bash Script!!!"