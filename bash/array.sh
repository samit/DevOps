#!/bin/bash
arr=('sda' 'sdahal' 'samit' 'sanjaya')
echo ${arr[@]}
echo ${#arr[@]}
echo ${!arr[@]}
unset arr[3]
echo ${arr[@]}
arr[3]='indu'
echo ${arr[@]}