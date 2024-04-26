<style>
td {
  text-align: left !important;
  vertical-align: middle !important;
}
td, th , table{
   border: none!important;
   font-size: 0.8rem;
   padding:0 !important;
}

table tr:hover{
    background-color: transparent !important;
}

#purplecyl {
    padding-right: 2rem;
    width: 85%;
    height: auto;
}

</style>

# Stage 1A: Theory

As you probably know, CAD is a tool used to design parts digitally before they are manufactured. Most of our documentation will focus on FRC-specific CAD practice. However, to get started with Onshape, it’s important to understand some basic theory.

| | |
| :-: | :-: |
| Consider a basic 3D object, such as this cylinder. Every object you design in Onshape starts with a 2D sketch within a window called a part studio. Sketches are used to define a 2D profile, that is then manipulated with features. These features transform the 2D sketch, one change at a time, into a 3D object - by “extruding” or pulling the profile into 3D, revolving it around an axis, or by other methods. | ![purple_cylinder](../../../img/design-guide/stage1a/purplecyl.webp){#purplecyl} |

## Starting with a Sketch

| | |
| :-: | :-: |
| If you wanted to create this cylinder in Onshape, we would start by representing its profile in a 2D sketch. So what would this sketch look like for a cylinder? If we take the section from the plane on the top of the cylinder. In Onshape this is called the “Top” plane. We can see that this sketch forms a circle. | ![cross](../../../img/design-guide/stage1a/cross-light.webp#only-light) ![cross](../../../img/design-guide/stage1a/cross-dark.webp#only-dark) |

!!! note
    We could represent the cylinder in other 2D ways, if we chose a different plane.


## Making the leap to 3D
| | |
| :-: | :-: |
| While in the sketch, we define the nature of the circle - its position in space and its diameter. When we bring the sketch into 3D, these characteristics are maintained - determining the final diameter and position of the cylinder within the part studio. It is important to completely define the characteristics sketches so that the characteristics of the part being designed are not arbitrary. More on this later.| ![extrude](../../../img/design-guide/stage1a/extrude-light.webp#only-light) ![extrude](../../../img/design-guide/stage1a/extrude-dark.webp#only-dark) |

But how do we transform this defined sketch into a 3D object? By using features. In this case, an “extrude” feature is used to extend the profile of the sketch into 3D space.
Just like how we defined the sketch, we define the characteristics of this extrude. For example, we must specify a “depth” or final “height” for the cylinder. This is used to create the final geometry. There are many such settings we must specify when using features.

We can always add additional sketches and features to add more complex geometry to our parts, or to create additional parts within the part studio. We can also use features that don’t require a sketch, to round or chamfer corners or add specific geometry. 

These are the fundamentals of basic part design in Onshape.

## To recap:

- Create a new sketch within a new part studio
- Define the sketch with constraints
- Transform the sketch into a 3D object with specified features
- Manipulate the part with additional features 
- Repeat these steps until the part is complete

Remember: One “part studio” can have multiple, even many different parts. We won’t focus on it for now, but keep it in mind!

Now that you understand the fundamentals of CAD, It’s important to learn how to use the sketching tools and part design features in Onshape. Good luck!

## Onshape Courses
Please complete these courses before proceeding.

[Introduction to Sketching Course](https://learn.onshape.com/courses/introduction-to-sketching)<br>
[Part Design Course](https://learn.onshape.com/courses/fundamentals-part-design-using-part-studios)

!!! tip
    Feel free to ask for help in the beginner channels in the DDS Discord Server.

After completing these courses its still best to practice before moving further. Here are a variety of parts you can model to practice your sketching and modeling skills. 

## CADvent Part Gallery
<figure markdown>
![](../../../img/design-guide/stage1a/cadvents/cadvent1.webp){data-gallery="cadvent" width=75% height=75%}
<figcaption>Drawings made by AndrewD8724</figcaption>
</figure>
![](../../../img/design-guide/stage1a/cadvents/cadvent2.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent3.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent4.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent5.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent6.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent7.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent8.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent9.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent10.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent11.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent12.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent13.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent14.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent15.webp){data-gallery="cadvent" hidden="hidden"}
![](../../../img/design-guide/stage1a/cadvents/cadvent16.webp){data-gallery="cadvent" hidden="hidden"}

Good job learning part design! It’s now time to build on this knowledge with a more fundamental understanding of the FRC design workflow.
