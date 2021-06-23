$Num1=5
$Num2=5
$Num1+$Num2

#$input= Read-Host
#$Value=$input-as[int]
#$($Value+20)
$input_string = read-host
$value1 = $input_string -as [int]
$input_string = read-host
$value2 = $input_string -as [int]

$value1 + $value2

echo $value1

