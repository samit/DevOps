#!/bin/bash
: 'num=1
while [ $num -lt 10 ]
do
echo $num
num=$(( num+1 ))
done'

num=1
until [ $num -ge 10 ]
do
echo $num
num=$((num+1))
done
for i in  {0..20} # {0..20..2}{start..end..increment}
do
echo $i
done