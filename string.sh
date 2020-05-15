#!/bin/bash
echo "enter the first string"
read st1
echo "enter the second string"
read st2
if [ "$st1" == "$st2" ]
then
 echo "Both string " $st1 "and " $st2 "matched"
else
  echo "String " $st1 "and string" $st2 "did not matched"
fi
echo "lower case first string is " ${st1^}
echo "upper case first string is " ${st1^^}