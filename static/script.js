/* Установить ширину боковой панели с шириной 250 пикселей и следующий */
// function openNav() {
//     document.getElementById("mySidenav").style.width = "250px";
//   }
  
//   /* Установите ширину боковой навигации в 0 */
//   function closeNav() {
//     document.getElementById("mySidenav").style.width = "0";
//   }




  var slideIndex = 1;
  showSlides(slideIndex);
  
  // Вперед/назад элементы управления
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
  // Элементы управления миниатюрами изображений
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  
  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
  }





  function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

// Добавим обработчики клика для каждого пункта меню
document.getElementById("bashkybet-link").addEventListener("click", function() {
  window.location.href = "index.html";
  closeNav(); // Закрываем меню после перехода
});

document.getElementById("courses-link").addEventListener("click", function() {
    window.location.href = "courses.html";
    closeNav(); // Закрываем меню после перехода
});

document.getElementById("teachers-link").addEventListener("click", function() {
    window.location.href = "teachers.html";
    closeNav();
});

document.getElementById("videos-link").addEventListener("click", function() {
    window.location.href = "videos.html";
    closeNav();
});






document.getElementById("login-link").addEventListener("click", function() {
  window.location.href = "login.html";
  closeNav(); // Закрываем меню после перехода
});

document.getElementById("register-link").addEventListener("click", function() {
  window.location.href = "register.html";
  closeNav(); // Закрываем меню после перехода
});