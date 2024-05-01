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
</style>

# 1C: Gearbox Projects

<span class="left">[< 1B: Swerve Drivebase](1B-swerveDrivebase.md)</span> <span class="right">[2A Full Detail Drivebase >](../stage2/2A-drivebaseFullDetail.md)</span>
<br>

Though you can buy premade planetary gearboxes from vendors (which are still very good in a lot of use cases and packaging), custom gearboxes are typically more versatile in tight packaging situations, and can be tuned better to avoid backlash.
[comment]: <> (Link to designing for control page for reducing backlash)

## New Concepts
**Motors:**

- Spin! They add movement to your robot
- Use battery power to create motion
- Object manipulation, movement around the field, just about anything on your robot can be moved with the right motors and ratio

**Transfer of Motion:**
Gears, belts, and chains are used to both transfer torque from one shaft/mechanism to another. 

- **Mechanical advantage:** given a set speed and torque from a motor, you can use the difference between gear teeth, pulley teeth, or sprocket teeth to transfer speed to torque. A small gear on your motor meshing with a large gear on another axle will decrease the output speed but increase the torque, and is called a *reduction*. The opposite is true as well: a large gear meshing with a smaller gear will increase output speed but decrease the torque, and is called an *upduction*.

- Besides rollers and shooter wheels, reductions are necessary to optimize motor speed vs. torque. This reduction can be calculated with [ReCalc](https://www.reca.lc/) or a variety of spreadsheet calculators found on ChiefDelphi, such as [KLib](https://www.chiefdelphi.com/t/klib-a-tool-for-frc-design/398904/16).

<center><img src="\img\design-guide\stage1c\powertrains.webp"></center>

- Gears mesh together directly and cause the direction of rotation to switch, belts/pulleys and chain/sprockets work at a distance and don't cause a change in direction of rotation.
- Belts are lightweight and drive high speed mechanisms well, but can skip with high loads if not tensioned perfectly
- Chains are heavy duty and handle high torque well, but always need an extra tensioning mechanism for maintenance as they stretch through use

**Bearings**

- Allow axles to spin OR stuff ON an axle to spin (or both)
- 0.5in hex axles are the most common in FRC, and rounded versions can use special bearings with an inside diameter of 13.75mm (referred to as thunderhex bearings)

### Common Measurements

- 0.196 inches = #10-32 bolt (hardware standard) close fit hole. As #10-32 hardware is standardized for most COTS parts, we try to exclusively use this except where stronger 1/4-20 bolts are needed
- 1.127 inches = Rounded hex bearing hole. This size may change depending on your team's machining tolerances. Ask someone more experienced if they know, otherwise use this reference number.
- 60mm = CIM class Motor Diameter (Kraken, Vortex, Neo, etc)
- 2 inches = Motor Mounting Hole Circle
- 0.8 inches = Motor Center hole

The pitch diameter is the diameter of the gear where if two pitch diameters are touching, allows the gears to perfectly mesh.

- Pitch Diameter = number of teeth/diametrical pitch
- Diametrical pitch = dp, the number of teeth per inch of diameter. Pretty much every gear we use in FRC will be 20 DP.
- In CAD, this means you can make bearing holes for axles based off of two construction circles representing gears (dimensioned with the pitch diameters) that are tangent to each other
  
Gears always come in even increments of teeth, but you should check a COTS vendor to see what gears they provide. It should be under "20 DP gears" from West Coast Products, REV, or Andymark.

## Gearbox 1
The first gearbox introduces you to some basic ideas. As always, it's a mix between CAD fundamentals and FRC fundamentals. By the end of this you should be able to design a simple 1-stage gearbox with a motor.

This project is a little less guided than the last one, and introduces you to basic plate design, the spacer and shaft featurescripts, and way more assembly fundamentals and MKCAD insertion. Try to copy [this gearbox](https://cad.onshape.com/documents/ff20a652374bc6dccedba340/w/c40a663858e835275eedc6be/e/df046387942e63628ef3d99c?renderMode=0&uiState=66328dd3b89a596adab116a3), making sure to use a single sketch to drive the whole gearbox structure, especially all the hole placements. 

You can watch this video for a full tutorial:
<center><iframe width="880" height="550" src="https://www.youtube.com/embed/OE-NVLBxm6I" frameborder="0" allowfullscreen></iframe></center>


## Gearbox 2
The second gearbox introduces you to some more featurescripts as well as more design fundamentals. Try to copy [this gearbox](https://cad.onshape.com/documents/dbfca47b976b572e1ed949ec/w/3e1d28e9efa9b31b349bcd33/e/03fe2e65fe5e7e357d04ce9e?renderMode=0&uiState=662da16d9cc5a27a76e8e6b8), again keeping in mind to use layout sketches:

<center>![Gearbox](\img\design-guide\stage1c\gearbox.webp){width=45% height=45%}</center>

Check out these two videos to learn concepts about plate design and belt/pulley design (which will both be used for this gearbox):

<center>
<iframe width="880" height="550" src="https://www.youtube.com/embed/9ckB7p3kp6c" frameborder="0" allowfullscreen></iframe>

<iframe width="880" height="550" src="https://www.youtube.com/embed/fX-BLKZHsJM" frameborder="0" allowfullscreen></iframe>
</center>

Once you've finished both of the gearboxes, you can move on to Stage 2 and start working on more complex mechanisms!

<br>
<center>1C: Gearboxes</center> 
<span class="left">[< 1B: Swerve Drivebase](1B-swerveDrivebase.md)</span> <span class="right">[Stage 2 >](../stage2/2.md)</span>
<br>
<br>