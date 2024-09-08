<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}
#slide1 {display:block}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 250px;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 3px 3px 3px 3px;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.6);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 0.25s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
</style>

# 1B: Power Transmissions

## Chain and Sprocket Basics

Roller chain and sprocket drives are very similar to belt and pulley transmissions. They consist of two main components: a chain, which is a series of interconnected links, and sprockets, which are toothed wheels that mesh with the chain. As the sprockets rotate, they engage with the chain, causing it to move and transmit power from one shaft to another. Bikes are an everyday object that use chain to transmit power. Chains excel at transmitting high force over long distances.

<center><img src="\img\learning-course\stage1b\chain\chainAnimation.gif" style="width:40%"></center>
<center>*A simple animation of chain and sprocket. Notice that the sprockets will spin in the same direction.*</center>

In order to change the torque and speed from the input to the output, different sized sprockets must be used. The mechanical advantage for chain transmissions, similar to gears and pulleys, is based on the ratio between the number of teeth of the output sprocket to the number of teeth of the input sprocket. Similar to pulleys, the sprockets will spin in the same direction.

### Types of Chain

The two commonly used sizes of roller chain in FRC is #25 and #35 chain, with 0.25" and 0.375" pitch respectively. For chain, the **pitch** is the length of each link. The *pitch length* of the chain is then the pitch (0.25" or 0.375") multiplied by the number of links. Try to use an even number of links to avoid the use of a "half-link" which is weaker than a full-link. This means your chain pitch length should be a multiple of 0.5".
<!-- 
To calculate the pitch diameter, the following equation can be used:

<center>**`PD = Pitch / sin [180°/# of teeth]`**</center> -->

Additionally, the **chain clearance diameter** describes the diameter of the sprocket with the chain wrapped around it. The following equation can be used:

<center>**`Clearance Diameter = PD + Pitch`**</center>

Below is an illustration of the pitch, pitch diameter, outside diameter, and chain clearance diameter of a sprocket.

<center><img src="\img\learning-course\stage1b\chain\chainDiagram.webp" style="width:70%"></center>
<center>*Illustration of chain sprocket diameter measures. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/sprockets-and-chain">WCP</a>)*</center>

In FRC, #25 chain is most commonly used as it is strong yet relatively lightweight. #35 is sometimes used on very high torque transmissions, but it is heavy and bulky. 

### Modeling Chain Transmissions

The modeling workflow for chain is the exact same as for belts in the previous page. You will need the pitch diameter of the two sprockets and a correct center-to-center distance.

Utilize the [`Origin Cube` Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/2b321cb91b74224b9c14b433 "Origin Cube Featurescript Onshape Document"){:target="_blank"} function to dimension the pitch diameters of two sprockets on points you want connected with a chain. 

* `#SprocketPD_25(n)`: Calculates the pitch diameter of a #25 pitch sprocket with `n` teeth.
    * Ex: `#SprocketPD_25(16)` returns the pitch diameter of an 16T #25 pitch sprocket.

Generate a 3D model of the chain with the same [`Belt & Chain Gen` Featurescript](https://cad.onshape.com/documents/53c0b14cad92676c14e04e97/w/1271c254ccb0a79563210195/e/7394c4a86d8d6c35c9a12041 "Belt & Chain Gen Featurescript Onshape Document"){:target="_blank"} that you used for belts, check the chain link count that it generates, then  go back to the sketch and dimension your center-to-center distance using that chain link count to get the correct center-to-center distance. Use the following Origin Cube function: 

* `#ChainCTC_25(n1, n2, n3)`: Calculates the c-c distance of a `n1` link #25 pitch chain connecting sprocket with tooth count `n2` and sprocket with tooth count `n3`.
    * Ex: `#ChainCTC_25(80,16,48)` returns the center distance for an 80 link #25 pitch chain connecting a 16T sprocket to a 48T sprocket.


### Chain Tensioners

One difficulty when designing with chain is that it will physically stretch as it is used. This means the distance between each link will slightly increase, making the overall chain longer in a non-insignificant way. Loose chain can be difficult to fix if the chain transmission is not designed with chain tensioning in mind. Although you will not be learning about chain tensioning methods quite yet, you should keep this idea in the back of your mind. 

In Stage 2, different chain tensioning methods are introduced in the context of different types of robot mechanisms. The [Design Handbook page](/design-handbook/ "Design Handbook Page"){:target="_blank"} also dives deeper into this topic.

!!! Example "Example of Chain Tensioning"
    <center><img src="\img\learning-course\stage1b\chain\turnbuckle.webp" style="width:60%"></center>
    <figcaption>A "turnbuckle" chain tensioner. The turnbuckle acts as a variable-length link in the chain that can be adjusted to keep the chain tight. (Photo Credit: FRC 1538)</figcaption>

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