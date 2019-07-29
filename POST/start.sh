set times1=0
while true
do
	let "times1=times1+1"
	echo $times1
	python3 main_POST.py
done
