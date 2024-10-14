

# 1E: Subsystem Workflow - Detailing the Drivebase

## Exercise: Mounting Electronics

In the reference design, the Power Distribution Hub (PDH), main breaker, and RoboRIO are mounted onto the bellypan. The [`Electronic Mounting` Featurescript](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/83cfa4ae1a46ea05581445c9 "Electronic Mounting Featurescript Onshape Document"){:target="_blank"} can be very useful for generating the mounting holes for electronics. If you cannot accurately manufacture mounting holes for electronics, VHB tape (which comes in the Kit of Parts) can be a good option for robustly securing your electronics.

### Bellypan Mounting Instructions

**Add mounting for some electronic components to your drivetrain.** You can take inspiration from the following instructions slides. 

<!-- <center>**Sample Electronics Mounting Slides**</center> -->
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
            <figcaption>1. Draw box outline for PDH and RoboRIO. Also add the outline and holes for the main breaker. (The `Electronic Mounting` Featurescript does not support mounting holes for the main breaker at this time unforunately).</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <video width="1920" controls>
              <source src="/img/learning-course/stage2-drivebase/elec/elec1s2.webm" type="video/webm">
              Your browser does not support the video tag.
            </video>
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
    <button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
    <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
    <!-- The dots/circles -->
    <div class="dotsContainer" style="text-align:center">
        <!-- Dots will be generated here -->
    </div>
</div>

!!! Tip "Simplified Models"
    It is recommended to use the Simplified electronics models to improve assembly performance. You can read more about simplified models on the [Assembly Best Practices Page](/best-practices/assembly-setup/ "Assembly Best Practices Page"){:target="_blank"}. Simplified swerve module models can also be used to reduce lag. 

### Robot Signal Light (RSL)

Every robot is also required to have a Robot Signal Light (RSL). An easy location to mount the RSL is on the side of the drive frame. Typically, only one RSL is required and needs to be “easily visible while standing 3 ft. (~ 100 cm) away from at least one side of the ROBOT”. Be sure to check the latest game manual rules for the most up to date RSL mounting rules.

**Add mounting for an RSL to your Stage 1D drivetrain.** You can take inspiration from the following image. 

<center><img src="\img\learning-course\stage2-drivebase\elec\RSL.webp" style="width:80%"></center>
<center><figcaption>RSL mount constructed out of 1/8" thick polycarbonate plate. The mounting hole for the RSL is 1” in diameter. The RSL model can be found in the MKCad App.</figcaption></center>

### Radio

Each robot is also required to have a radio. The radio should be mounted on the robot following Vivid Hosting's [radio mounting guidelines](https://frc-radio.vivid-hosting.net/getting-started/usage/mounting-your-radio "Vivid Hosting Radio Mounting Guidelines"){:target="_blank"}.



<br>
