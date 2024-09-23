# 1D: Design Methodology - Simple Swerve Drivebase

## Top Down Design Methodology 
When designing a model in CAD, there are two high level strategies that can be employed: top-down and bottom-up. Top-down design employs high level, low detail sketches to dictate the design, and then refining details and components within that framework. Conversely, bottom-up design involves creating individual components or parts separately and then assembling them to form the final product. 

Top-down design offers a holistic approach, allowing for better system integration, consistency, and is more parametric. Bottom-up design offers flexibility and independence in designing individual parts. In FRC robot design, top-down approach is favored as system integration is often the most challenging aspect. Top-down ensures that the robot architecture dictates part design.

### Master Sketch

To achieve this, a ***master sketch*** is utilized. A master sketch is a series of sketches that capture the major dimensions of each mechanism, field element interactions, and robot size constraints. Then, the master sketch(es) are inserted into each mechanism's part studio and the individual components are then modeled around the imported layout sketch. More information on master sketches can be found on the [Master Sketch Best Practices](../../../best-practices/mastersketch-setup.md "Master Sketch Best Practices Page"){:target="_blank"} page.

???+ Example "Example Master Layout Sketch"
    <center><img src="\img\learning-course\stage1d\exampleMasterSketch.webp" style="width:60%"></center>
    <center>*Example of robot master sketches. Each mechanism has a number of layout sketches that capture the important details.*</center>


### Origin Placement and Origin Cube
To fully utilize master sketch top-down design, we must choose a unified origin for all part studios. Utilizing the same origin as the master sketch across all part studios and assemblies is twofold:

1. The origin will always be a consistent central point you can reference. This helps keep things parametric too.
2. To unify the robot CAD and robot software origin point. By having the same origin in CAD and code, the robot can be seamlessly exported to [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope "AdvantageScope Repository"){:target="_blank"} and camera transformations more easily measured. 

!!! Note
    Although definitions may vary from team to team, the origin of an FRC robot is typically defined as ***the center of the drivebase, on floor level***.

To achieve this, we use the [`Origin Cube` Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/df3afdbec8d1356c2af15e4b?renderMode=0&uiState=6637caa6ccbcaa36badca03a "Origin Cube Featurescript Document"){:target="_blank"} which generates a transparent 2" cube at the origin and provides several useful constants and functions that have already been used in previous stage.

The Origin Cube will become very useful later on for assembly mating but for now all you need to remember is that **the Origin Cube should be the first feature in all part studios**. You can read more about the Origin Cube on the [assembly best practices page](../../../best-practices/assembly-setup.md "Assembly Best Practices Page"){:target="_blank"}.

<br>