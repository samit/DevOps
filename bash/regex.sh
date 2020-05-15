#!/bin/bash
echo "Extracting ip addresses"
grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" regex.txt

echo "Extracting the email addresses"

grep -E -o "[a-zA-Z0-9\.\+\_\!]+\@[a-zA-Z0-9]+\.\w+" regex.txt

echo "Extracting the phone number"

grep -E -o "(\([0-9]{1,3}\)|[0-9]{1,3})[ \-]?[0-9]{1,3}[ \-]?[0-9]{1,3}[ \-]?[0-9]{1,4}" regex.txt

echo "Extracting user name"

grep -E -o "Mr[s]?[ \.]?\w+" regex.txt

echo "Extracting  web url"
grep -E -o "http[s]?://(www\.|[a-zA-Z0-9]+\.)?[a-zA-Z0-9]+\.\w+" regex.txt
