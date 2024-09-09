# 2D: Slapdown Intake

## Assembly

Just like the dead axle pivot, this subsystem contains a static part and a moving part. Again, we want to separate them into rigid (no movement) assemblies, then combine them at the top level. 

### Base Assembly

Create an assembly for the static parts, insert the parts and origin cube from the part studio with the green checkmark, and group them together. Fasten the origin cube to the origin. Add the rest of the parts from the part studio, MKCAD, and standard content, using replicate and patterns when you can. 

<figure>
    <img src="/img/learning-course/stage2-slapdown/staticAssembly.webp" width="70%">
    <figcaption>Finished Static Assembly</figcaption>
</figure>

### Arm Assembly

Create an assembly for the intake arms and do the same thing as above to complete the assembly and make it rigid. For the rollers, insert them from the [Configurable Rollers Document](https://cad.onshape.com/documents/b75886a5660c38eee7d50e47/w/58faeca16d5b2008a9485b5c/e/6274f59b451ed6222cd7523d "Configurable Rollers Onshape Document"){:target="_blank"}.

<figure>
    <img src="/img/learning-course/stage2-slapdown/intakeArms.webp" width="70%">
    <figcaption>Finished Intake Arms Assembly</figcaption>
</figure>

### Top Level Assembly 

Now create a top level assembly and insert the static assembly (fasten to the origin) and intake arm assembly. Create a revolute mate between the mate connectors from the origin cubes in both assemblies and add a limit to it. This completes the slapdown intake assembly.

<figure>
    <img src="/img/learning-course/stage2-slapdown/intakeTopLevel.webp" width="70%">
    <figcaption>Finished Top Level Intake Assembly</figcaption>
</figure>

<br>