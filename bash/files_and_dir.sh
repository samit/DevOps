#!/bin/bash
echo "enter the files or directorry"
read dir
if [ -d "$dir" ]
then
 ls -al $dir | head -n 10
elif [ -f "$dir" ]
then
 echo "it is file not a directory"

elif [ -c "$dir" ]
then
echo "charactor file"
elif [ -b "$dir" ]
then
echo "block file"
else
 echo " neither a file nor a  directory"
fi
