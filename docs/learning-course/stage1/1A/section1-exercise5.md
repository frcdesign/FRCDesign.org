# 1A: Onshape Fundamentals
## Exercise 5: Building a Box Superstructure
### Introduction

Frames made out of box tube can added to the top of a drivetrain for extra mounting for more parts of subsystems, like a shooter or an arm.

<figure style="margin-bottom: 2rem;">
  <img src="/img/learning-course/stage1a/exercise-5-973-example.webp" style="width:60%; border:5px solid #ADADAD">
  <figcaption>973’s 2022 Superstructure</figcaption>
</figure>


In this exercise we'll be adding a simple box tube frame to the drivetrain you made previously.

<figure>
  <img src="/img/learning-course/stage1a/exercise5-frame.webp" style="width:80%">
  <figcaption>Final Box Tube Frame</figcaption>
</figure>

---

### Layout Sketch and Drivetrain

1. To properly plan this out, we must create a side layout sketch (the used previously in Exercise 5). 
2. Start by inserting the **origin cube feature script** that you added in [required course tools](../../course-setup/required-course-tools/featurescripts.md){:target="_blank"}. Remember you can look things up using `Alt + C`! 
3. Make a new sketch, select the `right plane`, and start copying this sketch. Figure out the constraints you need yourself to replicate it perfectly.


    <figure>
      <img src="/img/learning-course/stage1a/exercise5-frame-sketch.webp" style="width:100%">
      <figcaption>Box superstructure sketch</figcaption>
    </figure>

    !!! Info "Origin Placement"
        The wheels are the 1.75-inch blocks on the corners of the tube. If that's the case, where is the origin placed in the side layout sketch? Why do you think it's placed there? Imagine if you looked at the robot in real life to the side.

4. After the side layout sketch is done, create the swerve drivetrain frame in your part studio according to what you remember from the last exercise. (Remember to select the mate connector!) 

    !!! Tip
        If you struggle, refer to the previous video after trying

    !!! Info "Design Intent"
        Let’s make this drivetrain a square. How would you approach your top sketch to avoid using any unnecessary dimensions? You should only need to define your swerve gap, the distance between your cross tubes (8 inches), and your tube offset.

    ??? Hint
        What length is already defined/constrained? Can you use the equal constraint? 



### Modeling the Frame
So far, sketches have been created on default planes and mate connectors. In order to model the box tube for the frame on top of the cross tubes, the sketch to create the tubes should be created on the face of the cross tube, because that's where you want that tube to be, even if the cross tube changes position. 

!!! Tip "Design Intent"
    This is called modeling with "design intent." There are many different ways to model something, but you can choose specific ways based on what your intent for a part or the overall design is. This can also help you avoid creative blocks and keep your CAD from creating errors when the design changes.

<figure>
  <img src="/img/learning-course/stage1a/side profile.webp" style="width:80%">
  <figcaption>Box superstructure sketch</figcaption>
</figure>

Watch a demonstration of this sketching technique below.
<figure>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/_b2Gf8IiEEA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</figure>

Now that you’ve seen a demonstration, **try to complete the box tube structure** by creating a sketch on the face of the cross tube and projecting lines from the layout sketch into the new sketch with the `use` tool.

### Requirements
- The box frame should be made using 0 new dimensions total, both in the sketch and the extrude
- Edit tube converter to use 1/16" thick walls and change “centered on tube” to “auto offset” 

!!! Warning "Tube Offsets"
    The distance between the edge of your tube and your hole differs for drivetrains and typical use. If you use "centered on tube" for your regular box tubes your hole spacing wont be correct. Only use “Centered on tube” for your drivetrain rails!

---

### Finishing Up

Once you finish, **take a 5-minute break**. 

After you come back, **try to improve or correct any mistakes you find**. Once you finish, compare your workflow with the solution. **What thought process led you to do something different?**


<center markdown>[Solution Document](https://cad.onshape.com/documents/5f1057b0e7579ff9dd5811fe/w/4c6a1a1d9747b8ea76b238a3/e/b89eed09a1d075135ee83667){ .md-button .md-button--primary }</center>

Follow the short video below to learn how to rename your features, then rename the sketches and features in your part studio. Moving forward, we want to **always name our sketches and features**.

<figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ELdwPyFnm4Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</figure>

<br>

After you're done renaming your features, move on to the next exercise.

<br>