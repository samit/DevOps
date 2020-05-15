#!/bin/bash
count=1000
if [ $count -eq 10 ]
then
    echo "equality operation " $count
else
    echo "not equall"
fi
greatercount=100
if [ $greatercount -le 10 ]
then
  echo "less than operation" $greatercount
else
 echo "the condition is false"
fi
if [ $greatercount -gt $count ]
then
 echo "greater than operation" $greatercount ">" $count
else
 echo "the variable " $greatercount "is less than " $count
 
fi
notequal=5
if [ $notequal -ne 10 ]
then
 echo "the data " $notequal "to 10"
 else
 echo "equall"
 fi

 withsmall=1
 if (($withsmall > 100))
 then
   echo "less"
 elif(($withsmall ==10))
 then
   echo "equall"
else
 echo "no match"
 fi

