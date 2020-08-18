<?php
	$account = $_GET['account'];
	$merchant = $_GET['merchant'];
	$memo = $_GET['memo'];
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

    
			<h4>
			  <img src="public/wamu-logo.jpg" width="220" style="padding-bottom: 4px">
			  Online Payment Service
			</h4>

			<form method="post" action="pay.php">
			  <input type="hidden" name="merchant" value="<?php echo $merchant; ?>">
			  <input type="hidden" name="amount" value="<?php echo $amount; ?>">
			  <input type="hidden" name="memo" value="<?php echo $memo; ?>">

			  <div style="margin: 8px">
			    <p class="alert alert-info">
			      <strong>Good news! You're already logged in.</strong>
			      <br>Confirm the details below to complete your payment.
			    </p>

			    <h4>Recipient</h4>
			    <dl class="clearfix">
			      <dt>Name
			      <dd>Pets.com
			      <dt>Amount
			      <dd>$39.99
			      <dt>For
			      <dd>Royal Canin Indoor Light 40 (20lbs)
			    </dl>

			    <h4>Your Account</h4>
			    <dl class="clearfix">
			      <dt>Type
			      <dd>User
			      <dt>Phone
			      <dd>******379
			      <dt>Credit card
			      <dd>*******
			      <dt>PIN
			      <dd>
			        <input type="password" name="pin" maxlength="4" style="width: 55px">
			        <small>Enter the PIN you use at the ATM.</small>
			    </dl>

			    <input type="submit" value="Pay " class="btn btn-primary">

			  </div>
			</form>

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

  <h5 style="margin-top: 20px">
    You will have a chance to confirm your order.
  </h5>
</div>

  </body>

</html>
