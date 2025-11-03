# 1E: Subsystem Workflow - Detailing the Drivebase


## Exercise: Bellypan Pocketing

Some teams may choose to pocket their bellypan to reduce weight and make wiring easier. A pocketed bellypan can save around 3-4 lbs. However, this will add significant machining time if you are manufacturing the bellypan yourself or increase cost if you are purchasing the bellypan from a fabrication service (eg: [Fabworks](https://fabworks.com/ "Fabworks Sheet Metal Services"){:target="_blank"}). You should carefully consider the tradeoffs with your team.

### Instructions

**If you choose to pocket your bellypan for your drivetrain**, you can **follow the instructions in the slides** which utilize the `Part Lighten` [Featurescript](../../../resources/featurescripts.md "Featurescripts Page"){:target="_blank"}. You could also use the `Vent` or `Part Lighten` [Featurescripts](../../../resources/featurescripts.md "Featurescripts Page"){:target="_blank"} to pocket the bellypan. While the workflow may vary slightly between each Featurescript, the general idea is the same. A diamond pattern is recommended for strength and ease of modeling.

<!-- <center>**Sample Bellypan Pocketing Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">
    <!-- Full-width images with number and caption text -->
    <div id="slide1" class="mySlides fade">
        <figure>
            <img src="../images/pocket/pocket-0.webp" style="width:100%">
            <figcaption>0. Pocketed bellypan. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="../images/pocket/pocket-1.webp" style="width:100%">
            <figcaption>1. Draw two perpendicular lines that are offset 45 degrees from vertical and a line offset slightly from the edge of the crosstube. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="../images/pocket/pocket-2.webp" style="width:100%">
            <figcaption>2. Linear pattern the diagonal lines until they completely cover the top portion of the bellypan. These will be the main ribs.
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="../images/pocket/pocket-3.webp" style="width:100%">
            <figcaption>3. Mirror the top ribs to the bottom of the bellypan.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <div class="slide-content">
            <iframe src="https://www.youtube.com/embed/ZvEMMgEf420?controls=1&rel=0&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
            <figcaption>4. Connect any islands that might result from mounting holes being too far from a rib. The video shows a potential workflow that allows you to see the end result of the lighten feature while adding ribs.</figcaption>
        </div>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="../images/pocket/pocket-0.webp" style="width:100%">
            <figcaption>5. Use a pocketing Featurescript to pocket the bellypan. Recommended settings are 0.15” wide ribs and 3/16” tool radius.</figcaption>
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



<br>
