# Exercise 1: Plates

## What Are Plates?

We’ve been making a lot of box tubes that float in the air. How do we attach them? 

We can do this through plates.
Plates have two functions:

1. Connect tubes precisely the way you want. 
2. Precisely place other objects of the robot in the exact spot you want them.

<figure>
  <img src="/img/learning-course/stage1a/9442-plate.webp" style="width:100%">
  <figcaption>9442's Robot Plate.</figcaption>
</figure>

<figure>
  <img src="/img/learning-course/stage1a/other-plate.webp" style="width:100%">
  <figcaption>Another Plate.</figcaption>
</figure>

---
### Background

Since your tubes are always in 0.5-inch increments, your plates allow you to connect uneven distances. 

What is a plate? A plate material around a hole or a set of holes. That is it. For example, we can make a plate with one hole by making a sketch of our hole, defining the hole size, then defining the material around it with another sketch.

Plates are composed of circles, arcs, and lines. Watch this video to get a primer on how a plate outline is made. (Do not follow along, just watch and absorb whatever you can)


<iframe width="100%" height="315" src="https://www.youtube.com/embed/0a5A_xZJ3sw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The tangent constraint allows us to create a tangent line or object to an arc or circle. Watch this video for a demonstration. This is important to “smooth” out our plate. We don’t want sharp edges!

## Your Task

We’ll make a plate that can hold two bearing holes. Bearings help reduce friction in shafts, but for now, just think of it as a big hole. (insert gif with rotating shaft in bearing pt 2) 

The holes in the sketch are already made for you, so we just need to outline. Watch this video to learn how to use the center point arc, line, and tangent constraint.

!!! info "Tip"

    Tip: holding shift turns off auto constraining, you may accidentally make one part of your arc horizontally or vertically constrained.
    You can also delete constraints by hovering over parts. 

### Complete?

After Finishing, delete your plate outline, and repeat these steps 2-3 times or until it feels boring and you can do it easily from memory. 

Try not to reference the video. It helps you remember! 

Open the workflow below once you have messed around to see if you are going about the same route:

??? Question "Workflow"
    After attempting, here's an example workflow:

    1. Identify the holes in the sketch.
    2. Create center point arcs based on each edge hole to define the material.
    3. Dimension the distance between the hole and the arc.
    4. Connect each point of the arc with lines, and repeat till the region is filled.
    5. Use the tangent constraint to smooth out the arcs
    
---

## When You're Ready

Continue to [Exercise 2: Plates Gussets](section2-exercise2.md).
