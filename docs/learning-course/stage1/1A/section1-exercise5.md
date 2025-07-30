# 1A: Onshape Fundamentals
##Introduction

Now that we have a drivetrain frame made, a frame made out of box tube can added to the top of the drivetrain for extra mounting for more parts of subsystems, like a shooter or an arm.

<figure style="margin-bottom: 2rem;">
  <img src="/img/learning-course/stage1a/exercise-5-973-example.webp" style="width:60%; border:5px solid #ADADAD">
  <figcaption>973’s superstructure</figcaption>
</figure>

---

## Exercise 5: Building a Box Superstructure

<figure>
  <img src="/img/learning-course/stage1a/exercise5-frame.webp" style="width:80%">
</figure>

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
So far, sketches have been created on default planes and mate connectors. In order to model the box tube for the frame on top of the cross tubes, the sketch to create the tubes should be created on the face of the cross tube, because that helps preserve design intent

We need to find a way to model the box frame in the part studio. Since our box tubes get created on the sketch, we need to move our sketch to model the box structure on the robot.

We’ve been creating new sketches using a sketch's planes and mate connectors. 

There’s another way you can place sketches: by placing a sketch on the face of a tube

<figure>
  <img src="/img/learning-course/stage1a/side profile.webp" style="width:100%">
  <figcaption>Box superstructure sketch</figcaption>
</figure>

If you want to reference your layout sketch, you can use the use tool. 

### Video Demonstration

<iframe width="560" height="315" src="https://www.youtube.com/embed/_b2Gf8IiEEA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Now that you’ve seen a demonstration, try to complete the box tube structure using this concept. 
### Requirements
- You should be able to make your box frame using 0 new dimensions total. 
- For our Box frame, modify your tube converter to use 1/16 thick aluminum! Additionally, change “centered on tube” to “auto offset” 

!!! warning "Tube Offsets"
  The distance between the edge of your tube and your hole differs for drivetrains and typical use. If you use "centered on tube" for your regular box tubes your hole spacing wont be correct. Only use “Centered on tube” for your drivetrain rails!

### Finished?

Once you finish, take a 5-minute break and try to improve or correct your mistakes. Once you finish, compare your workflow with the solution. What thought process led you to do something different? 

Let’s also rename our features. Heres a tutorial on how to set this up. Moving forward, we want to always name our features.


### Renaming Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/ELdwPyFnm4Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

### Solution: 
[Solution](https://cad.onshape.com/documents/5f1057b0e7579ff9dd5811fe/w/4c6a1a1d9747b8ea76b238a3/e/b89eed09a1d075135ee83667){ .md-button .md-button--primary }


## When You are Done

[Continue to Exercise 6](section1-exercise6.md){ .md-button .md-button--primary }
