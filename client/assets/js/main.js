(function ($) {
  "use strict";

///////////////////////////////////////////////////////
// Preloader

var introSec = document.querySelector(".intro_sec");

// Check if introSec element exists before performing operations
if (introSec) {
// Add the "animate" class
introSec.classList.add("animate");

// Set display to "none" after 1000 milliseconds (1 second)
setTimeout(function () {
  introSec.style.display = "none";
}, 1500);

// Scroll to the top of the page and allow scrolling
setTimeout(function () {
  window.scrollTo(0, 0);
  document.body.style.overflow = "unset";
}, 1500);
}

// Preloader End


// Menu

jQuery(document).ready(function () {
  jQuery('header .mainmenu').meanmenu({
      meanScreenWidth: "992",
  });
});

document.querySelectorAll('.menu-anim > li > a').forEach(button => button.innerHTML = '<div class="menu-text"><span>' + button.textContent.split('').join('</span><span>') + '</span></div>');

setTimeout(() => {
  var menu_text = document.querySelectorAll(".menu-text span");
  menu_text.forEach((item) => {
      var font_sizes = window.getComputedStyle(item, null);
      let font_size = font_sizes.getPropertyValue("font-size");
      let size_in_number = parseInt(font_size.replace("px", ""), 10);
      let new_size = parseInt(size_in_number / 3, 10);
      new_size = new_size + "px";
      if (item.innerHTML === " ") {
          item.style.width = new_size;
      }
  });
}, 1000);

// Menu End


// Search Start
document.addEventListener("click", (event) => {
const searchToggle = event.target.closest(".search-icon");
if (searchToggle) {
  searchToggle.classList.toggle("active");
}
});
// Search End


///////////////////////////////////////////////////////
// Sticky Menu
$(window).on( 'scroll', function() {
  var scroll = $(window).scrollTop();
  if (scroll >= 150) {
      $(".menu-area").addClass("sticky");
  } else {
      $(".menu-area").removeClass("sticky");
  }
});
// Sticky Menu End


///////////////////////////////////////////////////////
// Magnific Popup gallery
$('.popup-gallery').magnificPopup({
  delegate: 'a', // child items selector, by clicking on it popup will open
  gallery: {
      enabled: true
  },
  type: 'image'
  // other options
});

$('.popup-youtube').magnificPopup({
type: 'iframe'
});


$("a.vid").YouTubePopUp();

// Magnific Popup gallery End


/*Trending Slide*/

var trendingSlider = new Swiper('.trending-slider-wrap', {
slidesPerView: 3,
spaceBetween: 15,
loop:true,
speed: 1000,
breakpoints: {
  320: {
    slidesPerView: 1
  },
  480: {
    slidesPerView: 1
  },
  768: {
    slidesPerView: 2
  },
  992: {
    slidesPerView: 2
  },
  1200: {
    slidesPerView: 3
  },
  1400: {
    slidesPerView:3
  }
},
navigation: {
  nextEl: ".trending-button-next",
  prevEl: ".trending-button-prev",
},
});

//////////////////////////////////////
var trendingSliderTwo = new Swiper('.trending-slider-wrap-two', {
slidesPerView: 2.5,
spaceBetween: 15,
loop:true,
speed: 1000,
breakpoints: {
  320: {
    slidesPerView: 1
  },
  480: {
    slidesPerView: 1
  },
  768: {
    slidesPerView: 2
  },
  992: {
    slidesPerView: 2.2
  },
  1200: {
    slidesPerView: 2.5
  },
  1400: {
    slidesPerView:2.5
  }
},
navigation: {
  nextEl: ".trending-button-next-two",
  prevEl: ".trending-button-prev-two",
},
});

/*Trending Slide End*/

/*Instagram Slide*/

var instagramSlider = new Swiper('.instagram-slider', {
slidesPerView: 6.5,
spaceBetween: 10,
loop:true,
centeredSlides: true,
speed: 2500,
breakpoints: {
  0: {
    slidesPerView: 2
  },
  480: {
    slidesPerView: 3
  },
  768: {
    slidesPerView: 4
  },
  992: {
    slidesPerView: 5
  },
  1200: {
    slidesPerView: 6
  },
  1400: {
    slidesPerView:6.5
  }
},
});

/*Instagram Slide End*/

///////////////////////////////////////////////////////
// Cta Slider

var cta_slider = new Swiper('.info-slide-wrap', {
spaceBetween: 0,
speed: 1000,
pagination: {
  el: ".info-pagination",
  clickable: true,
},
loop: true,
slidesPerView: 2.5,
spaceBetween: 0,
centeredSlides: true,
breakpoints: {
  320: {
    slidesPerView: 1
  },
  480: {
    slidesPerView: 1
  },
  768: {
    slidesPerView: 2
  },
  992: {
    slidesPerView: 2
  },
  1200: {
    slidesPerView: 2.5
  },
  1400: {
    slidesPerView:2.5
  }
},
});

// Cta Slider End

///////////////////////////////////////////////////////
// Testimonial Slider

var testimonial_slider = new Swiper('.testimonial-slide-wrap', {
spaceBetween: 30,
speed: 500,
fadeEffect: { crossFade: true },
loop: true,
effect: "fade",
pagination: {
  el: ".testimonial-pagination",
  clickable: true,
},
});

// Testimonial Slider End


// Hero logo Slider

var about_slider = new Swiper('.about-slider-wrap', {
spaceBetween: 20,
centeredSlides: true,
speed: 3000,
autoplay: {
  delay: 1,
},
loop: true,
slidesPerView:'auto',
allowTouchMove: false,
disableOnInteraction: true
});

// Hero logo Slider End

// Testimonial Card
var testimonialCard = new Swiper(".testimonial-card", {
effect: "cards",
grabCursor: false,
centeredSlides: true,
initialSlide: 1,
loop: true,
rotate: true,
keyboardControl: true,
pagination: {
  el: ".testimonial-card-pagination",
  clickable: true,
},
});

// Testimonial Card End

// Hero
var heroBg = new Swiper('.hero-bg-slide', {
autoplay: {
delay: 6000,
fadeEffect: { crossFade: true },
},
effect: 'fade',
loop: true,
speed: 1000,
})


var heroImg = new Swiper('.hero-img-slide', {
fadeEffect: { crossFade: true },
effect: 'fade',
loop: true,
allowTouchMove : false,
})



var heroInfo = new Swiper('.hero-info-slide', {
spaceBetween: 24,
slidesPerView: 1,
loop: true,
fadeEffect: { crossFade: true },
effect: 'fade',
allowTouchMove : false,
navigation: {
  nextEl: ".hero-img-button-next",
},
pagination: {
  el: ".hero-img-pagination",
  clickable: true,
  renderBullet: function (index, className) {
    var images = ['assets/images/hero/hero-1.png', 'assets/images/hero/hero-2.png', 'assets/images/hero/hero-3.png'];
    return '<span class="' + className + '" style="background-image: url(\'' + images[index] + '\');"></span>';
  },
},
thumbs: {
  swiper: heroImg
}
});


// Hero End

// Food Slide
var foodSlide = new Swiper(".food-slide", {
slidesPerView: 'auto',
spaceBetween: 100,
centeredSlides: true,
preventClicks:true,
loop:true,
speed: 600,
autoplay: {
  delay: 3000,
},
breakpoints: {
  0: {
    spaceBetween: 70,
  },
  480: {
    spaceBetween: 70,
  },
  768: {
    spaceBetween: 100
  },
}, 
});

//////////////////////////////
// Menu 1
var foodmenutwoSlider = new Swiper('.food-menu-two-slider', {
slidesPerView: 3,
spaceBetween: 24,
loop:true,
speed: 1000,
breakpoints: {
  320: {
    slidesPerView: 1
  },
  480: {
    slidesPerView: 1
  },
  768: {
    slidesPerView: 2
  },
  992: {
    slidesPerView: 2
  },
  1200: {
    slidesPerView: 3
  },
  1400: {
    slidesPerView:3
  }
},
navigation: {
  nextEl: ".food-menu-two-button-next",
  prevEl: ".food-menu-two-button-prev",
},
});

//////////////////////////////
// Menu 2
var foodmenutwoSlidertwo = new Swiper('.food-menu-two-slider-two', {
slidesPerView: 3,
spaceBetween: 24,
loop:true,
speed: 1000,
breakpoints: {
  320: {
    slidesPerView: 1
  },
  480: {
    slidesPerView: 1
  },
  768: {
    slidesPerView: 2
  },
  992: {
    slidesPerView: 2
  },
  1200: {
    slidesPerView: 3
  },
  1400: {
    slidesPerView:3
  }
},
navigation: {
  nextEl: ".food-menu-two-button-next-two",
  prevEl: ".food-menu-two-button-prev-two",
},
});

//////////////////////////////
// Menu 3
var foodmenuthreeSlider = new Swiper('.food-menu-two-slider-three', {
slidesPerView: 3,
spaceBetween: 24,
loop:true,
speed: 1000,
breakpoints: {
  320: {
    slidesPerView: 1
  },
  480: {
    slidesPerView: 1
  },
  768: {
    slidesPerView: 2
  },
  992: {
    slidesPerView: 2
  },
  1200: {
    slidesPerView: 3
  },
  1400: {
    slidesPerView:3
  }
},
navigation: {
  nextEl: ".food-menu-two-button-next-three",
  prevEl: ".food-menu-two-button-prev-three",
},
});

// Food Slide End


// Chef
var chefSlider = new Swiper('.chef-slide-wrap', {
slidesPerView: 3,
spaceBetween: 24,
loop:true,
speed: 1000,
breakpoints: {
  320: {
    slidesPerView: 1
  },
  480: {
    slidesPerView: 1
  },
  768: {
    slidesPerView: 2
  },
  992: {
    slidesPerView: 2
  },
  1200: {
    slidesPerView: 3
  },
  1400: {
    slidesPerView:3
  }
}, 
pagination: {
  el: ".chef-pagination",
  clickable: true,
},
});

// Food Slide End


///////////////////////////////////////////////////////
// Bottom to top start
$(document).ready(function () {
$(window).on('scroll', (function () {
  if ($(this).scrollTop() > 100) {
    $('#scroll-top').fadeIn();
  } else {
    $('#scroll-top').fadeOut();
  }
}));
$('#scroll-top').on( 'click', function () {
  $("html, body").animate({ scrollTop: 0 }, 600);
  return false;
});
});
// Bottom to top End



///////////////////////////////////////////////////////
// Odometer Counter
$(".counter-item").each(function () {
$(this).isInViewport(function (status) {
  if (status === "entered") {
      for (var i = 0; i < document.querySelectorAll(".odometer").length; i++) {
      var el = document.querySelectorAll('.odometer')[i];
      el.innerHTML = el.getAttribute("data-odometer-final");
    }
  }
});
});


window.onload = function () {

// Custom Cursor
const cursor = document.querySelector('.cursor');

if (cursor) {
  const editCursor = e => {
    const { clientX: x, clientY: y } = e;
    cursor.style.left = x + 'px';
    cursor.style.top = y + 'px';
  };
  window.addEventListener('mousemove', editCursor);

  document.querySelectorAll("a, .cursor-pointer").forEach(item => {
    item.addEventListener('mouseover', () => {
      cursor.classList.add('cursor-active');
    });

    item.addEventListener('mouseout', () => {
      cursor.classList.remove('cursor-active');
    });
  });
}


// Wow Animation

var wow = new WOW(
  {
    boxClass:     'wow',      // animated element css class (default is wow)
    animateClass: 'animated', // animation css class (default is animated)
    offset:       0,          // distance to the element when triggering the animation (default is 0)
    mobile:       true,       // trigger animations on mobile devices (default is true)
    live:         true,       // act on asynchronously loaded content (default is true)
    callback:     function(box) {
      // the callback is fired every time an animation is started
      // the argument that is passed in is the DOM node being animated
    },
    scrollContainer: null,    // optional scroll container selector, otherwise use window,
    resetAnimation: true,     // reset animation on end (default is true)
  }
);
wow.init();


};

// Custom Cursor End


// Select2
$('.select2').select2({
  minimumResultsForSearch: Infinity,
});

// Datepicker
$(".datepicker").datepicker({
  orientation: "top"
});


// Coming Soon Countdown 

function timeConverter(UNIX_timestamp) {
var a = new Date(UNIX_timestamp * 1000);
var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
var year = a.getFullYear();
var month = months[a.getMonth()];
var date = a.getDate();
var hour = a.getHours();
var min = a.getMinutes();
var sec = a.getSeconds();
var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec;
// return time;
console.log(date);

$("#timer #days").html( date);
$("#timer #hours").html( hour);
$("#timer #minutes").html(min);
$("#timer #seconds").html( sec);
}

function makeTimer() {

var endTime = new Date("December 19, 2025 00:00:00");
var endTime = (Date.parse(endTime)) / 1000; //replace these two lines with the unix timestamp from the server

var now = new Date();
var now = (Date.parse(now) / 1000);

var timeLeft = endTime - now;

var days = Math.floor(timeLeft / 86400);
var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
var Xmas95 = new Date('December 25, 1995 23:15:30');
// console.log(Xmas95);
// console.log(Date.parse(timeLeft * 1000));
var hour = Xmas95.getHours();
// console.log(hour);

var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));

if (hours < "10") {
  hours = "0" + hours;
}
if (minutes < "10") {
  minutes = "0" + minutes;
}
if (seconds < "10") {
  seconds = "0" + seconds;
}

$("#timer #days").html( days);
$("#timer #hours").html( hours);
$("#timer #minutes").html( minutes);
$("#timer #seconds").html( seconds);

}

setInterval(function() {
makeTimer();
}, 1000);

// Coming Soon Countdown end


}(jQuery)); 