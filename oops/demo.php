<?php

class Fruit{
    public $name;
    public $color;
    function set_details($name,$color)
    {
        $this->name = $name;
        $this->color = $color;
    }

    function get_details()
    {
        echo "name of the fruit is $this->name";
        echo " and color is $this->color.";
    }
}

// object creation
$a = new Fruit();
$a-> set_details("banana","yellow"); //calling methods with object
echo $a-> get_details(); //printing values passed

echo "<br>";

$b = new Fruit();
$b->set_details("apple","red");
echo $b-> get_details();
?>