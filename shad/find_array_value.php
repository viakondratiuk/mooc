<?php

function f(array $a, $k) {
    $b = sort($a);
    $n = count($b);
    $i = 0;
    $j = $n -1;
    $c = 0;
    while ($i < $j) {
	if ($b[$i] + $b[$j] < $k) {
	    $i = $i + 1;
	} elseif ($b[$i] + $b[$j] > $k) {
	    $j = $j - 1;
	} else {
	    $c = $c + 1;
	    $i = $i + 1;
	    $j = $j - 1;
	}
    }
    
    return $c;
}

$inputArray = array(18, 19, 6, 13, 3, 20, 10, 1, 0, 17, 12, 4, 5, 8, 9);
$k = 25;

echo f($inputArray, $k) . "\n";