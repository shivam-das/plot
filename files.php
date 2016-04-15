<html>
<body>
    <?php
            if (isset($_FILES['my_file'])) {
                $myFile = $_FILES['my_file'];
                $fileCount = count($myFile["name"]);
                 $myfile = fopen("trails.txt", "a") or die("Unable to open file!");

                for ($i = 0; $i < $fileCount; $i++) {
                    ?>
                        
                    
                <?php
                       
                        fwrite($myfile,$myFile["name"][$i].PHP_EOL);
                       
                }
                
            }
     fclose($myfile);
    
?>
    ?>
</body>
</html>