ls _posts/* | xargs grep $1
file=$(ls _posts/* | xargs grep $1 | grep -v 'video_reco' | awk -F: '{print $1}' | sort | uniq)

echo $file
open $file

link=$(ls _posts/* | xargs grep $1 | grep -v 'video_reco' | grep 开源项目 | awk -F： '{print $NF}')
echo $link
open $link
