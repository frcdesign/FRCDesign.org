<style>
* {box-sizing:border-box}

details {
        font-size: 0.7rem !important;
    }   

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

# 2H: Cascade Elevator

## Cascade Elevator
Elevators pop up commonly in FRC and are used to move mechanisms in a compact linear fashion. This is usually to reach higher places with a mechanism, reach far out from your frame perimeter, or even climb on a field element. Elevators are typically classified by the way they are "Rigged". Elevator "Rigging" is what allows the motor to transmit motion to each stage. FRC elevators are usually rigged to be either Cascade or Continuous. This page will be covering the design of a Cascade elevator due to there currently being much better COTS part availability for making a Cascade elevator.

<br>
<figure><img align="left"  src="\img\design-guide\stage2-elevator\2468elevator.gif" width="50%"><img align="right" src="\img\design-guide\stage2-elevator\4414elevator.gif" width="40%"></figure>
<figcaption>2468's Cascade Elevator and 4414's Continuous Elevator</figcaption>
<br>

Some match videos with examples of elevators include [one showcasing 2468's 2023 Robot with a cascade rigged elevator](https://www.youtube.com/watch?v=RAFjZgB_72w){target=void} and [one showcasing 4414's 2023 Robot with a continuous rigged elevator](https://youtu.be/PKPuqpe1Wlg){target=void}.

Elevators as designed most typically may be out of the scope of a lower-capability team because of the amount of custom metal parts that need to be bought or manufactured, but once you know how one works and have designed one, you may be able to make one with minimal manufacturing capabalities and time required.

## "Cascade" Motion
Cascade elevators are characterized by the way the stages move. In a cascade rigged system, each elevator stage moves the same distance from its parent stage.

<figure markdown="span">
    ![cascade](/img/design-guide/stage2-elevator/cascade.gif)
    <figcaption>Cascade Motion</figcaption>
</figure>

### Comparison

| **Pros** | **Cons** |
|----------|----------|
| Cascade elevators are great when you just need to move a mechanism up and down and you don't need more than 3 Elevator stages to reach the desired height. While it is possible to make cascade elevators with more than 3 stages, designing the rigging gets harder, especially if you are width constrained. | Usually things cannot be passed through a cascade elevator because of the rigging, while you can pass things through a continuous elevator. |
| Cascade motion is faster than continuous due to the stages being linked together and continuous effectively being one long stage. | The center of gravity is not optimal in the middle range of extension compared to continuous. |
| All of the major Cascade Elevator components are available as COTS components, which means you can simply stock cascade elevator components and throw it together without worrying about custom manufacturing. | The motors powering a cascade elevator need geared down more to counteract the natural upduction the cascade rigging adds. |


<br>

## Project

Because elevators are just mechanisms to move other mechanisms around, this project is similar to the dead axle pivot and will be designed without much context to learn the design process and components. You will get practice with designing elevators in the context of a robot in Stage 3.

<figure markdown="span">
    <img src="/img/design-guide/stage2-elevator/elevatorTopLevel.webp" style="width:85%">
</figure>

The reference is provided in [**this document**](https://cad.onshape.com/documents/da5aef9e6bf6e869f4a51a45/w/5a0f4a3426876db0ba214277/e/c64f9fd69e2ddbe82410f283). You should model a copy of it in your own document. The mechanism design concepts, decisions made for this design, and a basic guide are all provided below.

### Key Components

Elevators have some key components that differ from most other mechanisms, and it's important to understand all of them.

??? Concept "Elevator Blocks"

    Every modern elevator will use some form of "elevator block" to allow the stages to slide past each other smoothly using bearings. Most teams will purchase elevator blocks from WCP or TTB instead of manufacturing them in-house (because of the time investment and machining capabilities of a typical team) but ones can be made with plates instead of billet (see [2471 2018](https://cad.onshape.com/documents/bd18a956391f75b5bca27546/w/827793489fb93072e2a1d993/e/adea515b9f2a94ccfd7ca72e)). 
    <br>

    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/elevator-blocks.webp" style="width:75%">
    </figure>

    The elevator featured in this guide uses the WCP Inline Clamping and Inline blocks, but different blocks from WCP or TTB could be substituted with little to no design changes besides the distance between the stages on the sides.

??? Concept "Chain Attachment Point"

    Most cascade elevators use chain to power their initial stage; this chain can run either parallel or perpendicular to the face of the elevator, but the core concept is the same. The chain is bolted to the first stage of the elevator, and the rigging moves the other stages off it. The elevator design featured in this guide uses the TTB chain comb to bolt the chain to the first stage.
    <br>

    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/chain-comb.webp" style="width:75%">
    </figure>

??? Concept "Rigging"

    Elevator rigging typically takes up the bulk of the design process, as its the most important part of the elevator. Rigging style, and organization drives the motor mounting, and position of the crossmember the clamp plate is mounted to, so its important to properly plan out the cable paths.
    <br>
    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/rigging-light.webp#only-light" style="width:50%">
        <img src="/img/design-guide/stage2-elevator/rigging-dark.webp#only-dark" style="width:50%">
    </figure>

??? Concept "Cable Clamp & Pulleys"

    Cascade elevators function by moving a fixed length of cable from one side of a clamp to the other side of the clamp, to force the elevator up. This cable clamp is usually bolted to some form of crossmember. The elevator from this guide uses the TTB cable clamp to maintain consistency in rigging components (they come in [a kit](https://www.thethriftybot.com/products/elevator-dyneema-pulley-kit?_pos=6&_sid=1876486ab&_ss=r)). The clamp consists of two plates; the first one is fastened to the tube and the second one is ONLY fastened to the first plate. You can choose to make access holes for the bolts or bolt all the way through the cross member with a crushblock.

    !!! Note 
        The WCP cable clamp uses a similar design but the fasteners go through both plates into the crossmember tube, sharing the clamping force with the crossmember.
    <br>

    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/cable-clamp.webp" style="width:75%">
    </figure>

??? Concept "Cable Ends"

    The ends of the cable are arguably the most important part of elevator rigging to do right. If they are handled improperly it can cause issues with rigging falling apart during impacts; this usually takes the elevator (and anything requiring it to move) completely out of commission for the match. Cascade rigging consists of at least one loop of cable per stage, which drives the motion for the next stage.
    <br>

    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/carriage.webp" style="width:50%">
    </figure>

    To ensure smooth motion, these cables need tensioned. One of the best ways to tension these cables is through a ratcheting cable spool. The COTS solution is to use the [WCP Ratchet Plate](https://wcproducts.com/products/wcp-0585) (though an easy homemade solution can be done by cutting the end off of a ratcheting wrench and fastening it to your mechanism), with a hex shaft acting as the spool. The hex shaft gets a hole drilled in it so the cable is forced to wrap around it. 

    It is important to tie a self-tightening knot in the cable to prevent this from coming undone under high load. This ratcheting spool only needs to be done on one side, with a simple fixed loop on the other side. To tension properly, you will need to loosen the clamping plate before adding tension. This is for two reasons: in order to maintain sync between the stages and so that the tension gets added to each side instead of just the side with the ratchet.
    <br>

    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/ratchet-plate.webp" style="width:50%">
    </figure>


??? Concept "Power Gearbox"

    Elevators need motors to power them. Once you have the rigging planned out you can figure out where you can fit the motors to drive the base elevator stage.
    There are many methods to power the base stage, but this guide will be using a vertical chain, and the TTB chain comb.
    <br>
    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/gearbox.webp" style="width:60%">
    </figure>


### Master Sketches

Elevator master sketches usually start with an extended side view so you can drive the length of it based off of the extension limits and your required beginning and end position for whatever mechanism you're moving. Though this elevator doesn't have that context, it's still useful to follow the same workflow of starting with a side sketch, which will contain most important dimensions but can be hard to conceptualize at first.

<br>

<!-- Slideshow container -->
<div class="slideshow-container">
    <!-- Full-width images with number and caption text -->
    <div id="slide1" class="mySlides fade">
        <figure>
            <img src="/img/design-guide/stage2-elevator/master-sketch.webp" style="width:40%">
            <figcaption>A clean view of the front sketch of the elevator tubes.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/design-guide/stage2-elevator/elevatorSideExtendedSketch.webp" style="width:75%" style="border:5px solid #ADADAD">
            <figcaption> As practice for stage 3, we'll start with defining the position of the elevator in relation to drivetrain side sketch. Use rectangles to represent the 2x2 tube and the length of the stages. Add rectangles to represent the bottom tubes of each stage and carriage as well. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/design-guide/stage2-elevator/elevatorSideRetractedSketch.webp" style="width:70%" style="border:5px solid #ADADAD">
            <figcaption> Feel free to create a retracted side sketch (constraining it to the geometry of the first side sketch) to help double check geometry and integration. This especially helpful when designing a full robot. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/design-guide/stage2-elevator/elevatorFrontSketch.webp" style="width:75%" style="border:5px solid #ADADAD">
            <figcaption> Now add the front sketch to define all the elevator tubes, the width of the elevator, and the distance between stages on the side.</figcaption>
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

!!! Tip
    Instead of creating "extended" and "retracted" views, you can separate the stages into their own individual side sketches to let you "animate" how it moves in the sketch. You can use configurations to do this.



### Part Studio
1. Use the origin cube featurescript and derive the master sketches if you made them in a separate part studio.
2. Use extrude individual to create the tubes (without creating only duplicates; this means only the bottoms of stages on one side).
3. Convert the extrusions into tubes.

    ??? Tip "Converting Extrusions into Tubes"
        Tube converter is the easiest way to do this, as demonstrated before, but the hole pattern can break things and be misaligned pretty easily if the dimensions of the elevator end up changing. The most parametric way is to shell the tubes manually, then use a mix of sketches and linear patterns to create the hole pattern. This way you can build design intent into the hole pattern so it won't be misaligned with anything when dimensions change.

        To create parametric hole patterns, you first use the [**Measure Value**](https://cad.onshape.com/documents/77baa8153589a7fc5f289829/w/cffd0f2a7077380d5378a885/e/d3174bf5315e6aafcb889367?renderMode=0&uiState=652ee7d25129162fc0afad5f) featurescript from CADSHARP to measure the length of the tube. You create your first hole at the top of the tube, then create a feature pattern or sketch pattern down the length of the tube with the distance of 0.5" and the instance count set to `((#frame_side_tube/inch)*2)-1`. This method keeps the hole count parametric to the length of the tube.

4. Transform and copy the tubes to complete the structure.

    !!! Tip
        At this point, as design lead, you could create mate connectors, subassemblies, and top level assembly, and hand off the elevator to other people to parallelize the process if that's how your team works.

5. Model any unique crushblocks

    !!! Info 
        Crushblocks and tube plugs are commonly used for most superstructures and elevators nowadays. Find out what they are and why they're useful on [the design fundamentals page about structure](../../design-fundamentals\structure\structure.md).

    <figure markdown="span">
        <img src="/img/design-guide/stage2-elevator/tubesAndCrushblocks.webp" style="width:75%">
    </figure>

6. Decide where you want your rigging (rope) and model it with a path, profile, and sweep.
7. Derive the [TTB chain comb](https://www.thethriftybot.com/products/elevator-25h-chain-drive-kit) into place on a first stage tube. This is for knowing how much to space the chain off from the tubes.
8. Sketch the chain transmission and crossmember, including the bearing holes for the sprockets.
9. Create the plates and tube for the crossmember. The clamp for the rigging will be mounted to the crossmember, but it's also for the rigidity of the base stage.
10. Derive the [TTB cable clamp](https://www.thethriftybot.com/products/elevator-dyneema-pulley-kit) into place on the crossmember and create mounting holes for it, and a crushblock if bolting all the way through the tube.
11. Add holes for the tube plugs on the crossmember.
12. Create the chain transmission, including the chain, any custom spacers, and axles
13. Derive some maxplanetary parts to build the gearbox around. Create spacers and mounting for both maxplanetaries. Make sure to leave them easily accessible and replaceable
14. Add plates at the bottom of the elevator to support the MAXplanetary shafts.
15. Optionally, derive nut strips and a ratchet plate for the carriage and create the shaft for the rigging to be tied to.
16. Create a reference mate in the middle of the base tube, owned by the origin cube, to later mate the subassemblies together with.

<figure markdown="span">
    <img src="/img/design-guide/stage2-elevator/elevatorPartStudio.webp" style="width:75%">
</figure>

### Assembly
Because this subsystem has multiple moving parts, just like the dead axle pivot and slapdown intake, separate rigid subassemblies should be created for each stage.

Create an assembly for the static parts and follow the typical process for inserting them and creating a rigid body (origin cube, group, fasten to origin). Add the rest of the parts by duplicating existing parts, MKCAD, and standard content, using replicate and patterns when you can.

<figure markdown="span">
    <img src="/img/design-guide/stage2-elevator/frameSubassembly.webp" style="width:85%">
</figure>

Do the same thing for the first stage subassembly.

<figure markdown="span">
    <img src="/img/design-guide/stage2-elevator/stage1Subassembly.webp" style="width:85%">
</figure>

And finally the carriage subassembly.

<figure markdown="span">
    <img src="/img/design-guide/stage2-elevator/carriageSubassembly.webp" style="width:75%">
</figure>

Now create the top level assembly, insert the subassemblies (fasten the origin cube of the static assembly to the origin), and use the reference mates on the origin cubes from the separate subassemblies to create slider mates with limits to define the motion of the elevator. 

<figure markdown="span">
    <img src="/img/design-guide/stage2-elevator/elevatorTopLevel.webp" style="width:75%">
</figure>

Because it's a cascade elevator, you can create "linear relation" between the two slider mates with a ratio of 1. This will link the motion together in the same way it would be in real life.

## Summary

You've completed Stage 2E! To summarize what you've learned in this stage:

- The concepts and key components of a cascade-rigged elevator
- The master sketch concepts and geometry for elevators
- Linear relations in assemblies
- The uses of tube plugs and crush blocks for tube assemblies
- More practice with a mechanism with moving parts and the origin cube

There's a lot of freedom for attaching mechanisms to this kind of elevator. If you mount it 90 degrees offset from the front of your robot, you can even create a passthrough mechanism that can move up and down. Once you practice more master sketch integration in the next stage, you will be able to replicate a robot with an angled elevator in the later part of Stage 3.

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