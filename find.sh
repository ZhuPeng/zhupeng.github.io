ls _posts/* | xargs grep $1
file=$(ls _posts/* | xargs grep $1 | awk -F: '{print $1}')

echo $file
open $file
