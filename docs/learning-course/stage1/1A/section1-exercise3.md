# 1A: Onshape Fundamentals
## Exercise 3: More Extrudes

## Extrude the Rectangles

In this exercise, you'll extrude four rectangles by two inches symmetrically — and turn them into tubes.  
Use just one extrude feature. What happens?

<figure>
  <img src="/img/learning-course/stage1a/exercise3-rectangles.webp" style="width:100%">
  <figcaption>Starting setup with four rectangles.</figcaption>
</figure>

Don't forget: use the Tube Converter after extruding.

---

## Looks a bit weird?

??? question "Click here after you try it"

    If you followed the instructions and used a single extrude, all four rectangles probably merged into one big block.
    In real life, you don't want parts fused together like this unless you meant to.

    > Can you figure out how to extrude them **individually** to keep them separate?

    If you need to restart, here's a quick video showing how to delete your bad tubes:

    <iframe width="100%" height="400" src="https://www.youtube.com/embed/2Jzb1Xr6NBE" frameborder="0" allowfullscreen></iframe>

---

## Example Solution

??? success "Click here if you fixed your extrude"

    manually doing four extrudes is tedious. There's a better way!

    - Delete your old extrudes.

    - Use the **Extrude Individual** Featurescript from Stage 0.
    - (Hit **Alt+C** and search `"extrude individual"` if needed.)

    This tool lets you extrude multiple sketch regions separately, all in one step.

    Also, if you click the "Symmetric" option inside Extrude Individual, you can force symmetry.

    <figure>
      <img src="/img/learning-course/stage1a/extrude-individual.webp" style="width:100%">
      <figcaption>Using "Symmetric" inside Extrude Individual.</figcaption>
    </figure>

---

# Exercise 3.1: Sketching Basics

In the last exercise, you extruded an existing sketch.  
Now its your turn to **create the sketch yourself**.

When we sketch, we use rectangles to represent box tubes in 2D, and use **dimensions** and **constraints** to lock everything into place.

Follow along with the video:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/ftbpbvuZklc" frameborder="0" allowfullscreen></iframe>

---

## Key Sketching Points

!!! tip "Sketching Fundamentals"

    - **Dimensions** control distances (like making a rectangle exactly 5 inches wide).
    - **Constraints** define relationships (like locking a rectangle edge to another).
    - **Yellow dotted lines** show automatic constraints — use them!
    - **The Origin** is your anchor. Attach sketches to the origin whenever possible.
    - **Blue is bad** — a blue sketch means it's not fully defined yet. Everything should turn black.
    - **Less is better** — use the fewest dimensions necessary to fully lock down your design.

## Todo:
---

## What You Learned

- How to extrude multiple tubes separately
- How to create and constrain a sketch
- How to make rectangles properly
- How to use basic dimensions and relationships
- How to mirror using construction lines

---

# Exercise 3.2: Adding Rails

<figure>
  <img src="/img/learning-course/stage1a/3-2-sketch.webp" style="width:100%">
  <figcaption>Edit this sketch</figcaption>
</figure>


Now let's apply this to the robot.

Open the drivetrain sketch and **add two cross tubes** that are **8 inches apart**.  
Double-click the sketch in the feature tree to edit it.

Draw the new rails yourself.  
Only use **one new dimension** total.

The only numbers you should see:
- 4.25 (gap between modules)
- 1 (tube width)
- 8 (distance between cross rails)

<figure>
  <img src="/img/learning-course/stage1a/drivetrain-crossrail-sketch2.webp" style="width:100%">
  <figcaption>Final cross rail sketch setup.</figcaption>
</figure>

---

## Check Your Work

??? info "Click here after you finish your sketch"

    Here's an optimized way to sketch it:

    <iframe width="100%" height="400" src="https://www.youtube.com/embed/ktKuSFVV10U" frameborder="0" allowfullscreen></iframe>

    Compare your approach to the video.  
    What did you do differently?  
    How would you avoid mistakes like that next time?

---

## When You're Ready

[Continue to Exercise 4](section1-exercise4.md){ .md-button .md-button--primary }
