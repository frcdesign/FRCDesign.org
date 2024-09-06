# 1A: Onshape Fundamentals

## Assemblies

Assemblies are where parts designed in the part studio get assembled together. This is where you truly define the position and motion of all the different parts of something. 

### Learning Center Course

**Complete the following Onshape Learning Course:**

- The [Onshape Assemblies](https://learn.onshape.com/courses/fundamentals-onshape-assemblies "Onshape Assemblies Onshape Learning Course"){:target="_blank"} learning course introduces assemblies, mating parts together, and other useful assembly concepts.

### Assembly Tools

As was introduced in the Onshape learning tutorials, when parts are inserted into an assembly, they free float. We can utilize a number of different assembly tools to constrain the motion of all the parts:

- **`Group`**: Restricts the relative motion between a group of parts
- **`Fix`**: Locks a part in place within the assembly (not recommended as it's not parametric)
- **`Mates`**: Tools to constrain the degrees of freedom between parts using "mate connectors." These connectors are automatically generated or manually created coordinate systems on parts. You can align the axes and apply offsets in any direction or rotation. Different mates constrain different degrees of freedom. Here are three commonly used mates:
    - `Fasten`: Prevents any movement between two mate connectors, such as a bolt in a hole
    - `Revolute`: Allows rotational movement about the z-axis between two mate connectors (e.g. an arm pivot)
    - `Slider`: Enables linear movement along the z-axis between two mate connectors (e.g. an elevator)

!!! Example "Example of a Fasten Mate"
    <center>
    <figure>
      <video width="1920" controls>
        <source src="\img\learning-course\stage1a\1a-fasten.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>Using a fasten mate to secure a gusset to a tube.</figcaption>
    </figure>
    </center>

### Best Practices

The best practices for constraining an assembly, along with other assembly tools like replicate, pattern, and standard content, will be learned through projects and described in more detail in later stages. They are also outlined in the [assembly best practices](../../best-practices/assembly-setup.md "Assembly Best Practices Page"){:target="_blank"} page.

!!! Warning "<span style="font-size: 0.8rem !important;">**DO NOT MOVE PAST THIS POINT UNTIL YOU HAVE COMPLETED THE LEARNING COURSE ABOVE**</span>"

<br>