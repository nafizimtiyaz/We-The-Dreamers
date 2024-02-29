/*Charitify Theme Scripts */

(function($){
    "use strict";
             
    $(window).on('load', function() {
        $('body').addClass('loaded');
    });

/*=========================================================================
    	Sticky Header
=========================================================================*/ 
    $(function() {
        var header = $("#header"),
            height = header.height(),
            yOffset = 0,
            triggerPoint = 100;
        $('.header-height').css('height', height+'px');
        $(window).on( 'scroll', function() {
            yOffset = $(window).scrollTop();

            if (yOffset >= triggerPoint) {
            	header.removeClass("animated cssanimation fadeIn");
                header.addClass("navbar-fixed-top  cssanimation animated fadeInTop");
            } else {
                header.removeClass("navbar-fixed-top cssanimation  animated fadeInTop");
                header.addClass("animated cssanimation fadeIn");
            }

        });
    });

/*=========================================================================
    Nivo slider 
=========================================================================*/
    $('#main-slider').nivoSlider({
        effect: 'random',
        animSpeed: 300,
        pauseTime: 5000,
        directionNav: true,
        manualAdvance: false,
        controlNavThumbs: false,
        pauseOnHover: true,
        controlNav: false,
        prevText: "<i class='ti-arrow-left'></i>",
        nextText: "<i class='ti-arrow-right'></i>"
    });

/*=========================================================================
    Mobile Menu
=========================================================================*/  
    $(function(){
        $('#mainmenu').slicknav({
            prependTo: '.site-branding',
            label: '',
            allowParentLinks: true
        });
    });
             
/*=========================================================================
	Counter Up Active
=========================================================================*/
	var counterSelector = $('.counter');
	counterSelector.counterUp({
		delay: 10,
		time: 1000
	});
             
/*=========================================================================
    Event Carousel
=========================================================================*/
    $('#event-carousel').owlCarousel({
        loop: true,
        margin: 15,
        autoplay: false,
        smartSpeed: 500,
        nav: true,
        navText: ['<i class="ti-arrow-left"></i>', '<i class="ti-arrow-right"></i>'],
        dots: false,
        responsive : {
            0 : {
                items: 1
            },
            480 : {
                items: 1,
            },
            768 : {
                items: 2,
            },
            992 : {
                items: 2,
            }
        }
    });
    
    $('#about-carousel').owlCarousel({
        loop: true,
        margin: 15,
        autoplay: false,
        smartSpeed: 500,
        nav: true,
        navText: ['<i class="ti-arrow-left"></i>', '<i class="ti-arrow-right"></i>'],
        dots: false,
        responsive : {
            0 : {
                items: 1
            },
            480 : {
                items: 1,
            },
            768 : {
                items: 1,
            },
            992 : {
                items: 1,
            }
        }
    });
             
/*=========================================================================
    Isotope Active
=========================================================================*/
	$('.gallery-items').imagesLoaded( function() {

		 // Add isotope click function
		$('.gallery-filter li').on( 'click', function(){
	        $(".gallery-filter li").removeClass("active");
	        $(this).addClass("active");
	 
	        var selector = $(this).attr('data-filter');
	        $(".gallery-items").isotope({
	            filter: selector,
	            animationOptions: {
	                duration: 750,
	                easing: 'linear',
	                queue: false,
	            }
	        });
	        return false;
	    });

	    $(".gallery-items").isotope({
	        itemSelector: '.single-item',
	        layoutMode: 'masonry',
	    });
	});

/*=========================================================================
    Initialize smoothscroll plugin
=========================================================================*/
	smoothScroll.init({
		offset: 60
	});

/*=========================================================================
    Testimonial Carousel
=========================================================================*/
	$('#testimonial-carousel').owlCarousel({
        loop: true,
        margin: 15,
        autoplay: true,
        smartSpeed: 500,
        items: 1,
        nav: false,
        dots: true,
        responsive : {
			0 : {
				items: 1,
			},
			480 : {
				items: 2,
			},
			768 : {
				items: 2
			},
			992 : {
				items: 3
			}
		}
    });

/*=========================================================================
        Sponsor Carousel
=========================================================================*/
    $('#sponsor-carousel').owlCarousel({
        loop: true,
        margin: 40,
        autoplay: true,
        smartSpeed: 500,
        nav: false,
        dots: false,
        responsive : {
            0 : {
                items: 2
            },
            480 : {
                items: 3,
            },
            768 : {
                items: 4
            },
            992 : {
                items: 6
            }
        }
    });
		
/*=========================================================================
        Active venobox
=========================================================================*/
	$('.img-popup').venobox({
		numeratio: true,
		infinigall: true
	}); 

/*=========================================================================
	WOW Active
=========================================================================*/ 
    new WOW().init();             
             
/*=========================================================================
  Scroll To Top
=========================================================================*/     
    $(window).on( 'scroll', function () {
        if ($(this).scrollTop() > 100) {
            $('#scroll-to-top').fadeIn();
        } else {
            $('#scroll-to-top').fadeOut();
        }
    });

    $("[id^='show']").on("click", function() {
        var divElements = $("[class^=show]")
        var radioBtn = this.id;
        console.log(radioBtn)
        divElements.each(function(index, element) {
            if (element.classList.contains(radioBtn)) {
            $(element).show();
            } else {
            $(element).hide();
            }
        })
    });

    $(document).ready(function () {
        $('.incidentalNo').hide();
        $('#incidentalYes, #incidentalNo').change(function () {
            if ($('#incidentalNo').prop('checked')) {
                $('.incidentalNo').show();
            } else {
                $('.incidentalNo').hide();
            }
        });
    });

    $(document).ready(function () {
        $('.beforeYes').hide();
        $('#beforeYes, #beforeNo').change(function () {
            if ($('#beforeYes').prop('checked')) {
                $('.beforeYes').show();
            } else {
                $('.beforeYes').hide();
            }
        });
    });

    $(document).ready(function () {
        $('.regAdvancedYes').hide();
        $('#regAdvancedYes, #regAdvancedNo').change(function () {
            if ($('#regAdvancedYes').prop('checked')) {
                $('.regAdvancedYes').show();
            } else {
                $('.regAdvancedYes').hide();
            }
        });
    });

    $(document).ready(function () {
        $('.spendMoney').hide();
        $('#medicineYes, #medicineNo').change(function () {
            if ($('#medicineYes').prop('checked')) {
                $('.spendMoney').show();
            } else {
                $('.spendMoney').hide();
            }
        });
    });

    $(document).ready(function () {
        $('.eatingAway').hide();
        $('#eatVanueYes, #eatVanueNo').change(function () {
            if ($('#eatVanueNo').prop('checked')) {
                $('.eatingAway').show();
            } else {
                $('.eatingAway').hide();
            }
        });
    });

    $(document).ready(function () {
        $('.siteSeeingNo').hide();
        $('#siteSeeingYes, #siteSeeingNo').change(function () {
            if ($('#siteSeeingNo').prop('checked')) {
                $('.siteSeeingNo').show();
            } else {
                $('.siteSeeingNo').hide();
            }
        });
    });

    $(function(){
        $('#datepicker, #birthpicker').datepicker({
            format: "dd/mm/yyyy",
            changeMonth: true,
            changeYear: true,
            endDate: new Date(),
        });
    });

    $(function(){
        var endDate = new Date();
        endDate.setMonth(endDate.getMonth() + 3);
        $('#campPicker').datepicker({
            format: "dd/mm/yyyy",
            changeMonth: true,
            changeYear: false,
            endDate: endDate,
        });
    });

    $(function(){
        $('#estPicker').datepicker({
            format: "dd/mm/yyyy",
            changeMonth: true,
            changeYear: true,
            endDate: new Date(),
        });
    });
    $(function(){
        $('#preCamp').datepicker({
            format: "dd/mm/yyyy",
            changeMonth: true,
            changeYear: true,
            endDate: new Date(),
            multidate: true
        });
    });
             
})(jQuery);
