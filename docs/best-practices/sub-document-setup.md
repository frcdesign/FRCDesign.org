---
title: Best Practices
description: The best practices to follow with organizing your mechanism documents in Onshape.
---

# Sub-Document Setup

Each subsystem document should have at least one part studio and one assembly associated with it. 

!!! Info "Important"
    Never pattern or mirror parts in part studios that don't explicitly need to be patterned. Creating one of each part in the studio means you can simply duplicate it when assembling, and your part studio regeneration time will be greatly improved at no cost.

[Stage 2B - Basic Shooter](https://cad.onshape.com/documents/8f093edaad44b5702e92ddd9/w/fefbb7a7af099fc237c1513a/e/84d7075719d34c35b3be9410) is a simple subsystem with no moving parts. This contains only a part studio and a rigid assembly.

<center><img src="/img/best-practices/shooterAssembly.webp" style="border:5px solid #ADADAD"></center>

### Subsystems with Multiple Degrees of Freedom

You may want to split subsystems with multiple degrees of freedom into multiple rigid assemblies. Each separate moving part of the subsystem should have a 'rigid' assembly (no degrees of freedom allowed for any part), while the top-level subsystem assembly only defines the motion between them. 

!!! Note
    A rigid assembly, when inserted, is treated as a solid body with no mates calculated. It decreases load time in top-level assemblies greatly. You will learn how to integrate the origin cube into this system for easy parametric mates in [assembly best practices](assembly-setup.md).

For example, you could split an elevator document into one part studio and corresponding rigid assembly for each stage. The top-level elevator assembly would thus include each of the stage subassemblies within it and the slider mates.


[Stage 2D - Slapdown Intake](https://cad.onshape.com/documents/17302d787e092ce11015f7ee/w/f7cf5c02c7655f0328a3a74a/e/f1456325e0175c4c081008c2) is a subsystem with a static portion and a pivoting portion. Functionally, this contains a part studio, a static assembly for the gearboxes and pivot, a rigid assembly for the arms and rollers, and a top-level assembly combining the two subassemblies.

<center><img src="/img/best-practices/subassembly.webp" style="border:5px solid #ADADAD"></center>

<br>