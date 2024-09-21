

# 1E: Subsystem Workflow - Detailing the Drivebase

## Exercise: Bumpers
Bumper construction is described in each year’s FRC game manual. Typically, it is required to be two 2.5” diameter pool noodles backed by a 5” tall 3/4" thick plywood sheet. Refer to the latest game manual for the most up to date bumper rules. Bumper cutout and ground clearance rules will vary from year to year.

### Bumper Model
It is recommended to place the bumpers in a new part studio and assembly to keep your feature and assembly trees organized. The minimum level of detail should be a block model of the bumper. Some teams may opt to model the bumper wood, bumper wood holes, angle brackets for the bumper wood, and other details to assist with manufacturing. You should communicate with the rest of your team members to determine the level of detail that is required. 

### Instructions

**Add bumpers to your Stage 1D drivetrain.** You can take inspiration from the following instructions slides.

<!-- <center>**Sample Bumper Modeling Slides**</center> -->
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
    <button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
    <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
    <!-- The dots/circles -->
    <div class="dotsContainer" style="text-align:center">
        <!-- Dots will be generated here -->
    </div>
</div>

Keeping the bumper part studio and assembly separate from the drivetrain keeps the drivetrain feature tree cleaner and allows for easier hiding/showing of the bumpers in the top level assembly since you can show and hide the entire bumper assembly at once.




<br>
