<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AAIAC 2023 | Registration</title>
<!-- Stylesheets -->
<link href="assets/css/bootstrap.min.css" rel="stylesheet">
<link href="assets/plugins/revolution/css/settings.css" rel="stylesheet" type="text/css"><!-- REVOLUTION SETTINGS STYLES -->
<link href="assets/plugins/revolution/css/layers.css" rel="stylesheet" type="text/css"><!-- REVOLUTION LAYERS STYLES -->
<link href="assets/plugins/revolution/css/navigation.css" rel="stylesheet" type="text/css"><!-- REVOLUTION NAVIGATION STYLES -->
<link href="assets/css/style.css" rel="stylesheet">
<link href="assets/css/responsive.css" rel="stylesheet">
<script src="assets/js/jquery.js"></script>
<link rel="shortcut icon" href="assets/images/icon-colored.png" type="image/x-icon">
<link rel="icon" href="assets/images/icon-light.png" type="image/x-icon">
<!--Color Switcher Mockup-->
<link href="assets/css/color-switcher-design.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/css/intlTelInput.css">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
<!-- Responsive -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
<!--[if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.js"></script><![endif]-->
<!--[if lt IE 9]><script src="js/respond.js"></script><![endif]-->
<script src="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/intlTelInput.min.js"></script>
<script src="assets/js/payment.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
<script type="text/javascript">
    $(document).ready(function(){
        $("#valid").hide();
        //   const input = document.querySelector("#phone");
        //   window.intlTelInput(input, {
        //     utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js",
        //   });

    $("#ticketType").change(function(){
     var tt = $(this).val();
     if (tt=="pp-member") {
        $("#valid").hide();
        $("#tt").html("Physical Presenter (IEEE Member)");
        $("#total").html("$80");
     }
     if(tt=="pp-nmember"){
        $("#valid").hide();
        $("#tt").html("Physical Presenter (IEEE Non Member)");
        $("#total").html("$100");
     }
     if(tt=="pnp-member"){
        $("#valid").hide();
        $("#tt").html("Physical Non Presenter (IEEE Member)");
        $("#total").html("$64");
     }
     if(tt=="pnp-nmember"){
        $("#valid").hide();
        $("#tt").html("Physical Non Presenter (IEEE Non Member)");
        $("#total").html("$80");
     }
     if (tt=="op-member") {
        $("#valid").hide();
        $("#tt").html("Online Presenter (IEEE Member)");
        $("#total").html("$64");
     }
     if(tt=="op-nmember"){
        $("#tt").html("Online Presenter (IEEE Non Member)");
        $("#total").html("$84");
     }
     if(tt=="onp-member"){
        $("#valid").hide();
        $("#tt").html("Online Non Presenter (IEEE Member)");
        $("#total").html("$40");
     }
     if(tt=="onp-nmember"){
        $("#valid").hide();
        $("#tt").html("Online Non Presenter (IEEE Non Member)");
        $("#total").html("$50");
     }
     if(tt=="psp"){
        $("#valid").hide();
        $("#tt").html("Physical Student Presenter");
        $("#total").html("$50");
     }
     if(tt=="psnp"){
        $("#valid").hide();
        $("#tt").html("Physical Student Non Presenter");
        $("#total").html("$30");
     }
     if(tt=="osp"){
        $("#valid").hide();
        $("#tt").html("Online Student Presenter");
        $("#total").html("$30");
     }
     if(tt=="osnp"){
        $("#valid").hide();
        $("#tt").html("Online Student Non Presenter");
        $("#total").html("$20");
     }
     if(tt=="none"){
        $("#valid").show();
        $("#tt").html("Not Selected");
        $("#total").html("$00");
     }


    });


});



   
</script>
</head>

<body>

<div class="page-wrapper">

    <!-- Preloader -->
    <!-- <div class="preloader"></div> -->

    <!-- Main Header-->
    <header class="main-header header-style-one">

        
        <!-- Header Lower -->
        <div class="header">
            <div class="" >    
                <!-- Main box -->
                <div class="main-box">


                    <div class="nav-outer">

                        <!-- Main Menu -->
                        <nav class="main-menu navbar-expand-md">
                            <div class="navbar-collapse collapse clearfix" id="navbarSupportedContent">
                                <ul class="navigation clearfix">
                                    <li><a href="./index.html">Home</a></li>
                                    <li><a href="./index.html#about">About</a></li>
                                    <li><a href="./contacts.html">Contact us</a></li>
                                </ul>
                            </div>
                        </nav>
                        

                    </div>
                </div>
            </div>
        </div>

        <!-- Sticky Header  -->
        <div class="sticky-header">
            <div class="auto-container">            

                <div class="main-box">
                    <div class="logo-box">
                        <div class="logo"><a href="index.html"><img src="assets/images/logo-colored.png" alt="" title=""></a></div>
                        <div class="upper-right">
                            <div class="search-box">
                                <button class="search-btn mobile-search-btn"><i class="flaticon-search-2"></i></button>
                            </div>
                            <a href="#nav-mobile" class="mobile-nav-toggler navbar-trigger"><i class="flaticon-menu"></i></a>
                        </div>
                    </div>
                    
                    <nav class="main-menu navbar-expand-md">
                        <!--Keep This Empty / Menu will come through Javascript-->
                    </nav>
                </div>
            </div>
        </div><!-- End Sticky Menu -->

        <!-- Mobile Header -->
        <div class="mobile-header">
            <div class="logo"><a href="index.html"><img src="assets/images/logo-colored.png" alt="" title=""></a></div>

            <!--Nav Box-->
            <div class="nav-outer clearfix">
                <div class="outer-box">
                    <!-- Search Btn -->
                    <div class="search-box">
                        <button class="search-btn mobile-search-btn"><i class="flaticon-search-2"></i></button>
                    </div>

                    <a href="#nav-mobile" class="mobile-nav-toggler navbar-trigger"><i class="flaticon-menu"></i></a>
                </div>
            </div>
        </div>

        <!-- Mobile Menu  -->
        <div class="mobile-menu">
            <div class="menu-backdrop"></div>
            
            <!--Here Menu Will Come Automatically Via Javascript / Same Menu as in Header-->
            <nav class="menu-box">
                <div class="upper-box">
                    <div class="nav-logo"><a href="index.html"><img src="assets/images/logo-colored.png" alt="" title=""></a></div>
                    <div class="close-btn"><i class="icon flaticon-close"></i></div>
                </div>

                <ul class="navigation clearfix"><!--Keep This Empty / Menu will come through Javascript--></ul>

                <ul class="contact-list-one">
                    <li><i class="flaticon-location"></i> P. O. Box 490, Dodoma, Tanzania <strong>Address</strong></li>
                    <li><i class="flaticon-alarm-clock-1"></i>Monday - Friday 9am - 4pm <strong>Timeing</strong></li>
                    <li><i class="flaticon-email-1"></i> <a href="mailto:conference@ai4dlab.or.tz">conference@ai4dlab.or.tz</a> <strong>Mail to us</strong></li>
                </ul>

                <ul class="social-links">
                    <li><a href="#"><span class="fab fa-facebook-f"></span></a></li>
                    <li><a href="#"><span class="fab fa-pinterest"></span></a></li>
                    <li><a href="#"><span class="fab fa-twitter"></span></a></li>
                    <li><a href="#"><span class="fab fa-dribbble"></span></a></li>
                </ul>
            </nav>
        </div><!-- End Mobile Menu -->

        <!-- Header Search -->
        <div class="search-popup">
            <button class="close-search"><i class="flaticon-close"></i></button>
            <form method="post" action="blog.html">
                <div class="form-group">
                    <input type="search" name="search-field" value="" placeholder="Search" required="">
                    <button type="submit"><i class="fa fa-search"></i></button>
                </div>
            </form>
        </div>
        <!-- End Header Search -->

    </header>
    <!--End Main Header -->

    <!-- Hidden bar back drop -->
    <div class="form-back-drop"></div>

    <!-- Hidden Bar -->
    <section class="hidden-bar">
        <div class="inner-box">
            <div class="title-box">
                <h2>Contact Us</h2>
                <div class="cross-icon"><span class="fa fa-times"></span></div>
            </div>  

            <ul class="contact-list-one">
                <li><i class="flaticon-location"></i> P. O. Box 490, Dodoma <strong>Address</strong></li>
                <li><i class="flaticon-alarm-clock-1"></i>Wednesday - Thursday 9am - 6pm <strong>Timeing</strong></li>
                <li><i class="flaticon-email-1"></i> <a href="mailto:envato@gmail.com">conference@ai4dlab.or.tz</a> <strong>Mail to us</strong></li>
            </ul>
        </div>
    </section>
    <!--End Hidden Bar -->

    <!--Page Title-->
    <section class="page-title" style="background-image: url(images/background/11.jpg);">
        <div class="anim-icons full-width">
            <span class="icon icon-bull-eye"></span>
            <span class="icon icon-dotted-circle"></span>
        </div>
        <div class="auto-container">
            <div class="title-outer">
                <h1>Register</h1>
                <ul class="page-breadcrumb">
                    <li><a href="index.html">Home</a></li>
                    <li>Checkout</li>
                </ul> 
            </div>
        </div>
    </section>
    <!--End Page Title-->

    <!--Checkout Page-->
    <div class="checkout-page">
        <div class="auto-container">
                
            <!--Billing Details-->
            <div class="billing-details">
                <div class="shop-form">
                    <form  enctype="multipart/form-data" action="paymentlauncher.php" method="POST">
                        <div class="row clearfix">
                            <div class="col-lg-7 col-md-12 col-sm-12">
                
                                <div class="sec-title"><h2>Registration</h2></div>
                                <div class="billing-inner">
                                    <div class="row clearfix">

                                        <!--Form Group-->
                                        <div class="form-group col-md-12 col-sm-12 col-xs-12">
                                            <div class="field-label">Register Here</div>
                                            <select autocomplete="off" name="ticketType" id="ticketType">
                                                <option selected="selected" value = "none">Select a package</option>
                                                <option value="pp-member">Physical Presenter (IEEE Member)</option>
                                                <option value="pp-nmember">Physical Presenter (IEEE Non-Member)</option>
                                                <option value="pnp-member">Physical Non Presenter (IEEE Member)</option>
                                                <option value="pnp-nmember">Physical Non Presenter (IEEE Non-Member)</option>
                                                <option value="op-member">Online Presenter (IEEE Member)</option>
                                                <option value="op-nmember">Online Presenter (IEEE Non-Member)</option>
                                                <option value="onp-member">Online Non Presenter (IEEE Member)</option>
                                                <option value="onp-nmember">Online Non Presenter (IEEE Non-Member)</option>
                                                <option value="psp">Physical Student Presenter</option>
                                                <option value="psnp">Physical Student Non Presenter</option>
                                                <option value="osp">Online Student Presenter</option>
                                                <option value="osnp">Online Student Non Presenter</option>
                                            </select><br>
                                            <div class="field-label text-danger" id="valid">Please select a valid ticket! </div>
                                        </div>
      
                                        
                                    </div>
                                </div>
                            </div>

                            
                            <div class="col-lg-5 col-md-12 col-sm-12">
                                <div class="sec-title"><h2>Registration Details</h2></div>
                                <div class="shop-order-box">
                                    <ul class="order-list">
                                        <li>Package Type</li>
                                        <li id="tt">Not Selected</li>
                                        <li class="total">Total Fee<span class="dark" id="total">$00</span></li>
                                    </ul>
                                    
                                    
                                    <!--Place Order-->
                                    <div class="place-order">
                                        <!--Payment Options-->
                                        <div class="radio-option">
                                            <!-- <img src="assets/images/resource/paypall.jpg" alt="" /></label> -->
                                        </div>
                                        <div class="row">
                                            <div class="col-md-12">
                                            <button type="submit" name="submit" class="theme-btn btn-style-one" style="width:100%;" ><span class="btn-title">Credit Card</span></button>
                                            </div><hr>
                                            <div class="col-md-6">
                                            <a href="mobile_money.php" name="submit" class="theme-btn btn-style-one pull-right" ><span class="btn-title">Mobile Money</span></a>
                                            </div>
                                            <div class="col-md-6">
                                            <a href="wire_transfer.php" name="submit" class="theme-btn btn-style-one pull-right" ><span class="btn-title">Wire Transfer</span></a>
                                            </div>
                                        </div>
                                       
                                       
                                        
                                        
                                    </div>
                                    <!--End Place Order-->
                                    
                                </div>
                                
                                
                            </div>
                        </div>                             
                    </form>
                    
                </div>
                
            </div><!--End Billing Details-->
        </div>
    </div>




    <!-- Main Footer -->
    <footer class="main-footer" id="contact">
        <div class="auto-container">
            <!-- Footer Content -->
            <div class="footer-content wow fadeInUp">
                <div class="text-center">
                    <div class="footer-logo"><a href="#"><img src="assets/images/logo-light.png" alt=""></a></div>
                    <div class="text">Artificial Intelligence for Development AI4D - Lab A unique collaboration between UDOM & NM-AIST to foster Research, Training and Innovation in AI. The Lab is funded by IDRC and Sida through the AI4D Africa Program.</div> 
                    <hr>
                    <div class="row">
                        <div class="col-md-4">
                            <figure class="image-box"><a href="#" ><img src="assets/images/clients/idrc.jpg" alt="" width="150" height="100"></a></figure>
                        </div>
                        <div class="col-md-4">
                            <figure class="image-box"><a href="#"><img src="assets/images/clients/Sida.jpg" alt="" width="150" height="100"></a></figure>
                        </div>
                        <div class="col-md-4">
                            <figure class="image-box"><a href="#"><img src="assets/images/clients/ai4d.jpg" alt="" width="150" height="100"></a></figure>
                        </div>
                    </div>
                </div>
                <hr>
                <ul class="social-icon-two">
                    <li><a href="https://twitter.com/ai4dlab_Tz"><span class="fab fa-twitter"></span></a></li>
                    <li><a href="https://www.linkedin.com/company/ai4d-anglophone/mycompany/"><span class="fab fa-linkedin"></span></a></li>
                </ul>
                <ul class="contact-list-one">
                    <li><i class="flaticon-location"></i> P. O. Box 490, Dodoma, Tanzania <strong>Address</strong></li>
                    <li><i class="flaticon-alarm-clock-1"></i>Monday - Friday 9am - 4pm <strong>Timing</strong></li>
                    <li><i class="flaticon-email-1"></i> <a href="mailto:envato@gmail.com">conference@ai4dlab.or.tz</a> <strong>Mail to us</strong></li>
                </ul>
            </div>
        </div>

        <div class="footer-bottom">
            <div class="auto-container">
                <div class="inner-container">
                    <ul class="footer-nav">
                       <li><a href="#">Terms of Service</a></li> 
                       <li><a href="#">Privacy Policy</a></li> 
                    </ul>
                    
                    <div class="copyright-text">
                        <p>Copyright © 2023 All Rights Reserved. Developed by <a href="https://nsoma.me">Nsoma</a></p>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <!-- End Footer -->

</div>
<!-- End Page Wrapper -->

<!--Scroll to top-->
<div class="scroll-to-top scroll-to-target" data-target="html"><span class="fa fa-angle-up"></span></div>


<script src="assets/js/jquery.js"></script>
<script src="assets/js/popper.min.js"></script>
<!--Revolution Slider-->
<script src="assets/plugins/revolution/js/jquery.themepunch.revolution.min.js"></script>
<script src="assets/plugins/revolution/js/jquery.themepunch.tools.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.actions.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.carousel.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.kenburn.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.layeranimation.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.migration.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.navigation.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.parallax.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.slideanims.min.js"></script>
<script src="assets/plugins/revolution/js/extensions/revolution.extension.video.min.js"></script>
<script src="assets/js/main-slider-script.js"></script>
<!--Revolution Slider-->
<script src="assets/js/bootstrap.min.js"></script>
<script src="assets/js/jquery.fancybox.js"></script>
<script src="assets/js/jquery.countdown.js"></script>
<script src="assets/js/appear.js"></script>
<script src="assets/js/owl.js"></script>
<script src="assets/js/wow.js"></script>
<script src="assets/js/script.js"></script>
</body>
</html>