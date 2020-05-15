#!/bin/bash
declare passwd=/etc/passwd
echo $passwd
echo "changing passwd file"
declare passwd=/home/sdaha
echo "After changing the passwd is $passwd"
declare -r pwdfile=/etc/passwd
echo $pwdfile
pwdfile=/etc/abc
echo "the pwdfile is $pwdfile can not change to /etc/abc"