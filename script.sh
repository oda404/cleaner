#!/bin/bash

for i in {15..21}
do
	echo ================= Cleaning $i
	pcleaner clean -c chap$i || exit 1 
	echo ================= Cleaned $i
done

