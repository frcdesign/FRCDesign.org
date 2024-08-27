---
title: Feature Tree Best Practices
description: The best practices for part studio feature trees in each mechanism document.
---

# Part Studio Best Practices

Every part studio feature tree should start with a derive command, pulling down the relevant mastersketch (or multiple for visibility). This is what you will build on. 

The part studio should contain **all parts that need to be manufactured by your team**. This could include fully custom plates, shafts cut to length, modified COTS parts, etc. Unmodified COTs parts should be imported directly into the corresponding assembly - no modification inside the part studio is required. 

Also **avoid duplicating identical parts and over-using intensive featurescripts**, such as tube converter. These practices can make your part studio loading times high and navigation and changes very laggy. Creating only one of each part in the part studio means you can simply duplicate it when assembling while your part studio performance will be greatly improved.

!!! Tip 
    Instead of deriving COTS parts for reference, usually you can add simple measurements in your sketches (like a pitch circle instead of a a derived gear), which faster both in the moment and overall with load times. You can derive parts from your other subsystems (such as the frame and simplified modules from your drivetrain part studio into your intake part studio) and make them closed composites for easy reference, but keep it to a minimum.

**Sort and name the features, parts, and tabs and use folders** to make your CAD more understandable for other people working on the robot. One of the biggest benefits of Onshape is its collaborative capability, but unnamed and unsorted documents eliminate that point entirely. Sorting and naming in real time can also make it easier to go back and change things (which you will inevitably need to do). Some teams even use a part naming system to assist with organizing manufacturing and assembly.

!!! Tip
    You can rename parts manually or use one of many various [featurescripts](https://www.frcdesign.org/resources/featurescripts/?h=feat#onshape) to do so automatically. 

See an example of a well-organized part studio here:

<center><img src="/img/best-practices/part-studio-2.webp"></center>

<br>