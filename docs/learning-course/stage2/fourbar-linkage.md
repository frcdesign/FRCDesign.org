---
search:
  exclude: true
---

# 2x: Four-bar Linkage

Work In Progress

## Design Theory

### What are linkages / why would you use them

Four bar linkages are an alterative to the slapdown deployment method introduced in 2E {#TODO link}. Carefully designed linkages allow more design flexibility for space constrained designs or designs with difficult required positions for the intake rollers. By adjusting the layout sketch the end positions of the main intake plate can be translated and rotated as desired. A slapdown intake only rotates the intake, so will always end up with the intake being stowed vertically above its pivot point. A four bar intake could package the intake more tightly by translating a large intake closer to the bottom of the robot when stowed.

### Pneumatic vs Motor Actuation

Motors are the most approachable actuation method for any mechanism. Four bar intakes are one of the most common places to use pneumatic cylinders however, and can present some situational benifits. Pneumatic cylinders can move complexity from the mechanical design of the mechanism being designed to the electronics area of the robot. Before deciding on using pneumatics in a design, keep in mind that it imposes the weight and volume of the pneumatic system components onto another area of your robot.

### Linkage mechanical advantage

TODO: graphics for mechanical advantage (avoiding over center)

### Creating a Four Bar Linkage
This step by step guide walks through creating a four bar linkage to intake a 9" foam ball. It is actuated by a pneumatic cylinder.


<details>
  <summary>Alterate Video Tutorial By Nick Aarestad</summary>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QsAC_seQHJY?si=apjY7oN6o2JKj5xE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</details>




<p>Four Bar Guide:</p>
<p>Step 1.<br>
    First you need to understand the desired flow of the game piece through the intake (green arrow). Draw the bumper geometry, starting position of the game piece (touching the front bumper), and ending position of the game piece. Also draw several intermediate positions of the game piece along its path.
    <center><img src="\img\learning-course\stage2-fourbar\step 1 reqs.webp" width="60%"></center>

Step 2a (left).<br>
Next define the extended position and retracted position of your intake rollers (left picture). The rollers should maintain contact and the desired compression of the game piece. In this case the rollers are dimensioned to be 7" away from the bumpers and the leading roller is 7" off of the ground. The retracted state of the intake must be within the frame perimeter of the robot, and should take up as little space as possible.<br>

The main intake plate holds the intake rollers, as well as the mounting points where the four bar linkage links will attach to the intake plate. In the picture on the left the linkage attachment points are defined using triangles. These attachment points must be at a consistent location relative to the rollers. Equals constraints are used on each one of those construction lines between the extended and retracted states to make sure they are the same.<br>

Step 2b (right).<br>

The positions of the intake rollers are typically full defined, but other points will need to be moved around as required to design a functional linkage. The linkage attachment points in the intake plate, and the linkage attachment points to the chassis should be moved around by hand until a reasonable geometry is accomplished. Then, as in the right picture, use dimensions to fully define the linkage. The attachment points to the chassis should be dimensioned, and some points will end up fully defined as a result of the geometric constraints.
<center><img src="\img\learning-course\stage2-fourbar\step 2a partial sketch.webp" width="45%">  <img src="\img\learning-course\stage2-fourbar\step 2b full sketch.webp" width="45%"></center>
Fully Defined Layout Sketch:<br>
<center><img src="\img\learning-course\stage2-fourbar\step 3 layout sketch.webp" width="60%"></center>
Step 4. (only if pneumatic)<br>
In this example a pneumatic cylinder will be used to actuate the linkage in and out. The longer solid line is the extended length of the cylinder and the shorter construction line is the retracted length of the cylinder. There are many other ways to arrange this linkage, including ones that act on the top arm instead of the bottom arm, or that result in the cylinder being retracted when the intake is extended. Define the point onto the link where the cylinder will attach (5.5" dimension) at both the extended and retracted states of the linkage. The rear mounting point of the linkage will then be fully defined, and the linkage layout is complete.
<center><img src="\img\learning-course\stage2-fourbar\step 3 pneumatic sketch.webp" width="60%"></center>
Step 5. <br>
Using proper parametric cad practice, you are now ready to sketch and extrude the plates for the intake and linkage. These should be where they will actually be in the assembly not on the center line of the part studio. Advanced sketching techniques can be used to ensure zero collisions or perfect fit between the links. Do not attempt this for your first design. Instead, make simple shapes, then check for interferences in the assembly and adjust the plates as needed until there are no collisions at both ends of travel. These plates will take serious intakes with other robots and the field, 1/4" polycarbonate with significant margins around each hole (>0.5") is recommended.
<center><img src="\img\learning-course\stage2-fourbar\step 5 extrude plates.webp" width="60%"></center>
Step 6. <br>
Four bar linkages can be quite complicated to assemble, and will not be as clean as a simpler assembly with fewer moving subassemblies. That said, be sure to use proper origin cube assembly practices when assembling your intake. This picture shows the fully assembled intake plates, as well as the pneumatic cylinder. It includes some other hardware for clarity such as the intake rollers but should not be taken as an example of a good design. Insert the four bar layout sketches into the assembly and make sure that the intake moves exactly as you expect it to. The image shows the retracted state of the intake where the pneumatic cylinder is fully retracted, and the plates match the layout sketch perfectly. If this is not the case you must track down the problem and fix it.
<center><img src="\img\learning-course\stage2-fourbar\step 6 assembly.webp" width="60%"></center>
[onshape link](https://cad.onshape.com/documents/9aeba443b3990c61c52d9613/w/fe0631a64edb24356a3dbe20/e/673191a338fd6c4480e9d624?renderMode=0&uiState=663e8f226d078f47b184758e)


<br>

<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
</script>