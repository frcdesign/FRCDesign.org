# Exercise 5: Building a Box Superstructure

Although we have drivetrain frames, we can make frames on top of the robot using box tube to hold other parts of a robot.


<figure style="margin-bottom: 2rem;">
  <img src="/img/learning-course/stage1a/exercise-5-973-example.webp" style="width:80%">
  <figcaption>973’s superstructure</figcaption>
</figure>

<figure>
  <img src="/img/learning-course/stage1a/exercise5-frame.webp" style="width:80%">
  <figcaption>Box superstructure CAD example.</figcaption>
</figure>

---

### Instructions:

1. To properly plan this out, we must create a side layout sketch (The one you used before). 
Start by inserting the **origin cube feature script** that you added in stage 0. Remember you can look things up using alt + c! 
2. Make a new sketch, and select the “right” plane and copy this sketch. Figure out the constraints you need yourself to replicate it perfectly.


<figure>
  <img src="/img/learning-course/stage1a/exercise5-frame-sketch.webp" style="width:100%">
  <figcaption>Box superstructure sketch</figcaption>
</figure>

!!! info 

    The wheels are the 1.75-inch blocks on the corners of the tube. If that's the case, where is the origin placed in the side layout sketch? Why do you think it's placed there? 
    Imagine if you looked at the robot in real life to the side.

Once you finish, create the swerve drivetrain frame in your part studio according to what you remember from the last exercise. (Remember to select the mate connector!) (If you struggle, refer to the previous video after trying) 

Let’s make this drivetrain a square. How would you approach your top sketch to avoid using any unnecessary dimensions? You should only need to define your swerve gap, the distance between your cross tubes (8 inches), and your tube offset.


??? hint

    What length is already defined/constrained? Can you use the equal constraint? 



### Making the Box Frame:
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
