# 0D: Theory

As you probably know, CAD is a tool used to design parts digitally before they are manufactured. Most of our documentation will focus on FRC-specific CAD practice. However, to get started with Onshape, it’s important to understand some basic theory.

![purple_cylinder](../../../img/learning-course/stage0/theory/purplecyl.webp){align=right width=15%}
<hr style="height:5px; visibility:hidden;" />

Consider a basic 3D object, such as this cylinder. Every object you design in Onshape starts with a 2D sketch within a window called a part studio. Sketches are used to define a 2D profile, that is then manipulated with features. These features transform the 2D sketch, one change at a time, into a 3D object - by “extruding” or pulling the profile into 3D, revolving it around an axis, or by other methods. 

<br>

## Starting with a Sketch

<img src="/img/learning-course/stage0/theory/cross-light.webp#only-light" style="float:right; width:35%; margin-left:15px; margin-top:-30px">
<img src="/img/learning-course/stage0/theory/cross-dark.webp#only-dark" style="float:right; width:35%; margin-left:15px; margin-top:-30px">
If you wanted to create this cylinder in Onshape, we would start by representing its profile in a 2D sketch. So what would this sketch look like for a cylinder? If we take the section from the plane on the top of the cylinder. In Onshape this is called the “Top” plane. We can see that this sketch forms a circle. 

!!! Note
    We could represent the cylinder in other 2D ways, if we chose a different plane.


## Making the leap to 3D
![extrude](../../../img/learning-course/stage0/theory/extrude-light.webp#only-light){align=right width=40%} ![extrude](../../../img/learning-course/stage0/theory/extrude-dark.webp#only-dark){align=right width=40%}

While in the sketch, we define the nature of the circle - its position in space and its diameter. When we bring the sketch into 3D, these characteristics are maintained - determining the final diameter and position of the cylinder within the part studio. It is important to completely define the characteristics sketches so that the characteristics of the part being designed are not arbitrary. 

<br>
But how do we transform this defined sketch into a 3D object? By using *features*. In this case, an “extrude” feature is used to extend the profile of the sketch into 3D space.
Just like how we defined the sketch, we define the characteristics of this extrude. For example, we must specify a “depth” or final “height” for the cylinder. This is used to create the final geometry. There are many such settings we must specify when using features.

Using a side profile of the cylinder, you may also use the "revolve" feature to create the cylinder. There are usually different paths you can take to modeling something, and the one you choose depends on the intent of the design.

!!! Note
    These concepts, using sketches and features to model shapes, are universal across most parametric CAD software.

Additional sketches and features are used to add more complex geometry to parts or to create additional parts within the part studio.

!!! Note
    Features can also be used to modify existing geometry e.g. to round or chamfer corners; these don't require sketches.

<br>