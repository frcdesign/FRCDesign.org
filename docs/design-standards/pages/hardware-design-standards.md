<style>
.right{
    float:right;
}

.left{
    float:left;
}
</style>

# Hardware Design Standards

<span class="left">[< Assembly Best Practices](../pages/assembly-setup.md)</span> 
<br>

## Materials

Polycarbonate plastic is used in high impact applications such as subsystems that are exposed beyond the robot frame perimeter. Typically 1/4" thickness is used. 1/8 or 1/16" polycarbonate can be used for dust covers, sponsor panels, etc - it will almost never shatter and looks great.

!!! Tip
    "Smoked" or "tinted" polycarbonate can provide a more aesthetic look than clear. While making smoked polycarbonate is difficult, making frosted is easy! 30 seconds of sanding with an orbital sander using 240 grit will give the material a nice, glassy finish.

1/8, 3/16, and 1/4 aluminum stock are generally used for gussets and plates that have to be stiffer than plastic could provide. Avoid using use these materials in applications where they will be exposed beyond the robot frame, as they are not as impact-resistant as plastics and can easily bend, or fail catastrophically. 6061-T6 is the most common alloy, but 7075 is sometimes used and has higher yield strength.

!!! Note
    Make sure to check your supplier's thickness and tolerance for each material. Sometimes something marketed as in imperial measurements is actually manufactured to fit metric tolerances. For instance: 1/4" polycarb is actually sometimes manufactured as 6mm, which is 14 thousandths of an inch off of 1/4in. Account for these actual stock measurements when designing to make sure things end up fitting together!

## Hardware

Modern FRC generally uses two different types of imperial hardware, #10-32 and 1/4-20. However, 10-32 is vastely preferrable, and with a bit of effort, we can make robots that use almost exclusively 10-32 hardware. In general:

- 10-32 is used for almost everything: retaining shafts, screwing into motors, superstructure, etc.
- 1/4-20 hardware is used for structural applications where more strength is required than #10 can provide. 

When designing around hardware, it is best to use the **hole tool**

- 10-32 hardware uses a hole diameter of **0.196 inches** for a standard fit
- 1/4-20 hardware uses a hole diameter of **0.257 inches** for a standard fit

## Pocketing and internal features

Pocketing is used to reduce weight from high-thickness, high density materials such as 3/16 or 1/4 aluminum. While thinner aluminum and plastics can also be pocketed, this is less common, and higher risk.

!!! Tip
    Pocketing always happens last. **Get design approval before pocketing**! Use [offset driven design](https://www.youtube.com/watch?v=TT_QmZoUwG8) so your plates look decent **before** pocketing.

When pocketing, use the [Vent featurescript ](https://cad.onshape.com/documents/702f94d6e4ffb0c64f611f87/v/71f9487be753d9eef9c3f73f/e/d55354e2782385e34e0395c4?jumpToIndex=1209)

- Tool radius must be ≥0.125 the radius of the cutting tool you use on your CNC, typically 0.125
- Strut thickness is usually 0.2 for 1/4 inch aluminum, and cut thru-all - but this depends on load and other factors

## Belts, chain, power transmission

In general, belts are used on higher speed, higher precision applications. Differeing belt "profiles" have advantages and disadvantages:

- HTD5: most common, high load, low efficiency
- GT2/3: less common, less load, more efficient at higher speed

!!! Important
    Hex bores on printed pulleys can easily round out. Make sure to use hex inserts from WCP or TTB to make sure this common failure mode cannot happen. Belts can also fall off - It's reccomended to use pulleys with oversize flanges for this reason.

    Configurable templates for pulleys that satisfy these requirements can be found on the [Configurables](soon) page.

Chain is used in applications where higher load is needed. Chain must be actively tensioned because it stretches over time. It also comes in sizes:

- "#25" chain: smaller, lower load
- "#35" chain: heavier, higher load

Read more about theese topics:

Coming soon

