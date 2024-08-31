<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

.mySlides {
    display:none;
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

# 2A: Full Detail Drivebase

Welcome to Stage 2! This section covers FRC mechanism design, emphasizing CAD skills, best practices, and key engineering concepts. Each project guide explains design decisions and criteria, promoting independent CAD work with less step-by-step instruction.

## Introduction

The first project in Stage 2 will be detailing the drivetrain you began modeling in Stage 1B. So far, you’ve only modeled the frame and bare bellypan. To finish the drivetrain, you should add the following details.

1. Battery Mounting: Every robot needs a battery, and while the location may vary based on the other mechanisms present in your robot, it should always be placed as low as possible to make the robot more stable.

2. Electronics Mounting: Adequate space must be allocated on the robot for ease of wiring. Typically, the robot’s electronics are mounted on the bellypan.

3. Bellypan Pocketing: This step is optional. Some teams will prefer to add cutouts in their bellypan to remove weight and make wiring easier. However, pocketing the bellypan may significantly increase machining time.

4. Bumpers: While bumper rules can vary from year to year, they are almost always required to protect your robot and other robots from collisions. Making your bumpers easy to attach and remove is also a very nice quality of life improvement for when you’re at competition.

While the exact implementation for each of these details will vary based on the rest of your robot and from team to team, an example reference for Stage 2A is provided.

<center>[2A Drivetrain Reference](https://cad.onshape.com/documents/86303b75f6f9790b01106a3b/w/6d34296fadf33319c731fa02/e/245e154bf8681866056b6985){:target="_blank" .md-button .md-button--primary } </center>

<center><img src="/img/learning-course/stage2-drivebase/2a-FDdt.webp" style="width:80%"></center>

<center><figcaption>Example of a fully detailed Stage 2A drivetrain.</figcaption></center>

## Battery Mounting
Ensuring that your robot’s battery does not fall out of your robot is critical for successful robot operation. While it may seem obvious, even veteran teams [sometimes](https://youtu.be/bhjb3Vw8YHg?si=Bxm7oD5VkmYW7oj0&t=105 "3647 Battery Falling Out"){:target="_blank"} get [this](https://youtu.be/Dr_rnN2bjno?si=roWawTsyWt5W3RdA&t=86 "3647 Battery Falling Out...Again"){:target="_blank"} wrong. 
Successful battery mounting can be broken down into two components: good battery placement and a robust battery holder.

### Battery Placement
Batteries are heavy: the FRC robot battery weighs a whopping 13 lbs. Since the battery is so heavy, you need to place it as low as possible to keep your robot’s center of gravity low to prevent tipping over. Most teams will typically use the bellypan to support their battery as this is the lowest location on the robot. 

### Battery Holder

A strong strap is needed to secure the battery to its mount, preventing it from dislodging during hard collisions. A good option is to use a 1” or 2” wide buckle strap, which can be purchased and cut to size from most stores. FRC vendors like WCP also sell [battery mounting accessories](https://wcproducts.com/products/batteries-accessories "WCP Battery Accessories Product Page"){:target="_blank"} including battery holders and straps.

!!! Example
    <center><img src="/img/learning-course/stage2-drivebase/batt/battStrap.webp" style="width:70%"></center>
    <center><figcaption>Securely strapped battery in a robot. (Photo Credit: FRC 1538)</figcaption></center>

Below, we've provided one option for mounting the battery. In this design, the battery is placed horizontally on the bellypan. It is secured with a 2" wide strap that wraps around the battery and bellypan to secure it. 

<center>**Sample Battery Holder Modeling Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/batt/batt1s0.webp" style="width:100%">
        <figcaption>0. Finished battery holder w/ mounting holes, strap cutout in bellypan, and strap.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/batt/batt1s1.webp" style="width:100%">
        <figcaption>1. Layout of battery and battery mount plate. To fit the battery with 1/16” radius fillets on the inner corners, the cutout should be around 6.705” x 7.225”.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/batt/batt1s2.webp" style="width:100%">
        <figcaption>2. 1/8" thick aluminum is a good option for this plate. Also add a 3/8" diameter spacers to connect to the bellypan.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/batt/batt1s3.webp" style="width:100%">
        <figcaption>3. Add the mounting holes and cut out for the battery strap on the bellypan. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/batt/batt1s4.webp" style="width:100%">
        <figcaption>4. Optionally model the battery strap.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/batt/batt1s5.webp" style="width:100%">
        <figcaption>5. Optionally pocket the battery holder. 0.2" wide ribs are recommended. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/batt/batt1s0.webp" style="width:100%">
        <figcaption>6. Insert the battery holder, spacer, and battery into the assembly. Don't forget to organize your feature tree, name your parts, assign part materials, and organize your assembly file tree.</figcaption>
    </figure>
</div>

<!-- Next and previous buttons -->
<button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
<button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
<!-- The dots/circles -->
<div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
</div>
</div>



## Electronics Mounting

To make wiring the robot and later inspecting the wiring easier, enough space should be left around each electrical component. You should work with your electrical teammates to determine the best location for the various control system parts. Teams typically try to mount their electronics on the bellypan, permitted there is space. 

!!! Example
    <center><img src="\img\learning-course\stage2-drivebase\elec\elecPic.png" style="width:80%"></center>
    <center><figcaption>Example layout of various different electronic components on a bellypan.</figcaption></center>

A list of typical electrical components found on FRC robots is provided below, as well as a recommended mounting location. Again, mounting locations are highly dependent on the rest of your robot, make sure to always coordinate with your electrical team to decide what is best.


??? note "Electrical Components"
    | **Component** | **Function** | **Suggested Location** | **Image** |
    |---|---|---|---|
    | REV Power Distribution Hub (PDH) or  CTRE Power Distribution Panel (PDP) | Distributes power to all other components | Bellypan | ![PDH](\img\learning-course\stage2-drivebase\elecComponents\pdh.webp) |
    | Main Breaker | Is used to turn on/off the robot and protect electronics from events with extremely high current drawn | Somewhere easily accessible and close to the PDH and Battery | ![Main Breaker](\img\learning-course\stage2-drivebase\elecComponents\mbreak.webp) |
    | RoboRIO | Central controller for all robot operations | Bellypan | ![RoboRIO](\img\learning-course\stage2-drivebase\elecComponents\rio.webp) |
    | Integrated motor controller (eg: Falcon 500, Kraken X60) | Powers and controls the  integrated motor | No electrical mounting required | ![Integrated motor controller](\img\learning-course\stage2-drivebase\elecComponents\kx60.webp) |
    | Discrete motor controller  (eg: Spark Max, Talon SRX) | Required to power and control some motors  (eg: NEO, CIM) | Near the controlled motor  or on the bellypan | ![Discrete motor controller](\img\learning-course\stage2-drivebase\elecComponents\smax.webp) |
    | Robot Radio | Allows the robot to establish wireless connections to the field or driver station | Follow Vivid Hosting's [radio mounting guidelines](https://frc-radio.vivid-hosting.net/getting-started/usage/mounting-your-radio "Vivid Hosting Radio Mounting Guidelines"){:target="_blank"}. | ![Robot Radio](\img\learning-course\stage2-drivebase\elecComponents\vh109.webp) |
    | Robot Signal Light (RSL) | Indicates whether the robot is on and enabled/disabled | Somewhere easily visible | ![Robot Signal Light](\img\learning-course\stage2-drivebase\elecComponents\rsl.webp) |
    | Inertial Measurement Unit (IMU) | Used to determine robot heading and acceleration | Close to the center is best practice (on Bellypan or VHB tape to attach to RoboRIO) | ![Inertial Measurement Unit](\img\learning-course\stage2-drivebase\elecComponents\imu.webp) |
    | Voltage Regulator Module | Can be used for custom circuits | Bellypan | ![Voltage Regulator Module](\img\learning-course\stage2-drivebase\elecComponents\vrm.webp) |
    | Pneumatics Hub | Controls pneumatic components | Bellypan | ![Pneumatics Hub](\img\learning-course\stage2-drivebase\elecComponents\pcm.webp) |


One option for mounting the Power Distribution Hub (PDH), main breaker, and RoboRIO onto the bellypan is provided in the below example. The [`Electronic Mounting` Featurescript](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/83cfa4ae1a46ea05581445c9 "Electronic Mounting Featurescript Onshape Document"){:target="_blank"} can be very useful for generating the mounting holes for electronics. If you cannot accurately manufacture mounting holes for electronics, VHB tape (which comes in the Kit of Parts) can be a good option for robustly securing your electronics.

<center>**Sample Electronics Mounting Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/elec/elec1s0.webp" style="width:100%">
        <figcaption>0. Finished mounted electronics.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/elec/elec1s1.webp" style="width:100%">
        <figcaption>1. Draw box outline for PDH and RoboRIO. Also add the outline and holes for the main breaker.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/elec/elec1s2.webp" style="width:100%">
        <figcaption>2. Use the <code>Electronic Mounting</code> Featurescript to add the PDH and RoboRIO mounting holes. Optionally override the hole size for the PDH to be 5/32” diameter, which will allow the mounting bolt to screw directly into the bellypan.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/elec/elec1s0.webp" style="width:100%">
        <figcaption>3. Insert the electronics from the MKCad parts library and fasten them. The Pigeon IMU can be fastened to the RoboRIO.</figcaption>
    </figure>
</div>


<!-- Next and previous buttons -->
<button class="prev" onclick="plusSlides(-1,1)" style="background-color: #000; color: #fff;">&#10094;</button>
<button class="next" onclick="plusSlides(1,1)" style="background-color: #000; color: #fff;">&#10095;</button>
<!-- The dots/circles -->
<div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
</div>
</div>

It is recommended to use the Simplified electronics models to improve assembly performance. You can read more about simplified models on the [Assembly Best Practices Page](/best-practices/assembly-setup/ "Assembly Best Practices Page"){:target="_blank"}. Simplified swerve module models can also be used to reduce lag. 

Every robot is also required to have a Robot Signal Light (RSL). An easy location to mount the RSL is on the side of the drive frame. Typically, only one RSL is required and needs to be “easily visible while standing 3 ft. (~ 100 cm) away from at least one side of the ROBOT”. Be sure to check the latest game manual rules for the most up to date RSL mounting rules.

<center><img src="\img\learning-course\stage2-drivebase\elec\RSL.webp" style="width:80%"></center>
<center><figcaption>RSL mount constructed out of 1/8" thick polycarbonate plate. The mounting hole for the RSL is 1” in diameter. The RSL model can be found in the MKCad App.</figcaption></center>

Each robot is also required to have a radio. The radio should be mounted on the robot following Vivid Hosting's [radio mounting guidelines](https://frc-radio.vivid-hosting.net/getting-started/usage/mounting-your-radio "Vivid Hosting Radio Mounting Guidelines"){:target="_blank"}.

## Bellypan Pocketing

Some teams may choose to pocket their bellypan to reduce weight and make wiring easier. A pocketed bellypan can save around 3-4 lbs. However, this will add significant machining time if you are manufacturing the bellypan yourself or increase cost if you are purchasing the bellypan from a fabrication service (eg: [Fabworks](https://fabworks.com/ "Fabworks Sheet Metal Services"){:target="_blank"}). You should carefully consider the tradeoffs with your team.

If you choose to pocket your bellypan, you can utilize the `Vent`, `Lighten`, or `Part Lighten` [Featurescripts](../../../resources/featurescripts/ "Featurescripts Page"){:target="_blank"} to pocket the bellypan. While the workflow may slightly vary between each Featurescript, the general idea is the same. A diamond pattern is recommended for strength and ease of modeling.

<center>**Sample Bellypan Pocketing Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s0.webp" style="width:100%">
        <figcaption>0. Pocketed bellypan. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s1.webp" style="width:100%">
        <figcaption>1. Draw two perpendicular lines that are offset 45 degrees from vertical. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s2.webp" style="width:100%">
        <figcaption>2. Linear pattern the lines until they completely cover the bellypan. These will be the ribs for the bellypan.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s3.webp" style="width:100%">
        <figcaption>3. Offset the outline of the bellypan 0.5”.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s4.webp" style="width:100%">
        <figcaption>4.  Connect any islands that might result from mounting holes being too far from a rib. One way to fix this is to add a slot connecting the island to a rib.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s0.webp" style="width:100%">
        <figcaption>5. Use a pocketing Featurescript to pocket the bellypan. Recommended settings are 0.15” wide ribs and 3/16” tool radius.</figcaption>
    </figure>
</div>

<!-- Next and previous buttons -->
<button class="prev" onclick="plusSlides(-1,2)" style="background-color: #000; color: #fff;">&#10094;</button>
<button class="next" onclick="plusSlides(1,2)" style="background-color: #000; color: #fff;">&#10095;</button>
<!-- The dots/circles -->
<div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
</div>
</div>

## Bumpers
Bumper construction is described in each year’s FRC game manual. Typically, it is required to be two 2.5” diameter pool noodles backed by a 5” tall 3/4" thick plywood sheet. Refer to the latest game manual for the most up to date bumper rules. Bumper cutout and ground clearance rules will vary from year to year.

### Bumper Model
To begin, you'll need to model the bumpers. It is recommended to place the bumpers in a new part studio and assembly to keep your feature and assembly trees organized. The minimum level of detail should be a block model of the bumper. Some teams may opt to model the bumper wood, bumper wood holes, angle brackets for the bumper wood, and other details to assist with manufacturing. You should communicate with the rest of your team members to determine the level of detail that is required. 

<center>**Sample Bumper Modeling Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s0.webp" style="width:100%">
        <figcaption>0. Finished bumpers assembly inserted into drivetrain assembly. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s1.webp" style="width:100%">
        <figcaption>1. Create a new sketch in the Master Sketch part studio with the bumper profile. A 3/4" ground clearance and 1/4" gap between the bumper and frame is recommended.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s2.webp" style="width:100%">
        <figcaption>2. Create a new part studio in the drivetrain folder for the bumpers. Insert the Origin Cube and derive the drivetrain and bumper sketches from the Master Sketch.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s3.webp" style="width:100%">
        <figcaption>3. Sweep the bumper profile along the edges of the drivetrain top layout sketch to create the block model of the bumpers.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s4.webp" style="width:100%">
        <figcaption>4. Optionally add a fillet on the corners. Size it according to how your team wraps the bumper pool noodles.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s5.webp" style="width:100%">
        <figcaption>5. Optionally model the wood for the bumpers. This can be useful for manufacturing purposes.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s6.webp" style="width:100%">
        <figcaption>6. Create a bumper assembly in the drivetrain folder and insert all the components. Don’t forget to group all the components and mate the origin cube mate connector to the origin.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s0.webp" style="width:100%">
        <figcaption>7. Insert the bumper assembly into the drivetrain assembly.</figcaption>
    </figure>
</div>

<!-- Next and previous buttons -->
<button class="prev" onclick="plusSlides(-1,3)" style="background-color: #000; color: #fff;">&#10094;</button>
<button class="next" onclick="plusSlides(1,3)" style="background-color: #000; color: #fff;">&#10095;</button>
<!-- The dots/circles -->
    <div class="dotsContainer" style="text-align:center">
        <!-- Dots will be generated here -->
    </div>
</div>

Keeping the bumper part studio and assembly separate from the drivetrain keeps the drivetrain feature tree cleaner and allows for easier hiding/showing of the bumpers in the top level assembly since you can show and hide the entire bumper assembly at once.

### Bumper Mounting

Next, you'll need to model your desired bumper mounts in the drivetrain part studio. 

Similar to battery mounting, good bumper mounting is often overlooked. While a robust bumper mounting system won’t win you any matches, a poor bumper mounting system can certainly lose you a match. Poor bumper mounting can lead to bumper damage, long bumper swap time, or even lead to your [bumpers falling off](https://youtu.be/pBUKxWKGV-Q?si=hmJtt9N6C7vGLFpL&t=42 "Bumpers Falling Off"){:target="_blank"}.

In the provided example, the threaded stud bumper mounting system is implemented. 
<!-- 
You can learn more about bumpers and different bumper mounting options in the [Design Handbook](/design-handbook/) pages.  -->

<center><img src="\img\learning-course\stage2-drivebase\bumpers\studMount.png" style="width:60%"></center>
<center><figcaption>Section view of the threaded stud bumper mount system. The threaded stud is attached to the bumper wood and the nut holds the stud tight.</figcaption></center>

<center>**Sample Bumper Mount Modeling Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s0.webp" style="width:100%">
        <figcaption>0. Finished bumper mounts. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s1.webp" style="width:100%">
        <figcaption>1. Model the bumper mount. This part should be 3/16” thick aluminum. The threaded stud falls into the slot.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s2.webp" style="width:100%">
        <figcaption>2. Add the pocket for the nut that screws onto the threaded stud. This nut keeps the bumpers tight with the frame. The pocket secures the nut and prevents the bumper from lifting up.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s3.webp" style="width:100%">
        <figcaption>3. Optionally pocket the mount. 0.15" wide ribs and 1/8" tool radius are recommended. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s4.webp" style="width:100%">
        <figcaption>4. Insert the mount and add it to the <code>Group</code>. Copy three more mounts and mate them onto the drivetrain assembly. If your team runs multi piece bumpers (eg: two C shaped bumpers) you may need to add more mounts to secure the bumpers.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s0.webp" style="width:100%">
        <figcaption>5. Finished bumper mounts in drivetrain assembly.</figcaption>
    </figure>
</div>

<!-- Next and previous buttons -->
<button class="prev" onclick="plusSlides(-1,4)" style="background-color: #000; color: #fff;">&#10094;</button>
<button class="next" onclick="plusSlides(1,4)" style="background-color: #000; color: #fff;">&#10095;</button>
<!-- The dots/circles -->
    <div class="dotsContainer" style="text-align:center">
        <!-- Dots will be generated here -->
    </div>
</div>


## Summary

Congratulations on completing Stage 2A! With the Stage 2A tasks completed, your drivetrain model is well on its way to being fully functional. 

Here is a quick summary of what you have achieved in 2A:

* Learned about battery mounting and the importance of a secure battery holder
* Learned about core FRC electronics and how and where to mount them
* Learned how to use the `Electronic Mounting` Featurescript
* Optionally learned how to pocket a bellypan
* Learned about bumpers, how to model them, and the importance of having a secure mounting system
* Practiced more complex sketching and layout

As you progress, the projects will become more and more open ended and less step-by-step tutorial style as they have been up until now. Be sure to use the Discord to solicit feedback on your designs to learn and improve!

<br>

<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>

// Initialize slide index for each slideshow

let slideIndices = [0];

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

  currentSlide(1);

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