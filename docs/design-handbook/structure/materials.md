# Materials

Polycarbonate plastic is used in high impact applications such as subsystems that are exposed beyond the robot frame perimeter. Typically 1/4" thickness is used. 1/8 or 1/16" polycarbonate can be used for dust covers, sponsor panels, etc - it will almost never shatter and looks great.

!!! Tip
    "Smoked" or "tinted" polycarbonate can provide a more aesthetic look than clear. While making smoked polycarbonate is difficult, making frosted is easy! 30 seconds of sanding with an orbital sander using 240 grit will give the material a nice, glassy finish.

1/8, 3/16, and 1/4 aluminum stock are generally used for gussets and plates that have to be stiffer than plastic could provide. Avoid using use these materials in applications where they will be exposed beyond the robot frame, as they are not as impact-resistant as plastics and can easily bend, or fail catastrophically. 6061-T6 is the most common alloy, but 7075 is sometimes used and has higher yield strength.

!!! Note
    Make sure to check your supplier's thickness and tolerance for each material. Sometimes something marketed as in imperial measurements is actually manufactured to fit metric tolerances. For instance: 1/4" polycarb is actually sometimes manufactured as 6mm, which is 14 thousandths of an inch off of 1/4in. Account for these actual stock measurements when designing to make sure things end up fitting together!

## Pocketing and internal features

Pocketing is used to reduce weight from high-thickness, high density materials such as 3/16 or 1/4 aluminum. While thinner aluminum and plastics can also be pocketed, this is less common, and higher risk.

!!! Tip
    Pocketing always happens last. **Get design approval before pocketing**! Use [offset driven design](https://www.youtube.com/watch?v=TT_QmZoUwG8) so your plates look decent **before** pocketing.

When pocketing, use the [part lighten featurescript](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d).

- Tool radius must be ≥0.125 the radius of the cutting tool you use on your CNC, typically 0.125
- Strut thickness is usually 0.2 for 1/4 inch aluminum, and cut thru-all - but this depends on load and other factors

<br>