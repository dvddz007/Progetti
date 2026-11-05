echo "Inserire il primo numero: "
read x
echo "Inserire un secondo numero"
read y

n=0

while [ $y -gt 0 ]; do
	n=$(($n+$x))
	y=$(($y-1))
done

echo $n
