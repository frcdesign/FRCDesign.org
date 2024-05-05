<style>
.right{
    float:right;
}

.left{
    float:left;
}
</style>

# Assembly Best Practices

<span class="left">[< Feature Tree Best Practices](feature-tree-setup.md)</span> 
<br>


Assuming you have already named your parts and organized your work within the rest of the document, creating a well-organized assembly is very straightforward. 

## Process for Inserting Parts

1. Add a mate connector to one of your rigid parts on the origin in your part studio
2. Insert the whole part studio with the green checkbox so the origin is in the same place
3. Use the "group" tool on all parts that don't move
4. Fasten the mate connector to the origin
5. Duplicate and fasten any duplicate parts

This is a fast and parametric way of putting together an assembly, as opposed to using mates to constrain all the parts that were already in the correct place.

!!! Tip
    As you add more parts in the part studio, you can insert them individually into the assembly with the green checkmark, double click on the initial group, and add the part to the group to avoid mating it. This means that new part will always stay in the same place relative to where it was designed in the part studio.

Make sure you sort the instances in your assembly into folders (i.e. tubes, swerve modules).

## Other Best Practices

The first advice is to minimize primitives in your assembly. Primitives are kinda like the number of triangles used to render the mesh of the object, or in more simple terms, it's a measure of how complex the object is and how hard it is for Onshape to render. The more primitives there are, the more laggy your assembly will be.

Use [simplified models](https://www.frcdesign.org/simplified/) wherever possible to minimize primitives: electronics, swerve modules, motors, etc. Some of these are added to MKCAD as well.

<details>
<summary>Minimize Primitives</summary>
  <figure class="video_container">
    <video controls="true" allowfullscreen="true" poster="../../../../img/design-standards/minimizePrimitives.webp">
      <source src="../../../../img/design-standards/minimizePrimitives.webm" type="video/webm">
    </video>
  </figure>
</details>

Other things to keep in mind:

- Import COTS parts from MKCAD
- Use the **replicate tool** for adding hardware! You should only need to import one of each type
- Minimize the number of mates you use; this lowers the solve time
- Stay organized with folders

See a well-organized assembly here:

![](/img/design-standards/assembly.png)

<br>
<span class="left">[< Feature Tree Best Practices](feature-tree-setup.md)</span>
<br>
<br>