<html>
    <body>
    <?php

$filename = "newfile.txt";
if(file_exists($filename)){
    unlink($filename);
    echo "File deleted";
}
$myFile = fopen($filename,"w") or die("Unable to create a file.");
fwrite($myFile,"Lat,Lng".PHP_EOL);
fclose($myFile);

?>
        </body>
</html>