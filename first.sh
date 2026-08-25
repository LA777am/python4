#!/bin/bash
echo " hello every one this is going to be my first file"
echo " hello             hi"
num=$1
if [ $((num % 2)) -eq 0 ]; then
	echo "num is even"
elif [ $((num%2)) -ne 0 ]; then
	echo "num is odd"
fi  
