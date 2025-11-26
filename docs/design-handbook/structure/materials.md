# Materials

An overview of raw materials commonly found on FRC robots, including tips for handling them and use cases. This is specifically on materials used to make custom plates and parts, not necessarily COTS items. 

!!! Note
    For more information on materials used in 3D printing, like TPU or PLA, refer to the <a href="https://www.frcdesign.org/design-handbook/structure/intro-to-3d-printing/"target="_blank">Intro to 3D Printing</a> page for more information.

## Aluminum

Aluminum is one of the most versatile materials in FRC. It is both durable and easy to work with which means it's perfect for many applications. It's great for its cost; compared to other metals, it is relatively affordable. They are ideal for many applications where strength and structure are needed. In applications where this support isn't important, it may be more optimal to use a cheaper material like polycarbonate or to cut weight with SRPP. In addition, aluminum is not ideal for places where it extends beyond frame perimeter like intakes as it can easily bend or fail catastrophically. 

This section focuses on aluminum plates and blocks, however they are used everywhere in COTS and stock items like shafts, extrusions, etc. The thickness of the metal and type (6061 vs 7075) are important considerations as they each have different use cases. 

<figure>
    <img src="/img/design-handbook/materials/examplegusset.webp" style="width:50%">
    <figcaption>Example of gusset made out of aluminum. Credit: CTRE.</figcaption>
  </figure>

### Sheet Thickness

Aluminum sheets can come in many thicknesses. The following are common thicknesses, however consider them as more ranges than single values.

**1/16" or 0.090":** Such thin metal is almost exclusively used for supports, like gussets or bellypans. Easy to route and use, it is very helpful in many cases.

**1/8":** 1/8" aluminum can play a variety of roles, from structural pieces to gussets. It can be more beneficial than 1/4" material because of its lower weight, however in cases involving high loads and forces, 1/4" is preferred.

!!! Tip
    For outer frame tubes on a drivetrain, it is best practice that they are 1/8" rather than 1/16" because of the large forces they'd experience from robot collisions.

**1/4":** Best thickness for anything structural, where strength is needed (i.e. high laod pivots).

### Alloy

Although many types of aluminum alloys exist, the most commonly used in FRC is **6061-T6** followed by **7075**. 6061 is best because of its ability to be both strong and easy to machine with. For most applications, it works well. However, in applications where more strength to handle higher loads is wanted, 7075 aluminum can be helpful. For more information on alloys aside from the two discussed, visit <a href="https://www.allmetalsfab.com/understanding-aluminum-alloys/"target="_blank">this website</a> to learn more.

!!! Note
    7075 aluminum is used in many COTS items, notable solid hex shafts and gears. It is important to note the alloy on vendor websites if attemping to machine or modify COTS items. 

### Billet

Billet parts are blocks of metal that are machined through milling to remove part of it. They are usually made of 6061 aluminum. It is rare to see custom billet because of the difficulty in manufacturing for many teams, however they can be an important tool for many teams. Many COTS parts are made of billet material, such as tube plugs. 

<figure>
    <img src="/img/design-handbook/materials/coolbillet29102023.webp" style="width:50%">
    <figcaption>Billet part used on the end of 2910's 2023 telescoping tube. These parts can range wildly in complexity, and depends significantly on your team's capabilities.</figcaption>
</figure>

## Polycarbonate

Also known as Lexan, polycarbonate or "polycarb" is a very versatile and useful material used in applications where less strength is needed and where aluminum is overkill/not optimal. Polycarbonate plastic is used in high impact applications such as subsystems that are exposed beyond the robot frame perimeter. Typically 1/4" thickness is used. 1/8 or 1/16" polycarbonate can be used for dust covers, sponsor panels, etc. - it will almost never shatter, and looks great.

<figure>
    <img src="/img/design-handbook/materials/" style="width:50%">
    <figcaption></figcaption>
</figure>

!!! Warning
    Do not use locktite around polycarbonate! This can cause the plate to crack irreversibly. For bolts that are susceptible to vibrating out of plate, be sure to tighten them regularly and take care when assembling.

### Sheet Thickness

**1/32"-1/8":** Often used where strength is not important, such as in dust covers or sponsor plates. Can be great as a material for floors, for example the polycarbonate backing of shooters. 

**1/4":** Great for applications where more strength is needed. For maximum strength, switching to aluminum instead may be better. 

!!! Tip
    "Smoked" or "tinted" polycarbonate can provide a more aesthetic look than clear. While making smoked polycarbonate is difficult, making frosted is easy! 30 seconds of sanding with an orbital sander using 240 grit will give the material a nice, glassy finish.


!!! Note
    Make sure to check your supplier's thickness and tolerance for each material. Sometimes, something marketed as in imperial measurements is actually manufactured to fit metric tolerances. For instance: 1/4" polycarbonate is actually sometimes manufactured as 6mm, which is 14 thousandths of an inch off of 1/4in. Account for these actual stock measurements when designing to make sure things end up fitting together!

## Steel

Steel is a useful alternative to aluminum when maximum strength is needed or for ballast. Some teams may opt to have a steel bellypan instead of aluminum, for example, in order to lower their center of gravity. It is also used in some COTS items like steel hex axles or bolts. Custom machined steel is rare in FRC because of how difficult it is to machine with (steel saws and sanders are needed to work with steel). In almost all cases, teams will have to reach out to an outside manufacturer in order to make it. 

## Self-Reinforced Polypropylene (SRPP)

SRPP is an increasingly popular material in FRC for its weight savings and strength compared to polycarbonate. It is a less toxic compound used in plates, and it is composed of fibers woven into a "fabric" (similar to carbon fiber). It is both stiffer and significantly more impact resistant than polycarbonate. Plus, it also weighs much less, which can be hugely important for weight savings. It is a great material for mechanisms that are often outside of frame perimeter, like intakes; where polycarbonate might be used, SRPP can often be slotted in.

The major drawback is its expense: it costs $250 a sheet compared to $80 for polycarbonate. In addition, machining it is slightly different than polycarbonate. Laser cutting is the preferred method for clean, precise cuts. However, it can also be routed with a CNC machine, though extra precaution should be taken. It is fine to cut sheets, i.e. with a table saw. More information on manufacturing can be found at a vendor's website, for example <a href="https://docs.revrobotics.com/ion-build/structure/maxcomposite"target="_blank">REV Robotics guide for SRPP</a>.

<figure>
    <img src="/img/design-handbook/materials/srppexample.webp" style="width:50%">
    <figcaption>SRPP sheet. Credit: REV Robotics.</figcaption>
</figure>

!!! Tip
    SRPP is resistant to many chemicals, including locktite! This means you can locktite bolts around SRPP, unlike polycarbonate, with no issues. 

## Carbon Fiber

**Coming Soon**

## Wood



<br>
