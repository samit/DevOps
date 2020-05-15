#!/bin/bash
n1=24
n2=32

echo $(( n1+n2 ))
echo $(( n1-n2 ))
echo $(( n1*n2 ))
echo $(( n1/n2 ))
echo $(( n1%n2 ))
echo $( expr $n1 + $n2 )