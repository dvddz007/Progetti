echo "Inserire la base: "
read b

echo "Inserire l'esponente"
read e

n=1

while [ $e !=  0 ]; do
	n=$(($n*$b))
	e=$(($e-1))
done

echo $n
