<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <div class="">
        <h1>HELLO WORLD</h1>
        <h1 style="background-color:blue;">Happy</h1>
        
    </div>
    <?php
        $num=100;
        for ($i=0; $i < $num; $i+=5) { 
        ?>
        <div class="">
            <h2><?php echo $i ?></h2>
            </div>
            <?php
    }
    ?>



        <?php
            $input=5;
            if ($input > 5) {
                ?>
                <div class="">
                    <h1>possible 1</h1>
                </div>
                <?php
            }
            else
            {
            ?>
                <div class="">
                    <h1>possible 2</h1>
                </div>
                <?php
            }
    ?>

</body>
</html>