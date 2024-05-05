<style>
.right{
    float:right;
}

.left{
    float:left;
}
</style>

# Assembly Best Practices

<span class="left">[< Feature Tree Best Practices](feature-tree-setup.md)</span> 
<br>


Assuming you have already named your parts and organized your work within the rest of the document, creating a well-organized assembly is very straightforward. 

## 

## Process for Inserting Parts

1. Chose a method for creating an origin mate connector in your part studio
2. Insert the whole part studio with the green checkbox so the origin is in the same place
3. Use the "group" tool on all parts that don't move
4. Fasten the origin mate connector to the origin
5. Duplicate and fasten any duplicate parts

This is a fast and parametric way of putting together an assembly, as opposed to using mates to constrain all the parts that were already in the correct place.

!!! Tip
    As you add more parts in the part studio, you can insert them individually into the assembly with the green checkmark, double click on the initial group, and add the part to the group to avoid mating it. This means that new part will always stay in the same place relative to where it was designed in the part studio.

Make sure you sort the instances in your assembly into folders (i.e. tubes, swerve modules).


## The Importance of Intelligent Origins
As with many good practices in CAD, smart origins are another good practice to make future you's life easier. Intelligent origins allow designers to leverage default geometry (Front/Right/Top Planes, Origin Point) in their models. Good designers will utilize the default geometry for robust axes of symmetry and references. 

However, it should be noted that with multi-body part modeling, as opposed to a typical 1 part per file workflow in Solidworks, origins for parts are not quite as critical since there are multiple parts in a single file. For FRC CAD, the purpose of origin is two fold:

1. To use the same origin point across all part studios and assemblies in order to have the same origin as the master sketch.
2. To unify the robot CAD and robot software origin point. By having the same origin in CAD and code, the robot can be seamlessly exported to [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope) and camera transformations more easily measured. 

!!! Note
    Although definitions may vary from team to team, the origin of an FRC robot is typically defined as ***the center of the drivebase, on floor level***.

In the following sections, a few different methods for creating origins are introduced.

### Origin Cube Method
The origin cube Featurescript inserts a 2"x2"x2" transparent cube at the origin of the part studio. The cube has a mate connector for the origin. There is also an option to import a number of useful design constants (bolt hole sizes, common FRC dimensions, etc).

Compared to other methods like fixing components, the origin cube is a more robust and parametric method of aligning origins.

In each sub assembly, the cube is mated to the origin. Then, in the top level robot assembly, all the origin cubes are mated together to create the final robot assembly.

[Link to Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/df3afdbec8d1356c2af15e4b?renderMode=0&uiState=6637caa6ccbcaa36badca03a)

<center> <img src="\img\best-practices\originCubeFeature.webp" width="60%"> </center>
<center> *Inserting the Origin Cube feature.* </center>

#### Utilizing Origin Cube for Flexible Assemblies

To utilize the full potential of origin cubes and master sketches, it is recommended to have separate sub assemblies for the stationary group of components and the moving group of components of each mechanism. A single part studio or multiple part studios can be used to achieve this, it is up to the personal preference of the designer.

Take a slap down intake for example. In this example, two part studios that reference the same master sketches are used: one for the arm base and gearboxes, and one for the intake arm. The following three assemblies are then formed: the base components assembly, the arm components assembly, and the top level intake assembly containing the first two sub assemblies. The base component assembly and arm component assembly are both rigid assemblies with their respective origin cubes mated to their assembly origins. A rigid assembly is one where there are no moving components. The top level intake assembly should then only include two mates: a fasten to mate the origin cube of the base assembly to the origin, and a revolute mate to enable the motion of the arm.

The full file tree of this example will appear like so:

* Top Assembly: Intake
* Assembly: Intake Base
* Part Studio: Intake Base
* Assembly: Intake Arm
* Part Studio: Intake Arm

If only a single part studio is used, then there would be a single intake part studio:

* Top Assembly: Intake
* Assembly: Intake Base
* Assembly: Intake Arm
* Part Studio: Intake

<details>
<summary>Images of example assembly</summary>
<br>

<center><img src="/img/best-practices/0200-A.webp"><figcaption>Top Level Assembly: 0200-A-Intake. Notice that there is only two mates. The revolute is between the two intake pivot mate connectors, which are attached to the repective origin cubes.</figcaption></center>

<center><img src="/img/best-practices/0210-A.webp"><figcaption>Stationary Components Assembly: 0210-A-Intake Base. The components are group mated and the origin cube is fastened to the origin.</figcaption></center>

<center><img src="/img/best-practices/0210-PS.webp"><figcaption>Stationary Components PS: 0210-A-Intake Base. Notice the intake pivot mate connector, derived from the orange master sketch. </figcaption></center>

<center><img src="/img/best-practices/0220-A.webp"><figcaption>Moving Components Assembly: 0220-A-Intake Arm. The components are group mated and the origin cube is fastened to the origin.</figcaption></center>

<center><img src="/img/best-practices/0220-PS.webp"><figcaption>Moving Components PS: 0220-Intake Arm. Notice the intake pivot mate connector, derived from the orange master sketch.</figcaption></center>

</details>

In order to create a more robust revolute mate for the pivot, start by creating a mate connector in both part studios at the pivot point and attaching it to the origin cube. Then, in the top level assembly, add a revolute mate between the two origin cube's pivot mate connector and optionally set angle limits. By referencing the master sketch for the pivot point, the mate becomes parametric to any changes in either part studio. In fact, there would not need to be *any* parts in either assembly for the pivot to work because the mate connectors are attached to the origin cubes.

Again, the separation of the stationary components and moving components into two part studios for this example is purely personal preference. The key takeaway is that the parts need to be inserted into separate sub assemblies. A simple example of both methods is given in the Origin Cube Featurescript document.

This same method can also work for any type of flexible mechanism including elevators and linkages.

<!-- <details>
<summary>A video explanation is also available.</summary>
<br>

Coming Soon

</details> -->

### Origin Mate Connector Method
WIP


## Other Best Practices

The first advice is to minimize primitives in your assembly. Primitives are kinda like the number of triangles used to render the mesh of the object, or in more simple terms, it's a measure of how complex the object is and how hard it is for Onshape to render. The more primitives there are, the more laggy your assembly will be.

Use [simplified models](https://www.frcdesign.org/simplified/) wherever possible to minimize primitives: electronics, swerve modules, motors, etc. Some of these are added to MKCAD as well.

<details>
<summary>Minimize Primitives</summary>
  <figure class="video_container">
    <video controls="true" allowfullscreen="true" poster="/img/best-practices/minimizePrimitives.webp">
      <source src="/img/best-practices/minimizePrimitives.webm" type="video/webm">
    </video>
  </figure>
</details>

Other things to keep in mind:

- Import COTS parts from MKCAD
- Use the **replicate tool** for adding hardware! You should only need toimport one of each type
- Minimize the number of mates you use; this lowers the solve time
- Stay organized with folders

See a well-organized assembly here: 

<center><img src="/img/best-practices/assembly.png"></center>

<br>
<span class="left">[< Feature Tree Best Practices](feature-tree-setup.md)</span>
<br>
<br>