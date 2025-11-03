# Structure

A guide on creating robust and versatile robot structures. Covers different materials, techniques, and COTS components.

<!-- Add round tube, rectangular tube, thin vs thick wall tube -->

## Box Tube

**Coming Soon**

### Tube Plugs

Tube plugs are metal inserts that go into the ends of box tube that allow you to fasten tubes together without the use of gussets. Combining tube plugs with crush blocks provides a simple and strong connection between tubes. Tube plugs find a major use in modern elevator designs due to how much they simplify the design process. By not having to worry about bearing blocks interfering with gussets, you massively cut down on design complexity while also cutting part count and robot cost. When bolting tube plugs to the tube you typically dont need to use all 8 available bolts, with 2-4 being acceptable for most use cases.

!!! Note
Tube plugs are made to fit into tubes of 1/8" wall thickness. For tube with thinner walls you can use a plastic sleeve (possibly 3D-printed) on the outside of the tube plug to fill the gap with no strength loss.

!!! Info "Important"
When using tube plugs, well-toleranced holes relative to the end of the tube are required to make a strong connection between the tubes.

<center markdown>![tube plug](/img/best-practices/tube-plug.webp){width=50%}</center>

### Crush Blocks

Crush blocks are common in modern FRC due to how frequently used thin-walled box tubing is. The main purpose of crush blocks is to prevent forces from buckling the thin wall of the tube. This is very easy to do by simply overtightening a bolt on the tube. Thus, crush blocks enable you to tighten the bolts more than you would without having a crush block. This stiffens the connection and the tube as a whole.

!!! Note
Crush blocks can be made of any material, but 3D printing them is by far the simplest method of manufacturing for crush blocks. Just make sure to account for printer tolerances. Crush blocks shouldn't be too loose, but you also don't want to have to hammer them in.

<center markdown>![simplest_crush](/img/best-practices/simplest-crush.webp){width=25%}</center>
Above is the simplest form of a crush block: a piece of plastic that fills the empty space within the tube with some holes for bolts to go through. For a crush block at the end of a tube, you can include a flange to aide in alignment with the holes in the tube. Crush blocks may not be ideal for use in the middle of long tubes, since they would be hard to install and service; in these places, you can add an extra 1/16" plate on the outside of the tube to help spread the load of tightened bolts, functionally serving as a large washer. For additional strength, consider increasing the number of walls to 4-6 when 3D-printing.

<br>
