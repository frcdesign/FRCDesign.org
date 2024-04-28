<style>
.right{
    float:right;
}

.left{
    float:left;
}
</style>

# Assembly Best Practices

<span class="left">[< Feature Tree Best Practices](5-feature-tree-setup.md)</span> <span class="right">[Hardware Design Standards >](7-hardware-design-standards.md)</span>
<br>

Assuming you have already named your parts and organized your work within the rest of the document, creating a well-organized assembly is very straightforward. Just make sure to:

- Use [simplifed models](https://www.frcdesign.org/simplified/) wherever possible: electronics, swerve modules, motors, etc.
- Import COTS parts from MkCAD
- Use the **replicate tool** for adding hardware! You should only need to import one of each type
- Minimize the number of mates you use; this lowers the solve time
- Stay organized with folders

See a well-organized assembly here:
![](/img/design-standards/assembly.png)