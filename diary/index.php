<!DOCTYPE html>
<html>
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
Name: <input type="text" name="fname">
<input type="submit">
</form>

<?php
echo "Hello World</br>";
echo "I'm the php's king! \n";
$x = 5;
$y = 10;

function mtTest(){
	$GLOBALS['y'] = $GLOBALS['y'] + $GLOBALS['x'];
}
mtTest();
echo $y ;
echo strlen("</br>");
$cars=array("Volvo","BMW","Toyota");  
sort($cars);  
print_r($cars); 

$name = $_POST['fname']; 
echo $name;



?>


</body>
</html>