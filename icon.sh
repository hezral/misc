#!/bin/bash

#convert ico files to png
for i in *.ico; do mkdir ${i/.ico/}; mv $i ${i/.ico/}; cd ${i/.ico/}; convert $i -set filename:mysize '%wx%h' ${i/-2016.ico/}_%[filename:mysize].png; cd ..; done


for i in *@256.png; do convert -resize '16x16' $i ${i/@16}; done
for i in *@256.png; do convert -resize '32x32' $i ${i/@32}; done
for i in *@256.png; do convert -resize '48x48' $i ${i/@48}; done
for i in *@256.png; do convert -resize '64x64' $i ${i/@64}; done
for i in *@256.png; do convert -resize '128x128' $i ${i/@128}; done


#move files into each folder
for i in *.*; do j=$i; IFS=\@; arr=($i); dir=${arr[0]}; [ -d $dir ] || mkdir $dir; mv ${arr[0]}@${arr[1]} $dir; done
unset IFS
#go into each folder and convert to ico
for k in *; do cd $k; for x in *.png; do z+="${x} "; done; convert $z "${k}.ico"; x=''; z=''; cd ..; done

find . -name '*.ico' -exec cp {} /home/adi/Work/eWay-CRM/to_upload/ \; 

#go into each folder and convert to ico, using resize 
for k in *; do cd $k; for x in *@256.png; do convert $x -define icon:auto-resize=128,64,48,32,16 "${k}.ico"; cd ..; done; done

for k in *; do cd $k; png2icns ${k}.icns ${k}@*.png; cd ..; done




for k in *; do cd $k; for i in *@256.png; do echo convert -resize '16x16' $i ${i/@256/@16}; done; cd ..; done
for k in *; do cd $k; for i in *@256.png; do convert -resize '32x32' $i ${i/@256/@32}; done; cd ..; done
for k in *; do cd $k; for i in *@256.png; do convert -resize '48x48' $i ${i/@256/@48}; done; cd ..; done
for k in *; do cd $k; for i in *@256.png; do convert -resize '64x64' $i ${i/@256/@64}; done; cd ..; done
for k in *; do cd $k; for i in *@256.png; do convert -resize '128x128' $i ${i/@256/@128}; done; cd ..; done







for i in *.*; do j=$i; IFS=\@; arr=($i); dir=${arr[0]}; [ -d $dir ] || mkdir $dir; mv ${arr[0]}@${arr[1]} $dir; done; unset IFS; for k in *; do cd $k; for x in *.png; do z+="${x} "; done; convert $z "${k}.ico"; x=''; z=''; cd ..; done; find . -name '*.ico' -exec cp {} /home/adi/Cloud/OneDrive/Icons\ 2016\ to\ 2019/Icons-Light-Mode/ \;; for d in *; do if [ -d /home/adi/Work/eWay-CRM/Icons-Source-Light/$d ]; then rm -rf /home/adi/Work/eWay-CRM/Icons-Source-Light/$d; mv $d /home/adi/Work/eWay-CRM/Icons-Source-Light/; else mv $d /home/adi/Work/eWay-CRM/Icons-Source-Light/; fi; done


for i in *.*; do j=$i; IFS=\@; arr=($i); dir=${arr[0]}; [ -d $dir ] || mkdir $dir; mv ${arr[0]}@${arr[1]} $dir; done; unset IFS; for k in *; do cd $k; for x in *.png; do z+="${x} "; done; convert $z "${k}.ico"; x=''; z=''; cd ..; done; find . -name '*.ico' -exec cp {} /home/adi/Cloud/OneDrive/Icons\ 2016\ to\ 2019/Icons-Dark-Mode/ \;; for d in *; do if [ -d /home/adi/Work/eWay-CRM/Icons-Source-Dark/$d ]; then rm -rf /home/adi/Work/eWay-CRM/Icons-Source-Dark/$d; mv $d /home/adi/Work/eWay-CRM/Icons-Source-Dark/; else mv $d /home/adi/Work/eWay-CRM/Icons-Source-Dark/; fi; done


for i in *.*; do j=$i; IFS=\@; arr=($i); dir=${arr[0]}; [ -d $dir ] || mkdir $dir; mv ${arr[0]}@${arr[1]} $dir; done; unset IFS; for k in *; do cd $k; for x in *.png; do z+="${x} "; done; convert $z "${k}.ico"; x=''; z=''; cd ..; done; find . -name '*.ico' -exec cp {} . \;; rm -rf $k














