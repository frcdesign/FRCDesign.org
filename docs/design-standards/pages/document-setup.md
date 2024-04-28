<style>
.right{
    float:right;
}

.left{
    float:left;
}
</style>

# Document Setup

<span class="left">[< CAD Best Practices: Why?](../index.md)</span> <span class="right">[Sub-Document Setup >](../pages/sub-document-setup.md)</span>
<br>

In General, an FRC robot is too complicated and has too many parts to be created entirely within a single document. Doing so is possible, but will result in bad loading times, and likely poor organization. 

To alleviate these challenges, we generally split FRC robots into several documents, each with an individual version number:

- "Concept" document: contains the mastersketch, which determines the overall architrcture and geometry for the robot, alongside the CrayonCAD
- Several "Subsystem" documents, which contain the part studios, subassemblies and top-level assembly for each subsystem, such as an Intake
- "Master Robot" document, which contains the top-level full robot assembly. This assembly is comprised of the top-level assembly from each of the subsystem documents.

To connect these documents to each other, we make use of several Onshape features:

- **Derive** feature: brings your mastersketch from the concept document into the subsystem document, so you can design your parts on top of it.
- **Import**: Subassemblies are imported from each subsystem document so they can be assembled in the master robot document.

Here is a diagram showing the full file structure:

![](../img/design-standards/docsetup2.webp)

*Blue: Derive, Red: Import*

!!! Note
    Sometimes the "master robot" document is combined with the "concept" document. In this case nothing really changes, the file strcture just becomes a sort of loop, and there is one less document.

You can see an example of this document structure here (note the combination of the framework and master documents)

![](../img/design-standards/docsetup3.png)

![](../img/design-standards/docsetup4.png)

