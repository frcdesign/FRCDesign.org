# 2C: Slapdown Intake

## Pivot

### Gear Ratio

The pivot is powered by a single Kraken motor on a 2-stage MAXplanetary gearbox. The 4:1 stages in the MAXplanetary (16:1) and the 12:48 sprocket reduction make a total of 42:1 overall reduction for the pivot. 

You can assess whether you want this much reduction on your own mechanism by using an arm calculator, but around 30:1 to 42:1 should be good for most intakes.

### Pivot Design

The MAXplanetary uses a 1:1 belt/pulley to transfer rotation to a long cross-axle. All custom pulleys have pockets for COTS metal inserts to prevent them from stripping. There are sprockets on either end of this cross axle, with chain going up to sprockets attached to the arm. This setup is to ensure both sides of the intake are moved up and down equally so there's no weird twisting forces on the intake.

### Backlash and Sensor Feedback

To reduce backlash in the system, the 1:1 belt/pulley is exact center-center distance and the chains are tensioned with inline tensioners. Large sprockets on the output of the arms are good as well for more teeth engagement with the chain.

For controlling the intake position, no absolute encoder is needed. You can zero the position when it is stowed and against the hardstop or have it rest on the ground when the robot is turned on, and use the relative encoder to take it to a specific position down.

<figure>
    <img src="\img\learning-course\stage2-slapdown\pivot.webp" alt="Power Example" width="60%" style="border:5px solid #ADADAD">
    <figcaption> Reference Design Intake Pivot</figcaption>
</figure>

<br>