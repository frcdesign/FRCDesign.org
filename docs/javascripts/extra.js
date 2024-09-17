//This runs whenever the site loads first.
let slideIndices = [];
let slideshows;

// Next/previous controls
function plusSlides(n, no) {
    showSlides(slideIndices[no] += n, no);
}

// Thumbnail image controls
function currentSlide(n, no) {
    showSlides(slideIndices[no] = n, no);
}

function showSlides(n, no) {
    let i;
    let x = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("dot");
    if (n > x.length) {slideIndices[no] = 1}    
    if (n < 1) {slideIndices[no] = x.length}
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";  
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    x[slideIndices[no]-1].style.display = "block";  
    dots[slideIndices[no]-1].className += " active";
}

//This runs when a page loads.
document$.subscribe(function() {

    slideIndecies = [];
    slideshows = document.getElementsByClassName("slideshow-container");

    for (let no = 0; no < slideshows.length; no++) {
        slideIndices[no] = 1;
        let dotsContainer = slideshows[no].getElementsByClassName("dotsContainer")[0];
        let slides = slideshows[no].getElementsByClassName("mySlides");
        for (let i = 0; i < slides.length; i++) {
          let dot = document.createElement("span");
          dot.className = "dot";
          dot.onclick = function() { currentSlide(i+1, no); };
          dotsContainer.appendChild(dot);
        }
        showSlides(1, no);
      }
    
})