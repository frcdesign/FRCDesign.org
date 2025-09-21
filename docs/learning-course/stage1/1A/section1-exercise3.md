# 1A: Onshape Fundamentals - Section 1
## Exercise 3: More Extrudes

In this exercise, you'll extrude four rectangles by 50mm symmetrically — and turn them into tubes.  
Use just one extrude feature. What happens?

<figure>
  <img src="/img/learning-course/stage1a/exercise3-rectangles.webp" style="width:70%">
  <figcaption>Starting setup with four rectangles.</figcaption>
</figure>

Don't forget: use the Tube Converter after extruding.

---

??? question "Looks a bit weird? Click here after trying it."

    If you followed the instructions and used a single extrude, all four rectangles probably merged into one big block.
    In real life, you don't want parts fused together like this unless you meant to.

    > Can you figure out how to extrude them **individually** to keep them separate?

    If you need to restart, here's a quick video showing how to delete your bad tubes:

    <iframe width="100%" height="400" src="https://www.youtube.com/embed/2Jzb1Xr6NBE" frameborder="0" allowfullscreen></iframe>

---

??? success "Click Here if you fixed your extrude."

    Manually doing four extrudes is tedious. There's a better way!

    - Delete your old extrudes.

    - Use the `Extrude Individual` Featurescript you added in [required course tools](../../course-setup/required-course-tools/featurescripts.md){:target="_blank"}.
    - (Hit `Alt+C` and search "extrude individual" if needed.)

    This tool lets you extrude multiple sketch regions separately, all in one step.

    Also, if you click the "Symmetric" option inside Extrude Individual, you can force symmetry.

    <figure>
      <img src="/img/learning-course/stage1a/extrude-individual.webp" style="width:90%">
      <figcaption>Using "Symmetric" inside Extrude Individual.</figcaption>
    </figure>

---

## Exercise 3.1: Sketching Basics

In the last exercise, you extruded an existing sketch. Now it's your turn to **create the sketch yourself**.

When we sketch, we use rectangles to represent box tubes in 2D, and use **dimensions** and **constraints** to lock everything into place.


Follow along with the video below to practice sketching fundamentals in Onshape.

<br>

<figure>
    <iframe width="768" height="432" src="https://www.youtube.com/embed/ftbpbvuZklc" frameborder="0" allowfullscreen></iframe>
</figure>

<br>

!!! tip "Key Sketching Points"

    - **Dimensions** control distances (like making a rectangle exactly 5 inches wide).
    - **Constraints** define relationships (like locking a rectangle edge to another).
    - **Yellow dotted lines** show automatic constraints — use them!
    - **The Origin** is your anchor. Attach sketches to the origin whenever possible.
    - **Blue is bad** — a blue sketch means it's not fully defined yet. Everything should turn black.
    - **Less is better** — use the fewest dimensions necessary to fully lock down your design.

---

### What You Learned

- How to extrude multiple tubes separately
- How to create and constrain a sketch
- How to make rectangles properly
- How to use basic dimensions and relationships
- How to mirror using construction lines

---

## Exercise 3.2: Adding Rails

<figure>
  <img src="/img/learning-course/stage1a/3-2-sketch.webp" style="width:100%">
  <figcaption>Edit this sketch</figcaption>
</figure>


Now let's apply this to the robot.

Open the Top Tube Sketch in the Exercise 3.2 part studio and **add two cross tubes** that are **200mm part**.  

!!! Tip
    Double-click the sketch in the feature tree to edit it.

Draw the new rails yourself. Only use **one new dimension** total.

The only numbers you should see:

- 108mm (gap between modules)
- 25mm (tube width)
- 400mm (distance between cross rails)

<figure>
  <img src="/img/learning-course/stage1a/drivetrain-crossrail-sketch2.webp" style="width:90%">
  <figcaption>Final cross rail sketch setup.</figcaption>
</figure>

---

### Check Your Work

??? info "Click here after you finish your sketch"

    Here's an optimized way to sketch it:

    <iframe width="100%" height="400" src="https://www.youtube.com/embed/ktKuSFVV10U" frameborder="0" allowfullscreen></iframe>

    Compare your approach to the video.  
    > What did you do differently?  
    > How would you avoid mistakes like that next time?

<br>

After you're done checking your work and reviewing your approach, move on to the next exercise.

<br>
