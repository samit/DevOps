#!/bin/bash
age=2
if [ "$age" -gt 18 ] && [ "$age" -lt 40 ]
then
echo "you are young and you can enter the pub"
elif [ "$age" -lt 18 ] && [ "$age" -lt 10 ]
then
echo "You are too small child are not allowed "
else
echo "You are matured"
fi
count=10
if [[ "$count" -lt 20 && "$count" -gt 5 ]]
then
echo "you are in "
else
echo "You are out"
fi

if [ "$count" -lt 20 -a "$count" -gt 5 ]
then
echo "you are in "
else
echo "You are out"
fi

if [ "$count" -lt 20 -o "$count" -gt 5 ]
then
echo "you are in "
else
echo "You are out"
fi
#|| for or
