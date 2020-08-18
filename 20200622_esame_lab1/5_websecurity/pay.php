<?php
	$memo = trim($_POST['memo']);
	$memo = str_replace('<script>', '', $memo);
?>
<!doctype html>
<html>
  
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<head>
    <meta charset="utf-8">
    <title>Pets.com bank</title>
    <link rel="stylesheet" href="public/bootstrap.css">
  </head>

  <body>

<div class="center-block" style="width: 480px">
  <h4>
    <img src="public/pets-com-logo.gif" style="padding-bottom: 10px">
    Authorize payment with your bank
  </h4>

			  <div style="margin: 8px">
			    <p class="alert alert-info">
			      <strong>The payment has been completed</strong>
			      <br>You will recive a mail confirmations about: <?php echo $memo ?> 
			   </p>
			   
			<style>
			  dl dt {
			    float: left;
			    clear: left;
			    width: 100px;
			  }

			  dl dd {
			    float: left;
			  }

			  input {
			    font-size: 11px;
			  }
			</style>

			<script src="public/jquery.js"></script>

</div>

  </body>

</html>
