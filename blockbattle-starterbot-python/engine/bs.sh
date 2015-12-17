#!/bin/bash
# bash trap command
clear;
# bash clear screen command
# bash trap function is executed when CTRL-C is pressed:
# bash prints message => Executing bash trap subrutine !
# python genetic_algorithm.py



echo $1 $2 $3 $4 $5 $6 $7 $8 $9 ${10}
java -cp bin com.theaigames.blockbattle.Blockbattle "python ../BotRun.py ${1} ${2} ${3} ${4} ${5}" "python ../BotRun.py ${6} ${7} ${8} ${9} ${10}" 2>err.txt 1>out.txt
# echo "Exit Bash Script!!!"
