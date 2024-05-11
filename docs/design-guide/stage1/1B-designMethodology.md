<style>
.right{
    float:right;
}
.center{
    text-align:center;
}
.left{
    float:left;
}
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

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
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

# 1B: Swerve Drivebase Project

<span class="left">[< 1A: Sketching & Part Design](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Gearbox Projects >](1C-gearboxes.md)</span>
<br>

## Project Overview

In Stage 1B, you'll dive right into top-down robot design with master sketches. In this project, you will be designing a swerve drivebase using COTS swerve modules. You will be introduced to a top-down design workflow that will be applied to all future projects. Even if you've already CADed a drivetrain the past, this guide serves as an excellent introduction to the top-down master sketch design methodology.

To begin, you'll be modeling a swerve drivebase. Then, you'll create a top level robot assembly and insert and mate a pre modeled mechanism.

<center><img src="\img\design-guide\stage1b\SwerveBase\fullassy.webp" style="width:100%"></center>
<center>*Final robot assembly. (Update pic) *</center>

## Master Sketch Methodology
When designing a model in CAD, there are two high level strategies that can be employed: top-down and bottom-up. Top-down design employs high level, low detail sketches to dictate the design, and then refining details and components within that framework. Conversely, bottom-up design involves creating individual components or parts separately and then assembling them to form the final product. 

Top-down design offers a holistic approach, allowing for better system integration, consistency, and is more parametric. Bottom-up design offers flexibility and independence in designing individual parts. In FRC robot design, top-down approach is favored as system integration is often the most challenging aspect. Top-down ensures that the robot architecture dictates part design.

<!-- TODO: add text about creating a master layout part studio and deriving it into each sub system -->

## Swerve Drivebase
A drivebase is the mobile platform on which all our other mechanisms are designed around and attached to. With the advent of COTS swerve, designing a swerve drivebase has been made significantly easier and has become the most commonly used competitive drivetrain in FRC. 

A swerve drivebase is composed of four *swerve modules*. Each module has 2 motors: 1 for spinning the wheel and one for steering it. This enables the robot to translate in any direction independent of the rotation of the robot. There are many other COTS options available, each with their own advantages and tradeoffs. In this project, we'll be using [SDS MK4i modules](https://www.swervedrivespecialties.com/products/mk4i-swerve-module). You can learn more about drivetrains on the [Design Fundamentals](/design-fundamentals/mechanisms/drivebase/) page.

<center><img src="\img\design-guide\stage1b\SwerveBase\fullassy.webp" style="width:100%"></center>
<center>*Stage 1B swerve drivebase project.*</center>

As was introduced in Stage 1A, robot structures are typically constructed out of aluminum box tubing. The drivebase is no exception to this. Most teams will opt to design their box tubing with a standard 0.5" spacing pattern of 0.196" diameter holes. This enables modularity and allows for easy integration of many COTS components like gussets.

Box tubing extrusions can be purchased at most metal suppliers, but many FRC vendors including [WCP](https://wcproducts.com/collections/systems-structure/products/punched-tubing), [TTB](https://www.thethriftybot.com/products/thrifty-box-extrusion), [REV](https://www.revrobotics.com/MAXTube/) sell box tubing with pre-cut hole patterns which can significantly reduce manufacturing time and equipment requirements.

### Drivetrain Master Sketches
To begin, you will be creating a layout sketch of the drivetrain. This will dictate the size and position of the drive tubes. The layout will be drawn from the side and top view of the drivetrain. For your swerve drivebase, you will make it 26"x26".

Start by creating a Master Sketch part studio. Then, use the `Origin Cube` Featurescript to create an origin cube. You should start every part studio with an origin cube to set a reference for the origin of the robot. The origin of the robot is typically defined as the center of the drivebase on ground level. You can learn more about origins and the origin cube in [Assembly Best Practices](/best-practices/assembly-setup#origin-cube-method).


<center>**Drivetrain Layout Sketch Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>0. The final layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/originCube.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtSideLayout1.webp" style="width:100%">
      <figcaption>2. Draw the side profile of the drivetrain on the Right Plane. We place the tube 1.75" from the ground, which is the offset from the ground to the bottom of the tube for the MK4i modules.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtSideLayout2.webp" style="width:100%">
      <figcaption>3. Draw the wheel clearance box, which represents the area that the wheel takes up. For the MK4i modules, the box is 4.625" wide. The side layout of the drivebase is now finished.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout1.gif" style="width:100%">
      <figcaption>4. Create the top layout sketch by using the bottom mate connector on the vertical line of the side layout. Utilizing auto-generated mate connectors for sketch planes is a very useful tool to have. Press the “Top” button on the view cube to get a top view.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout2.gif" style="width:100%">
      <figcaption>5. Sketch the top outline of the drive base. Make the rectangle a square and set the side length equal to the length of the side layout tube. This ensures that the size of the top layout always matches the side layout, which makes the design parametric. Notice that the sketch is fully defined despite having no sketch dimensions.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout3.webp" style="width:100%">
      <figcaption>6. To sketch the tubes, draw a square 1" smaller than the previous square. This will represent the four 2"x1" tubes that make up the outer frame. Then, draw the top profile of the 2"x2" tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout4.webp" style="width:100%">
      <figcaption>7. Next, we need to make the cutouts on the drivetube for the swerve modules. Start by drawing two lines, each offset by 4.25" from the edge. This is the required offset for MK4i modules. Other modules will differ.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout5.gif" style="width:100%">
      <figcaption>8. To apply the cutout for all four tubes, we use the <code>Circular Pattern</code> sketch tool to copy the lines to all four corners. For a  <code>Circular Pattern</code> we first define the number of instances and then the axis of rotation.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>9. Finally, name your sketches and organize them into folders in the feature tree. Your sketches should all be fully defined.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

### Deriving Layout Sketches and Part Modeling

Now that you have created the layout sketch, you can begin modeling the individual parts. The critical dimensions of the parts, such as the length of the tubes, will be driven by the layout sketch. This way, the tubes will automatically update with any changes in the size of the drivebase in the layout sketch.

Start by creating a new Drivetrain folder tab. Then, create a new part studio called drivetrain.

<center>**Drivetrain Part Modeling**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts0.webp" style="width:100%">
      <figcaption>0. The final part studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts1.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube. Then, use the <code>Derived</code> tool to insert the layout sketches you previously drew from the Master Sketch part studio. This feature will automatically update if changes are made to the layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> and <code>Tube Converter</code> Featurescripts to model the tubes. The 2"x1" tubes should be 1/8" wall for strength, while the 2"x2" tube can be 1/16" wall.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts3.webp" style="width:100%">
      <figcaption>3. Start with one corner of the bellypan. The corner is cut out to create room for the swerve module. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts4.webp" style="width:100%">
      <figcaption>4. Use the <code>Fillet</code> sketch tool to add a 1" radius sketch fillet on the two internal corners of the cutout. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts5.gif" style="width:100%">
      <figcaption>5. Next, use the <code>Circular Pattern </code> sketch tool to pattern the other three corners. Extrude the bellypan to be 1/8" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts6.webp" style="width:100%">
      <figcaption>6. Use the <code> Fillet All Edges</code> Featurescript to add a 0.25" radius fillet to the remaining edges on the bellypan by selecting the bottom face of the bellypan.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts7.webp" style="width:100%">
      <figcaption>7. Next, add all of the holes for the bellypan. You can use the <code>Linear Pattern</code> sketch tool to easily draw the holes. For the 2"x1" edges, you can use the <code>Circular Pattern</code> sketch tool to pattern the holes onto all four edges. Extrude the holes through the bellypan. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts8.webp" style="width:100%">
      <figcaption>8. Add the gusset for the crosstube with the <code>Gusset</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts0.webp" style="width:100%">
      <figcaption>9. Finally, name your sketches and organize them into a folder in the feature tree. Additionally, set the material of the bellypan to Aluminum 6061 and name your parts.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,1)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,1)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>


