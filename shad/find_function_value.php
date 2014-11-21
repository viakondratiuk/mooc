<?php
function f($n) {
    $k = 0;
    while ($n > 0) {
	if ($n % 2 == 1)
	    $k = 1;
	return $k + f(floor($n / 2));
    }
    return 0;
}

echo f(f(f(246111))) . "\n";
?>