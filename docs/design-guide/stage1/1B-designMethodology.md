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
<center>*Final robot assembly.*</center>

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
To begin, you will be creating a layout sketch of the drivetrain. This will dictate the size and position of the drive tubes. For your swerve drivebase, you will make it 26"x26".

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
      <figcaption>4. Create the top layout sketch by using the bottom mate connector on the vertical line of the side layout. Utilizing auto-generated mate connectors for sketch planes is a very useful tool to have.</figcaption>
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
      <figcaption>6. Next, we need to make the cutouts on the drivetube for the swerve modules. Start by drawing two lines, each offset by 4.25" from the edge. This is the required offset for MK4i modules. Other modules will differ.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout5.gif" style="width:100%">
      <figcaption>6. To apply the cutout for all four tubes, we use the <code>Circular Pattern</code> sketch tool to copy the lines to all four corners. For a  <code>Circular Pattern</code> we first define the number of instances and then the axis of rotation.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>6. Finally, name your sketches and organize them into a folder in the file tree. Your sketches should all be fully defined.</figcaption>
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







The top layout sketch should be made at the bottom of where we want the tubes to be instead of at the ground. Instead of using a plane, we can create the sketch directly on a point on the side layout sketch, so the bottom of the tubes is driven by the side layout sketch without an extra plane.

Open the sketch dialogue to create a new sketch and click the circle symbol (select mate connector) next to the "sketch plane" selection box. Select a point on the bottom of the tube in the side layout sketch and a sketch will be created there. 

<center><img src="\img\design-guide\stage1b\mate_connector_sketch.webp"></center>

!!! Tip
    If the sketch is facing the wrong way, try selecting the point again and make sure the colored axis are pointing the right direction (blue up).

Press the “Top” button on the view cube to get a top view (or press ```n``` to rotate normal to the sketch plane). The next steps include sketching out the “top” of the drivetrain tubes. 

Start a center point rectangle on the origin, hover over the point at the top of the dotted line (making a horizontal constraint between it and the top of the rectangle), then moving the side out and clicking to finish the rectangle. 

<center><img src="\img\design-guide\stage1b\horiConstraint.webp"></center>

If you remember previously, that point was the edge of your drivetrain which you in the side layout sketch. See how the left side of the rectangle is already 26 inches? We want to make this a square, so let’s use the equal constraint (e key) between the top of the square and the left side of the square. This should make both sides equal to each other, and the whole sketch should be black.

<center><img src="\img\design-guide\stage1b\definedSketch.webp"></center>

Use the offset tool and offset the square inwards by 1 inch; this will define the side of your drive rails.

<center><img src="\img\design-guide\stage1b\offset.webp"></center>

Taking a look at the swerve drivetrain again, we can see there’s a cutout in each of the corners. We should define this in our sketch. From the edge of the corner, the gap is 4.25 inches long. 

<center><img src="\img\design-guide\stage1b\1a-Swerve 11.webp"></center>

Draw two lines, one horizontally constrained and one vertically constrained, and dimension them 4.25in away from the corner as shown.

<center><img src="\img\design-guide\stage1b\cornerCutout.webp"></center>

To apply this to all corners, circular pattern the two lines you created, changing the number of instances to four. It should look like this:

<center><img src="\img\design-guide\stage1b\1a-Swerve 13.webp"></center>

Confirming the sketch should show the chassis as shown, with some blue lines. Why is that? 

If you click on one of the points on the blue unconstrained lines, you can drag them around. This also reveals the center of rotation of the circular pattern (the blue dot).

<center><img src="\img\design-guide\stage1b\1a-Swerve 15.webp"></center>

Constrain the center of rotation to the origin by dragging it to the origin. Your sketch should look like this:

<center><img src="\img\design-guide\stage1b\1a-Swerve 16.webp"></center>

If we take the top view of a drivetrain, you can see how it looks similar. Removing the modules also shows the gaps we modeled.

<center><img align="center" src="\img\design-guide\stage1b\1a-Swerve 17.webp" width="45%"> <img align="center" src="\img\design-guide\stage1b\1a-Swerve 18.webp" width="45%"></center>

Let’s now sketch out the middle cross beam. We’ll make this out of 2x2 aluminum since 2x2 is stronger than 2x1. Let’s make it 2 inches wide, and 2 inches away from the center (origin).

<center><img src="\img\design-guide\stage1b\1a-Swerve 19.webp"></center>

Rename the sketch to “Drivetrain Top” and confirm it with the green checkmark.

Now, lets create the tubes. Click the extrude individual featurescript. 

!!! Tip
    The "extrude individual" featurescript allows us to make multiple parts, one per sketch region, with a single extrude feature.

<center><img src="\img\design-guide\stage1b\1a-Swerve 20.webp"></center>

Click the top faces of the sketch and extrude them 2 inches up to make the tubes.

<center><img src="\img\design-guide\stage1b\1a-Swerve 21.webp"></center>

Now, use the "tube converter" featurescript and click on the four outer tubes.

!!! Tip
    The "tube converter" featurescript converts box tube-shaped extrudes into COTS box tube with a hole pattern. 

<center><img src="\img\design-guide\stage1b\1a-Swerve 22.webp"></center>

Set the thickness to 0.125in, as 0.125in thickness is “thick wall” tubing. 0.125in wall thickness tubes are strong and allow for a strong and rigid frame that is resistant to collisions. Set the 2 inch face style to “1 inch between holes”, and click the checkbox for center row. Confirm the tube converter feature. 

!!! Note
    As mentioned earlier, you can find this type of box tubing from various COTS vendors, which sell the pre-punched tubing for your convenience.

<details>
<summary>WCP Box Tubes</summary>
<center><img src="\img\design-guide\stage1b\1a-Swerve 23.webp"><figcaption>(Source: West Coast Products)</figcaption></center>
</details>



Let’s do another tube converter for the 2x2 tube, but change the thickness to 1/16in. The reason for this is because 1/16in 2x2 is plenty strong, and allows for weight savings down the line.

Once you are done, change the appearance of all of your tubes to a color of your choosing. I’ll be using dark gray. You can do this by going to the parts menu and clicking all 5 parts, then right clicking and selecting “edit appearance for 5 parts”.

<center><img src="\img\design-guide\stage1b\1a-Swerve 24.webp"></center>

<center><img src="\img\design-guide\stage1b\Tubes.webp"></center>

## Assembly

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