<?php

$orderAmount = $_GET['amount'];
$orderDescription = $_GET['orderDescription'];
$uniqueOrderId =$_GET['OrderID'];

$url = "https://nmbbank.gateway.mastercard.com/api/nvp/version/67";
$data = array(
"apiOperation"=>"INITIATE_CHECKOUT", 
"apiPassword"=>"70e07366fbc15832fbec759e02938bc1", 
"apiUsername"=>"merchant.993455000069",
"merchant"=>"993455000069",
"interaction.merchant.name"=>"AI4D Research Lab - AAIAC", //replace with a real merchant name 
"interaction.operation"=>"PURCHASE" ,
'interaction.cancelUrl'=>"http://localhost/paymentapp/paymentlauncher.php", // replace with a real Url on production
"order.id"=>$uniqueOrderId, // you might need to generate meaningful unique IDs for each transaction
"order.reference"=>$uniqueOrderId,
"order.description"=>$orderDescription, // replace with a good description
"order.amount"=>$orderAmount, // put here the exact amount to be paid
"order.currency"=>"USD"); // put here the exact currency you need to operate on

// finally customize/rebrand everything to match the brand your are working on, refer to the documentation

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/x-www-form-urlencoded;charset=ISO-8859-1'));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);
parse_str(urldecode($response), $response_array);

print json_encode($response_array); // absorbe and manipulate the response buffer for your next steps

?>