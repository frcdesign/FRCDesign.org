# 1A: Onshape Fundamentals


## Multi-Part Modeling

Onshape is a software focused on a *top-down design* workflow (explored more in [Stage 1C](1C-designMethodology.md "Learning Course Stage 1C Page"){:target="_blank"}) using multi-part part studios. It allows you to create several different related parts in the same tab, all referencing each other, making the part creation for something like a subsystem easy.

### Learning Center Course
**Complete the following Onshape Learning Course:**

- The [**Multi-Part Part Studios**](https://learn.onshape.com/courses/fundamentals-multi-part-part-studios "Multi-Part Part Studios Onshape Learning Course"){:target="_blank"} course runs you through top-down design principles, sketching for multiple parts (master sketches), and some more practical skills for working with multiple parts in a part studio.

Check out [this page](../../best-practices/sub-document-setup.md "Sub-Document Best Practices Page"){:target="_blank"} to learn more about best practices for sub-documents. The following practice exercises will help you reinforce these concepts.

!!! Example "Multi-Part Part Studio Example"
    Notice how there's one instance of each unique part within this part studio. The part studio also resembles the completed product, as the parts are modeled relative to each other.
    <center><img src="\img\learning-course\stage1a\1a-PartStudio.webp" width="55%"></center>
    <center> *Example of a part studio* </center>

!!! Warning "<span style="font-size: 0.8rem !important;">**DO NOT MOVE PAST THIS POINT UNTIL YOU HAVE COMPLETED THE LEARNING COURSE ABOVE**</span>"

<br>



<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>
// Initialize slide index for each slideshow
let slideIndices = [];

let slideshows = document.getElementsByClassName("slideshow-container");
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

</script>


