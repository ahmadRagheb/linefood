$(document).ready(function() {
	// Add smooth scrolling to all links in navbar + footer link
	$(".navbar a, footer a[href='#myPage']").on('click', function(event) {
			if (this.hash !== "") {
				event.preventDefault();
				// Store hash
				var hash = this.hash;
				// Using jQuery's animate() method to add smooth page scroll
				// The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
				$('html, body').animate({
					scrollTop: $(hash).offset().top
				}, 900, function() {
					// Add hash (#) to URL when done scrolling (default click behavior)
					window.location.hash = hash;
				});
			} 
	});
	$("#show").click(function() {
		$.ajax({
			url: "http://localhost:8000/api/resource/Products",
			method: 'GET',
			success: function(result) {
				console.log(result);
				alert("ggg");
			}
		});
	});
})

// slide elments when scroll
$(window).scroll(function() {
	$(".slideanim").each(function() {
		var pos = $(this).offset().top;
		var winTop = $(window).scrollTop();
		if (pos < winTop + 600) {
			$(this).addClass("slide1");
		}
	});
});

// nav js 
$(".nav a").on("click", function(){
	$(".nav").find(".active").removeClass("active");
	$(this).parent().addClass("active");
});

// start of slider js 
$('#myCarousel').carousel({
 interval: 10000
})
$('#myCarousel.carousel .itemm').each(function(){
 var next = $(this).next();
 if (!next.length) {
	 next = $(this).siblings(':first');
 }
 next.children(':first-child').clone().appendTo($(this));
 
 if (next.next().length>0) {
	 next.next().children(':first-child').clone().appendTo($(this));
 }
 else {
	 $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
 }
});

var cw = $('.thumbimg').width();
$('.thumbimg').css({'height':(cw)+'px'});

// start of slider js 
var slideIndex = 1;
showDivs(slideIndex);
function plusDivs(n) {
  showDivs(slideIndex += n);
}
function currentDiv(n) {
  showDivs(slideIndex = n);
}
function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
     dots[i].className = dots[i].className.replace(" w3-white", "");
  }
  x[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " w3-white";
}

// Test 
console.log("Ready !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");

// Mark page Js 
var news_name = location.href.substring(location.href.lastIndexOf('=') + 1);
window.onload = function() {
	$.ajax({
		url: "http://localhost:8000/api/method/foodline.www.marks.marks.get_Product_by_trade_mark",
		method: 'POST',
		data: {
			name: news_name
		},
		success: function(result) {
			console.log(result);
		}
	});
}

// New Page Js
var news_name = location.href.substring(location.href.lastIndexOf('=') + 1);
window.onload = function() {
	$.ajax({
		url: "http://localhost:8000/api/method/foodline.www.news.news.get_news",
		method: 'POST',
		data: {
				name: news_name
		},
		success: function(result) {
				var title = document.getElementById('title');
				var image = document.getElementById('image');
				var subject = document.getElementById('subject');
				title.innerHTML = result.message[0][0];
				image.src = result.message[0][1];
				subject.innerHTML = result.message[0][2];

				console.log(result);
				// alert(result.message);
				// $("#div1").html(result);
		}
	});
}