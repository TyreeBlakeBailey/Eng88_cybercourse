
read -p "enter:" FIRST_NUM
read -p "enter:" SECOND_NUM
Addition=`expr $FIRST_NUM + $SECOND_NUM`
echo "$FIRST_NUM + $SECOND_NUM= "$Addition

Subtraction=`expr $FIRST_NUM - $SECOND_NUM`
echo "$FIRST_NUM - $SECOND_NUM= "$Subtraction

Multiplication=`expr $FIRST_NUM \* $SECOND_NUM`
echo "$FIRST_NUM x $SECOND_NUM= "$Multiplication

Division=`expr $FIRST_NUM / $SECOND_NUM`
echo "$FIRST_NUM / $SECOND_NUM= "$Division

