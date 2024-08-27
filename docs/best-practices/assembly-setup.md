---
title: Assembly Best Practices
description: The best practices for inserting parts into assemblies and organizing them.
---

# Assembly Best Practices

Assuming you have already named your parts and organized your work within the rest of the document, creating a well-organized assembly is very straightforward. 

### The Importance of Intelligent Origins
As with many good practices in CAD, smart origins are another good practice to make future you's life easier. Intelligent origins allow designers to leverage default geometry (Front/Right/Top Planes, Origin Point) for robust axes of symmetry and references in their models. 

For FRC CAD, the purpose of using the same origin as the master sketch across all studios and assemblies is twofold:

1. The origin will always be a consistent central point you can reference. This helps keep things parametric too.
2. To unify the robot CAD and robot software origin point. By having the same origin in CAD and code, the robot can be seamlessly exported to [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope) and camera transformations more easily measured. 

!!! Note
    Although definitions may vary from team to team, the origin of an FRC robot is typically defined as ***the center of the drivebase, on floor level***.

### The Origin Cube 
The [Origin Cube Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/df3afdbec8d1356c2af15e4b?renderMode=0&uiState=6637caa6ccbcaa36badca03a) inserts a 2" transparent cube at the origin of the part studio. The cube has a mate connector at the origin. Because this part will never change and always stays at the origin of the part studio, using it to group and fasten parts to the origin will always be more **robust and parametric** than fixing or using a mate connector attached to another part, in case that part changes or is deleted.

<figure>
<img src="\img\best-practices\originCubeFeature.webp" width="60%">
<figcaption>Inserting the Origin Cube feature</figcaption>
</figure>

!!! Tip
    The origin cube has the option of importing a number of useful constants and functions, including bolt hole sizes, gear outer diameter, and a center-to-center calculator.




### Process for Inserting Parts

As is described in [Sub-Document Setup](sub-document-setup.md#subsystems-with-multiple-degrees-of-freedom), subsystems with no degrees of freedom will only have one assembly, while subsystems with multiple moving parts are separated into rigid assemblies. The process for inserting parts and finishing assemblies is similar for both circumstances.

1. Create the origin cube in your part studio
3. Insert the related parts and origin cube for a rigid subassembly
4. Use the "group" tool on all parts
5. Fasten the origin mate connector to the origin
6. Duplicate and fasten any duplicate parts
7. Insert standard hardware and COTS components
8. Sort the instances into folders (i.e. tubes, swerve modules, spacers)

!!! Tip
    As you add more parts in the part studio, you can insert them individually into the assembly with the green checkmark, double click on the initial group, and add the part to the group to avoid mating it. This means that new part will always stay in the same place relative to where it was designed in the part studio.

If the subsystem has multiple moving parts (like an over-the-bumper intake or elevator), create a mate connector on the master sketch for each degree of freedom. This may be a pivot point or the starting point of a slider mate (in the case of an elevator). Make each mate connector owned by the origin cube.

Repeat steps 4-7 of the process for all other rigid subassemblies, if applicable. This will result in each subassembly being rigid, with the origin cube fastened to the origin and all the parts in the same place as in the part studio. Each subassembly will also contain the mate connectors owned by the origin cube.

Now create a top-level subsystem assembly and insert each subassembly into it. Fasten the origin cube of the static subassembly to the origin, and use the other mate connectors to mate the other subassemblies together.

??? Example "Stage 2D - Slapdown Intake"
    [Stage 2D - Slapdown Intake](https://cad.onshape.com/documents/17302d787e092ce11015f7ee/w/f7cf5c02c7655f0328a3a74a/e/f1456325e0175c4c081008c2) is a subsystem with a static portion and a pivoting portion. An extra mate connector is added for the pivot on the master sketch, owned by the origin cube

    <center><img src="/img/best-practices/slapdown-intake-example/slapdown-intake-mate-connector.webp" style="border:5px solid #ADADAD"></center>

    This mate connector exists in both subassemblies.
    <center><img src="/img/best-practices/slapdown-intake-example/slapdown-intake-static-connectors.webp" style="border:5px solid #ADADAD"></center>

    <center><img src="/img/best-practices/slapdown-intake-example/slapdown-intake-arm-connectors.webp" style="border:5px solid #ADADAD"></center>

    The static assembly is fastened to the origin and the arm assembly revolves using the pivot mate connector owned by both instances of the origin cube.
    <center><img src="/img/best-practices/slapdown-intake-example/slapdown-intake-top-level.webp" style="border:5px solid #ADADAD"></center>


??? Example "Stage 2E - Cascade Elevator"
    [Stage 2E - Cascade Elevator](https://cad.onshape.com/documents/da5aef9e6bf6e869f4a51a45/w/5a0f4a3426876db0ba214277/e/f8fd8133abcb12800eacb5d1) is a subsystem with a static portion and two subassemblies that slide linearly. This contains a part studio, a static frame/gearbox assembly, assemblies for the first stage and carriage, and a top-level assembly combining the 3 subassemblies with slider mates.

    <center><img src="/img/best-practices/elevatorAssembly.webp" style="border:5px solid #ADADAD"></center>


??? Example "3647 Millennium Falcons 2024 Intake"
    <center><img src="/img/best-practices/0200-A.webp"><figcaption>Top Level Assembly: 0200-A-Intake. Notice that there is only two mates. The revolute is between the two intake pivot mate connectors, which are attached to the repective origin cubes.</figcaption></center>

    <center><img src="/img/best-practices/0210-A.webp"><figcaption>Stationary Components Assembly: 0210-A-Intake Base. The components are group mated and the origin cube is fastened to the origin.</figcaption></center>

    <center><img src="/img/best-practices/0210-PS.webp"><figcaption>Stationary Components PS: 0210-A-Intake Base. Notice the intake pivot mate connector, derived from the orange master sketch. </figcaption></center>

    <center><img src="/img/best-practices/0220-A.webp"><figcaption>Moving Components Assembly: 0220-A-Intake Arm. The components are group mated and the origin cube is fastened to the origin.</figcaption></center>

    <center><img src="/img/best-practices/0220-PS.webp"><figcaption>Moving Components PS: 0220-Intake Arm. Notice the intake pivot mate connector, derived from the orange master sketch.</figcaption></center>


### Simplified Models

The first advice is to minimize primitives in your assembly. Primitives are a measure of how complex the object is and how hard it is for Onshape to render. The more primitives there are, the more laggy your assembly will be.

Use [simplified models](https://www.frcdesign.org/resources/simplified/) wherever possible to minimize primitives: electronics, swerve modules, motors, etc. Some of these are added to MKCAD as well.

??? Video "Minimize Primitives"
    <video controls="true" allowfullscreen="true" poster="/img/best-practices/minimizePrimitives.webp">
      <source src="/img/best-practices/minimizePrimitives.webm" type="video/webm">
    </video>

Other things to keep in mind:

- Import COTS parts from MKCAD
- Use the **replicate tool** for adding hardware! You should only need to import one of each type
- Minimize the number of mates you use; this lowers the solve time
- Stay organized with folders

See a well-organized assembly here: 

<center><img src="/img/best-practices/assembly.webp"></center>

<br>