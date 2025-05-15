# Exercise 3: More Extrudes

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

    If you did the extrude like the instructions said, all the boxes probably merged into one giant piece.  
    In real life, you don't want parts fused together like this unless you meant to.

    > Can you find a way to use multiple extrudes to keep them separate?

    If you need to restart, here's a quick video showing how to delete your bad tubes:

    <iframe width="100%" height="400" src="https://www.youtube.com/embed/WIwax3SHSQU" frameborder="0" allowfullscreen></iframe>

---

## Example Solution

??? success "Click here after fixing your tube in the above activity"

    Doing four separate extrudes manually is way too much work.

    Here's the faster way:
    - Delete your old extrudes.
    - Use the **Extrude Individual** feature script you installed in Stage 0.
    - (Hit **Alt+C** and type `"extrude individual"` if you can't find it.)

    Using Extrude Individual lets you extrude multiple shapes individually in one step!

    Also, if you click the "Bind" option inside Extrude Individual, you can force symmetry.

    <figure>
      <img src="/img/learning-course/stage1a/extrude-individual.webp" style="width:100%">
      <figcaption>Using "Bind" inside Extrude Individual.</figcaption>
    </figure>

---

# Exercise 3.1: Sketching Basics

In the last exercise, you extruded an existing sketch.  
Now, you're going to **make the sketch yourself**.

When we sketch, we use rectangles to represent box tubes in 2D, and use **dimensions** and **constraints** to lock everything into place.

📺 Follow along with the video:

<iframe width="100%" height="400" src="https://www.youtube.com/embed/xFm_EC-hl8o" frameborder="0" allowfullscreen></iframe>

---

## Key Sketching Points

!!! tip "Sketching Fundamentals"

    - **Dimensions** control distances (like making a rectangle exactly 5 inches wide).
    - **Constraints** define relationships (like locking a rectangle edge to another).
    - **Yellow dotted lines** show automatic constraints — use them!
    - **The Origin** is your anchor. Attach sketches to the origin whenever possible.
    - **Blue is bad** — a blue sketch means it's not fully defined yet. Everything should turn black.
    - **Less is better** — use the fewest dimensions necessary to fully lock down your design.

After watching the video, open Exercise 3 in Onshape.  
Create a flat sketch, extrude the shapes, and turn them into tubes.

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
Try to only use **one new dimension** total.

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

    <iframe width="100%" height="400" src="https://www.youtube.com/embed/-H2Lds8F34Q" frameborder="0" allowfullscreen></iframe>

    Compare your approach to the video.  
    What did you do differently?  
    How would you avoid mistakes like that next time?

---

## When You're Ready

[Continue to Exercise 4](section1-exercise4.md){ .md-button .md-button--primary }
