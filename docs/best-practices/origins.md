<style>
.right{
    float:right;
}

.left{
    float:left;
}
</style>


# Origins

<span class="left">[< Document Setup](document-setup.md)</span> <span class="right">[Sub-Document Setup >](sub-document-setup.md)</span>
<br>

## The Importance of Intelligent Origins
As with many good practices in CAD, smart origins are another good practice to make future you's life easier. Intelligent origins allow designers to leverage default geometry (Top/Right/Front Planes, Origin Point) in their models. Designers can utilize these planes for robust axes of symmetry and references. 


<details>
<summary>Examples of good and bad part origins</summary>
<br>
When modeling non-FRC parts, especially in non-multi-body workflow, origins are typically located on key features that have symmetry about them. The following examples help illustrate this.


<span style="color:red">TODO: add examples of good and bad part origins</span>.

</details>

However, it should be noted that with multi-body part modeling (As opposed to say, a 1 part per file workflow in Solidworks), origins for parts are not quite as critical since there are multiple parts in a single file. For FRC CAD, the purpose of origin is two fold:
1. We must have the same origin point across all part studios and assemblies so that the master sketch origin is respected.
2. To unify the robot CAD and robot software origin point. By having the same origin, the robot can be seamlessly exported to AdvantageScope and Camera transformations more easily measured measured. 

Although definitions may vary from team to team, the origin of an FRC robot is typically defined as the ***center of the drivebase, on floor level***.

In the following sections, we introduce a few different methods of locating an origin.

## Origin Cube Method
The origin cube Featurescript allows us to insert a 2"x2"x2" transparent cube at the origin of the part studio. The cube also has a mate connector for the origin. It also allows the designer to optionally import a number of useful design constants (such as bolt hole sizes, common FRC dimensions, etc).

Compared to other methods like fixing, the origin cube is a more robust and parametric method of aligning origins. 

Link to Featurescript: 
<center> ![Origin Cube Feature](/img/design-standards/originCubeFeature.webp) *Inserting the Origin Cube feature.* </center>

### Origin Cube Workflow

To fully utilize origin cubes and master sketches, it is recommended to have separate part studios for the fixed group of components and the moving group of components of each mechanism. Take a slap down intake for example. Two part studios can exist, both referencing the same master sketch(s): one for the arm base and gearboxes, and one for the intake arm. The following three assemblies can then be formed: the base components assembly, the arm components assembly, and the top level intake assembly containing the first two assemblies. The base component and arm component assemblies are both rigid assemblies with their origin cubes mated to the assembly origin. That is, there are no moving components in either assembly. The top level intake assembly should then only include two mates: one to mate the origin cube of the base assembly to the origin of the top level assembly, and another revolute mate to enable the motion of the arm.

The full file tree will appear like so:

* Top Assembly: 0200-A-Intake
* Assembly: 0210-A-Intake Base
* Part Studio: 0210-Intake Base
* Assembly: 0220-A-Intake Arm
* Part Studio: 0220-Intake Arm

<details>
<summary>Images of example assembly</summary>
<br>

<span style="color:red">TODO: add examples of good and bad part origins</span>.

</details>

In order to create a more robust revolute mate for the pivot, we can create a mate connector in both part studios at the pivot point and attaching it to the origin cube. In the top level assembly, we then add a revolute mate between the two origin cube's mate connectors and optionally set angle limits. By referencing the master sketch for the pivot point, the mate becomes parametric to any changes in either part studio. In fact, there would not need to be *any* parts in either assembly for the pivot to work because the mate connectors are attached to the origin cubes.

It should be noted that the separation of the fixed components and moving components into two separate part studios is not strictly necessary. It is possible to model everything in a single part studio with a single origin cube. However, the parts will need to be inserted into separate sub assemblies, but the same origin cube can be utilized in both sub assembly.

This same method can work for any type of flexible mechanism including elevators and linkages.

For rigid mechanisms, only a single assembly and part studio is required.

Finally, in the top level robot assembly, we can mate all the fixed origin cubes to the origin to create the final robot assembly.

<details>
<summary>A video explanation is also available.</summary>
<br>

<span style="color:red">TODO: add video talking about origin cube</span>.

</details>

## Origin Mate Connector Method

