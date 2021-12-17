#!/bin/sh

file1="list.txt"
file2="file2.txt"

while IFS= read -r j; do
        found=0

        while IFS= read -r i; do
                if [ $i = $j ]; then
                        found=1
                fi
        done < $file2

        if [ "$found" -ne 1 ]; then
                echo "$j not in $file2"
        fi

done < $file1

exit 0
