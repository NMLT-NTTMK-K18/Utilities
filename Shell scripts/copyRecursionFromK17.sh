#!/bin/bash

USERNAME=$1
EMAIL=$2
USER_COMMIT_MESSAGE=$3
USER_ORDER=$4
NUMBER_OF_MEMS=$5
NUMBER_OF_PROJECTS=$6
MAX_RANDOM_TIME=$7
MIN_RANDOM_TIME=$8

if [ -n "$EMAIL" ]; then
	git config --global user.email $EMAIL
else
	exit 1
fi

if [ -n "$USERNAME" ]; then
	git config --global user.name $USERNAME
else
	exit 1
fi

list_of_exercises_of_user=()
for ((num = $USER_ORDER; num <= $NUMBER_OF_PROJECTS; num = num + $NUMBER_OF_MEMS)); do
	list_of_exercises_of_user+=($(printf "%03d" "$num"))
done

echo "List of exercises of user $USER_ORDER"
echo "${list_of_exercises_of_user[@]}"
echo "---"

for i in "${list_of_exercises_of_user[@]}"; do
	if [ $(wc -c <"Bai$i/Source.cpp") -gt 100 ]; then
		echo "File already done by user, no need to copy"
		continue
	fi
	folder_dir=$(find Recursion-UIT-Together -type d -name "[Bb]ai$i*" -print -quit)
	if [ -z "${folder_dir}" ]; then
		echo "Error: Directory Bai${i} not found."
		continue
	fi
	file_dir=$(find $folder_dir -type f -name "[Bb]ai$i*.cpp" -print -quit)
	if [ -z "${file_dir}" ]; then
		echo "Error: File Bai${i} not found in directory ${folder_dir}."
		continue
	fi
	echo "Moving $file_dir from $folder_dir"
	mv -f $file_dir Bai$i/Source.cpp
	sed -i "/.*2252.*/ {N; s/.*2252.*\n//}" "Bai$i/Source.cpp"
	git add Bai$i/Source.cpp || true
	git commit -m "$USER_COMMIT_MESSAGE" || true
	echo "---"
	echo "Done commit Bai$i!"
	echo "---"
	random_number=$((RANDOM % ($MAX_RANDOM_TIME - $MIN_RANDOM_TIME + 1) + $MIN_RANDOM_TIME))
	echo "Sleeping for $random_number seconds..."
	sleep $random_number
	echo "End sleeping for $random_number ^^"
	echo "---"
done

echo "DONE!"
rm -rf Recursion-UIT-Together
