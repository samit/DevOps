#!/bin/bash
car=$1
case $car in
"BMW" )
  echo "youo have BMW" ;;

"Nissan" )
echo "You have nissan" ;;

"Toyota" )
echo "You have toyota" ;;

* )
echo "No match" ;;

esac

age=100
case $age in 
10 )
echo "small" ;;

18 )
echo "Young" ;;

40 )
echo "Matured" ;;

80 )
echo "old" ;;

* )
echo "You are as good as dead"
esac

