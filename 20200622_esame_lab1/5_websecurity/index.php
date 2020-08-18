<?php
	$account = rand(1000000,9999999);
	setcookie('Pets.com_account', $account, time() + 10000);
	setcookie('Pets.com_creditcard', base64_encode(rand(1000,9999)."-".rand(1000,9999)."-".rand(1000,9999)."-".rand(1000,9999)), time() + 10000);
	
	if(!isset($_GET['merchant']) || !isset($_GET['memo'])){
		$merchant = 'Pets.com';
		$memo = 'Royal Canin indoor light 40 (20lbs)';
	}else{
		$merchant = $_GET['merchant'];
		$memo = $_GET['memo'];
	}
	$amount = 3999; // fixed by the server
	
	header("Location: external_paymentfe48.php?account=".$account."&merchant=".$merchant."&memo=".$memo."&amount=".$amount);
	die();
?>