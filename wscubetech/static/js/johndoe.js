/*!
=========================================================
* JohnDoe Landing page
=========================================================

* Copyright: 2019 DevCRUD (https://devcrud.com)
* Licensed: (https://devcrud.com/licenses)
* Coded by www.devcrud.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
});

// protfolio filters
$(window).on("load", function() {
    var t = $(".portfolio-container");
    t.isotope({
        filter: ".new",
        animationOptions: {
            duration: 750,
            easing: "linear",
            queue: !1
        }
    }), $(".filters a").click(function() {
        $(".filters .active").removeClass("active"), $(this).addClass("active");
        var i = $(this).attr("data-filter");
        return t.isotope({
            filter: i,
            animationOptions: {
                duration: 750,
                easing: "linear",
                queue: !1
            }
        }), !1
    });
});


// google maps
function initMap() {
// Styles a map in night mode.
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 40.674, lng: -73.945},
        zoom: 12,
        scrollwheel:  false,
        navigationControl: false,
        mapTypeControl: false,
        scaleControl: false,
      styles: [
        {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
        {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
        {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
        {
          featureType: 'administrative.locality',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'poi',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'poi.park',
          elementType: 'geometry',
          stylers: [{color: '#263c3f'}]
        },
        {
          featureType: 'poi.park',
          elementType: 'labels.text.fill',
          stylers: [{color: '#6b9a76'}]
        },
        {
          featureType: 'road',
          elementType: 'geometry',
          stylers: [{color: '#38414e'}]
        },
        {
          featureType: 'road',
          elementType: 'geometry.stroke',
          stylers: [{color: '#212a37'}]
        },
        {
          featureType: 'road',
          elementType: 'labels.text.fill',
          stylers: [{color: '#9ca5b3'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'geometry',
          stylers: [{color: '#746855'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'geometry.stroke',
          stylers: [{color: '#1f2835'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'labels.text.fill',
          stylers: [{color: '#f3d19c'}]
        },
        {
          featureType: 'transit',
          elementType: 'geometry',
          stylers: [{color: '#2f3948'}]
        },
        {
          featureType: 'transit.station',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'water',
          elementType: 'geometry',
          stylers: [{color: '#17263c'}]
        },
        {
          featureType: 'water',
          elementType: 'labels.text.fill',
          stylers: [{color: '#515c6d'}]
        },
        {
          featureType: 'water',
          elementType: 'labels.text.stroke',
          stylers: [{color: '#17263c'}]
        }
      ]
    });
}
/* 

https://api.whatsapp.com/send?text=[post-title] [post-url]
https://wa.me/qr/7HKB4HZ7VMOVM1

https://www.facebook.com/sharer.php?u=[post-url]
https://www.facebook.com/khushal.vegad.50

https://twitter.com/share?url=[post-url]&text=[post-title]&via=[via]&hashtags=[hashtags]
https://twitter.com/khushal_vegad_?t=4AcJAXUruzkAXOhZkx1Bqg&s=08

https://www.linkedin.com/shareArticle?url=[post-url]&title=[post-title]
https://www.linkedin.com/in/khushal-vegad-2a180b1b8

$email = 'mailto:?subject=' . $[post-title] . '&body=Check out this site: '. $[post-url] .'" title="Share by Email';

https://instagram.com/_khushal_vegad_?igshid=YmMyMTA2M2Y=

*/

const facebookBtn = document.querySelector("facebook-btn");
const twitterBtn = document.querySelector("twitter-btn");
const instagramBtn = document.querySelector("instagram-btn");
const whatsappBtn = document.querySelector("whatsapp-btn");
const linkedinBtn = document.querySelector("linkedin-btn");

function init(){
  let postUrl = encodeURI(document.location.href);
  let postTitle = encodeURI("Hi everyone, please check thisout:");
  
  facebookBtn.setAttribute(
    "herf",
    `https://www.facebook.com/khushal.vegad.50`
  );

  instagramBtn.setAttribute(
    "herf",
    `https://instagram.com/_khushal_vegad_?igshid=YmMyMTA2M2Y=`
  );

  whatsappBtn.setAttribute(
    "herf",
    `https://wa.me/qr/7HKB4HZ7VMOVM1`
  );

  linkedinBtn.setAttribute(
    "herf",
    `https://www.linkedin.com/in/khushal-vegad-2a180b1b8`
  );

  twitterBtn.setAttribute(
    "herf",
   `https://twitter.com/khushal_vegad_?t=4AcJAXUruzkAXOhZkx1Bqg&s=08`
  );
}