#!/bin/bash
cd /home/soumith/gits
echo "Enter directory name"
read directory_name
curl -u 'soumithx' https://api.github.com/user/repos -d '{"name":"'$directory_name'","description":"This project is a test"}'

mkdir /home/soumith/gits/$directory_name
cd  /home/soumith/gits/$directory_name
git init
touch README.md
echo "Enter READme content"
read data
echo "$data" >> README.md
git add README.md
echo "enter message"
read m
git commit -m "$m"
git remote add origin https://github.com/soumithx/$directory_name.git
git push origin master