### Assembly

Now that we have the frame tubes, we need to insert them into the "assembly". You use part studios to design parts in reference to each other, and assemblies to define the position and motion of those parts and assemble the final product. Certain practices in the part studio can make assembly easier and faster; these are some of the best practices that are used in the guided projects and in the [best practices](../../best-practices/index.md) section of the website.

### Origin Mate Connector
Something to note is that both assemblies and part studios have an origin. We will need to make sure that our parts are in the same place in both the origin and part studio. We can do this through an origin mate connector.

!!! Tip
    Make sure to show the origin in the feature list if it was hidden by hovering over the origin in the list and clicking the eye symbol.

Select the mate connector button on the top. 

<center><img src="\img\design-guide\stage1b\Mate-Connector.webp"></center>

Select the origin entity as the origin, then the owner entity as the 2x2 tube. The 2x2 tube will now have an mate connector at the origin.

<details>
<summary>Video Tutorial</summary>
  <center><iframe width="880" height="550" src="https://www.youtube.com/embed/4jTYh0Rn5cU" frameborder="0" allowfullscreen></iframe></center>
</details>


### Assembling

Now that you have finished your part studio, you can follow this video tutorial to do the rest of the assembly. Assemblies require a bit more explaining, which is why it's in video as opposed to text. 

<center><iframe width="880" height="550" src="https://www.youtube.com/embed/9cMRIJJGGeE" frameborder="0" allowfullscreen></iframe></center>

Notice how when inserting parts into the assembly, the process is:

1. Add a mate connector to one of your rigid parts on the origin in your part studio
2. Insert the whole part studio with the green checkbox so the origin is in the same place
3. Use the "group" tool on all parts that don't move
4. Fasten the mate connector to the origin
5. Duplicate and fasten any duplicate parts

This is a fast and parametric way of putting together an assembly, as opposed to using mates to constrain all the parts that were already in the correct place.

!!! Tip
    As you add more parts in the part studio, you can insert them individually into the assembly with the green checkmark, double click on the initial group, and add the part to the group to avoid mating it. This means that new part will always stay in the same place relative to where it was designed in the part studio.

Make sure you sort the instances in your assembly into folders (i.e. tubes, swerve modules).

More details about best practices for Onshape assemblies are included in the [best practices](../../best-practices/index.md) category, on [this page](../../best-practices/assembly-setup.md).

## Conclusion
You've completed a basic swerve drivebase, going over many concepts in the process. The CAD concepts include sketching parametrically, creating a sketch on a mate connector, using featurescripts, and the fast assembly workflow. The FRC concepts include box tube and swerve modules.

The most important concept is how you can start with a layout sketch or two and build the entire rest of the part studio on top of those, meaning the part studio and assembly could change if you only changed the dimensions in the side layout sketch. This is what a top-down workflow is, and it allows you to create an outline first and slowly go into more detail, referencing the outline as you go.

<center><img src="\img\design-guide\stage1b\Assembly_1.webp"></center>

Try changing the dimensions in the side layout sketch and seeing what happens to the part studio and assembly.

Next, you'll learn how to sketch and assemble power transmission components in a few gearboxes.

<br>
<center>1B: Drivebase</center> 
<span class="left">[< 1A: Sketching & Part Design](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Gearbox Projects >](1C-gearboxes.md)</span>
<br>
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