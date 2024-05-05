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
As with many good practices in CAD, smart origins are another good practice to make future you's life easier. Intelligent origins allow designers to leverage default geometry (Front/Right/Top Planes, Origin Point) in their models. Good designers will utilize the default geometry for robust axes of symmetry and references. 

<!-- <details>
<summary>Examples of good and bad part origins</summary>
<br>
When modeling non-FRC parts, especially in non-multi-body workflow, origins are typically located on key features that have symmetry about them. The following examples help illustrate this.

<span style="color:red">TODO: add examples of good and bad part origins</span>.

</details> -->

However, it should be noted that with multi-body part modeling, as opposed to a typical 1 part per file workflow in Solidworks, origins for parts are not quite as critical since there are multiple parts in a single file. For FRC CAD, the purpose of origin is two fold:

1. TO use the same origin point across all part studios and assemblies in order to have the same origin as the master sketch.
2. To unify the robot CAD and robot software origin point. By having the same origin in CAD and code, the robot can be seamlessly exported to [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope) and camera transformations more easily measured. 

Although definitions may vary from team to team, the origin of an FRC robot is typically defined as ***the center of the drivebase, on floor level***.

In the following sections, a few different methods for creating origins are introduced.

## Origin Cube Method
The origin cube Featurescript inserts a 2"x2"x2" transparent cube at the origin of the part studio. The cube has a mate connector for the origin. There is also an option to import a number of useful design constants (bolt hole sizes, common FRC dimensions, etc).

Compared to other methods like fixing components, the origin cube is a more robust and parametric method of aligning origins.

In each sub assembly, the cube is mated to the origin. Then, in the top level robot assembly, all the origin cubes are mated together to create the final robot assembly.

[Link to Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/df3afdbec8d1356c2af15e4b?renderMode=0&uiState=6637caa6ccbcaa36badca03a)

<center> ![Origin Cube Feature](/img/design-standards/originCubeFeature.webp) *Inserting the Origin Cube feature.* </center>

### Utilizing Origin Cube for Flexible Assemblies

To utilize the full potential of origin cubes and master sketches, it is recommended to have separate part studios for the stationary group of components and the moving group of components of each mechanism. Take a slap down intake for example. Two part studios can exist, both referencing the same master sketch(s): one for the arm base and gearboxes, and one for the intake arm. The following three assemblies are then formed: the base components assembly, the arm components assembly, and the top level intake assembly containing the first two assemblies. The base component and arm component assemblies are both rigid assemblies with their respective origin cubes mated to their assembly origins. A rigid assembly is one where there are no moving components. The top level intake assembly should then only include two mates: a fasten to mate the origin cube of the base assembly to the origin, and a revolute mate to enable the motion of the arm.

The full file tree will appear like so:

* Top Assembly: 0200-A-Intake
* Assembly: 0210-A-Intake Base
* Part Studio: 0210-Intake Base
* Assembly: 0220-A-Intake Arm
* Part Studio: 0220-Intake Arm

<details>
<summary>Images of example assembly</summary>
<br>

<center><img src="/img/design-standards/0200-A.webp"><figcaption>Top Level Assembly: 0200-A-Intake. Notice that there is only two mates. The revolute is between the two intake pivot mate connectors, which are attached to the repective origin cubes.</figcaption></center>

<center><img src="/img/design-standards/0210-A.webp"><figcaption>Stationary Components Assembly: 0210-A-Intake Base. The components are group mated and the origin cube is fastened to the origin.</figcaption></center>

<center><img src="/img/design-standards/0210-PS.webp"><figcaption>Stationary Components PS: 0210-A-Intake Base. Notice the intake pivot mate connector, derived from the orange master sketch. </figcaption></center>

<center><img src="/img/design-standards/0220-A.webp"><figcaption>Moving Components Assembly: 0220-A-Intake Arm. The components are group mated and the origin cube is fastened to the origin.</figcaption></center>

<center><img src="/img/design-standards/0220-PS.webp"><figcaption>Moving Components PS: 0220-Intake Arm. Notice the intake pivot mate connector, derived from the orange master sketch.</figcaption></center>

</details>

In order to create a more robust revolute mate for the pivot, start by creating a mate connector in both part studios at the pivot point and attaching it to the origin cube. Then, in the top level assembly, add a revolute mate between the two origin cube's pivot mate connector and optionally set angle limits. By referencing the master sketch for the pivot point, the mate becomes parametric to any changes in either part studio. In fact, there would not need to be *any* parts in either assembly for the pivot to work because the mate connectors are attached to the origin cubes.

It should be noted that the separation of the stationary components and moving components into two part studios is not strictly necessary. It is possible to model everything in a single part studio with a single origin cube. However, the parts will still need to be inserted into separate sub assemblies, but the same origin cube can be utilized in both sub assemblies. A very simple example of this is given in the Origin Cube Featurescript document.

This same method can work for any type of flexible mechanism including elevators and linkages.

<!-- <details>
<summary>A video explanation is also available.</summary>
<br>

Coming Soon

</details> -->

## Origin Mate Connector Method
WIP

