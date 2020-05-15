#!/bin/bash
echo "Enter the file that you want to read"
read file
if [ -f $file ]
then
  echo "reading $file line by line"
  while IFS=  read -r line
    do
    echo $line| cut -f 1 -d ':'
    done < $file
else
echo "file does not exist"
fi
