<?php

if(isset($_POST['submit'])){

$ticketType = $_POST['ticketType'];


if ($ticketType =="pp-member") {
  $orderDescription="Physical Presenter (IEEE Member)";
    $amount = 80;
}
if($ticketType =="pp-nmember"){
  $orderDescription="Physical Presenter (IEEE Non Member)";
    $amount = 100;
}
if($ticketType =="pnp-member"){
  $orderDescription="Physical Non Presenter (IEEE Member)";
    $amount = 64;
}
if($ticketType =="pnp-nmember"){
  $orderDescription="Physical Non Presenter (IEEE No Member)";
    $amount = 80;
}
if ($ticketType =="op-member") {
  $orderDescription="Online Presenter (IEEE Member)";
    $amount = 64;
}
if($ticketType =="op-nmember"){
  $orderDescription="Online Presenter (IEEE Non Member)";
    $amount = 84;
}
if($ticketType =="onp-member"){
  $orderDescription="Online Non Presenter (IEEE Member)";
    $amount = 40;
}
if($ticketType =="onp-nmember"){
  $orderDescription="Online Non Presenter (IEEE Non Member)";
    $amount = 50;
}
if($ticketType =="psp"){
  $orderDescription="Physical Student Presenter";
  $amount = 50;
}
if($ticketType=="psnp"){
  $orderDescription="Physical Student Non Presenter";
    $amount = 30;
}
if($ticketType=="osp"){
  $orderDescription="Online Student Presenter";
  $amount = 30;
}
if($ticketType=="osnp"){
  $orderDescription="Online Student Non Presenter";     
  $amount = 20;
}
if($ticketType=="none"){
  header('location:ticket.php');
}

}

?>

<!DOCTYPE html>
<html>
    <head>
    <script src="https://nmbbank.gateway.mastercard.com/static/checkout/checkout.min.js" data-error="errorCallback" data-cancel="cancelCallback"></script>
        <script
			  src="https://code.jquery.com/jquery-3.7.1.min.js"
			  integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
			  crossorigin="anonymous"></script>
        <script type="text/javascript">
                   function errorCallback(error) {
                  console.log(JSON.stringify(error)); // implement your error callback suitable for the task at hand

            }
            function cancelCallback() {
                  console.log('Payment cancelled'); // implement your cancel callback suitable for the task at hand
            }
            $(document).ready(function(){

             // Get amount, orderDescription, and generate a random OrderID
            var amount = <?=$amount;?>; // 
            var orderDescription = "<?=$orderDescription;?>";
            var OrderID = Math.floor(Math.random() * 1000000); // Generate a random OrderID
     
            $.get("initiateCheckout.php",{ amount: amount, orderDescription: orderDescription, OrderID: OrderID },function(data,status,xhr){
            var responseObj=$.parseJSON(data);
            Checkout.configure({
              session: { 
            	id: responseObj.session_id
       			}
            });
            Checkout.showPaymentPage() // you might need to choose one between the two or just implement it as modal
            //Checkout.showEmbeddedPage('#embed-page');
            })
        })
        </script>
    </head>
    <body>
       
      <div id="embed-page"> </div> 
    
       
    </body>

</html>
