<?php

$srclat=$_POST['lat'];
$srclong=$_POST['lng'];
$line = $srclat.",".$srclong;
$filename = "newfile.txt";
$myfile = fopen($filename, "a") or die("Unable to open file!");
fwrite($myfile,$line.PHP_EOL);
fclose($myfile); 
