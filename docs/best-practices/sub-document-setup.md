---
title: Best Practices
description: The best practices to follow with organizing your mechanism documents in Onshape.
---

# Sub-Document Setup

Each subsystem document should have at least one part studio and one assembly associated with it. 

The Stage 2A Basic Shooter is a simple subsystem with no moving parts. This contains only a part studio and a rigid assembly.

<center>[Stage 2A - Basic Shooter](https://cad.onshape.com/documents/8f093edaad44b5702e92ddd9/w/fefbb7a7af099fc237c1513a/e/84d7075719d34c35b3be9410 "Stage 2A Basic Shooter Onshape Document"){:target="_blank" .md-button .md-button--primary}</center>

<center><img src="/img/best-practices/shooterAssembly.webp" style="border:5px solid #ADADAD"></center>

### Subsystems with Multiple Degrees of Freedom

You may want to split subsystems with multiple degrees of freedom into multiple rigid assemblies. Each separate moving part of the subsystem should have a 'rigid' assembly (no degrees of freedom allowed for any part), while the top-level subsystem assembly only defines the motion between them. 

!!! Note
    A rigid assembly, when inserted, is treated as a solid body with no mates calculated. It decreases load time in top-level assemblies greatly. You will learn how to integrate the origin cube into this system for easy parametric mates in [assembly best practices](assembly-setup.md).

For example, you could split an elevator document into one part studio and corresponding rigid assembly for each stage. The top-level elevator assembly would thus include each of the stage subassemblies within it and the slider mates.


The Stage 2C Slapdown Intake is a subsystem with a static portion and a pivoting portion. Functionally, this contains a part studio, a static assembly for the gearboxes and pivot, a rigid assembly for the arms and rollers, and a top-level assembly combining the two subassemblies.

<center>[Stage 2C - Slapdown Intake](https://cad.onshape.com/documents/17302d787e092ce11015f7ee/w/f7cf5c02c7655f0328a3a74a/e/f1456325e0175c4c081008c2 "Stage 2C Slapdown Intake Onshape Document"){:target="_blank" .md-button .md-button--primary}</center>

<center><img src="/img/best-practices/subassembly.webp" style="border:5px solid #ADADAD"></center>

The Stage 2D Cascade Elevator is a subsystem with a static portion and two subassemblies that slide linearly. This contains a part studio, a static frame/gearbox assembly, assemblies for the first stage and carriage, and a top-level assembly combining the 3 subassemblies with slider mates.

<center>[Stage 2D Cascade Elevator](https://cad.onshape.com/documents/da5aef9e6bf6e869f4a51a45/w/5a0f4a3426876db0ba214277/e/f8fd8133abcb12800eacb5d1 "Stage 2D Cascade Elevator Onshape Document"){:target="_blank" .md-button .md-button--primary}</center>

<center><img src="/img/best-practices/elevatorAssembly.webp" style="border:5px solid #ADADAD"></center>

<br>
