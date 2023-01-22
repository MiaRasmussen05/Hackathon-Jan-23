let div = document.getElementById("popup");

//function popUp() {
//    console.log("running");
//}


// Carousel Swiper
var swiper = new Swiper(".mySwiperComment", {
     slidesPerView: 3,
     spaceBetween: 30,
     slidesPerGroup: 3,
    //  loop: true,
     loopFillGroupWithBlank: true,
     pagination: {
       el: ".swiper-pagination",
       clickable: true,
     },
     navigation: {
       nextEl: ".swiper-button-next",
       prevEl: ".swiper-button-prev",
     },
});

var swiper = new Swiper(".mySwiper", {
  slidesPerView: 4,
  spaceBetween: 0,
  slidesPerGroup: 3,
 //  loop: true,
  loopFillGroupWithBlank: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});