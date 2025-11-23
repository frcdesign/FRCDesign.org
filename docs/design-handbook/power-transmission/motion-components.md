# Motion Components

A guide on bearings, bushings, and axles, including the mechanics behind transmission of torque through axles. This page also contains tips on how to manufacture and assemble these parts. 

## Bearings

Bearings are the most important and common type of motion component, used by virtually every team. The most common use of bearings is for allowing axles to spin freely with a low friction connection. They are incredibly important for making sure an axle can smoothly rotate. Bearings are recommended in low torque applications, but can handle very high speeds.

There are other applications of bearings, such as in eleavtor bearing blocks where they slide along a surface to allow for less friction, however this section is dedicated specifically for bearings' use in rotational systems. 

!!! Note 
    An axle on bearings is not a structural or rigid component, which means that it cannot support a structure, unlike a spacer bolted rigidly. 

<figure>
      <img src="/img/design-handbook/motion-components/bearing-context.png" style="width:70%">
      <figcaption>Flanged bearing used on rollers for 1678's 2024 robot.</figcaption>
</figure>

There are several types of bearing used in FRC®. Nearly all FRC bearings are ball bearings, meaning they spin using mini balls held in the structure of a bearing.

### Flanged Bearings

They are the most common types of bearings. They have a flange which allows them to securely mount onto plates, thus already supported on one side. They are used in a wide variety of applications like gearboxes, rollers, etc.

### Standard Bearings

They are very similar to flanged bearings, but they do not have  a flange. They are usually used in spaces where a flange will not fit or is not necessary. They can be used in much of the same applications as flanged bearings, however extra care is needed to mount them.

<figure>
      <img src="/img/design-handbook/motion-components/standard-bearing-context.png" style="width:50%">
      <figcaption>Standard bearing in gearbox. The plate is half pocketed so that the bearing doesn't fall out, and is retained by a custom axle.</figcaption>
</figure>

### Needle Bearings

Needle bearings are a special type of bearing which is much thinner than flanged and standard bearings. They can be used in spaces where there is not enough space for a normal bearing and are almost always used for round axles. As a result, they are a very common option to use with [dead axle rollers](link-url "https://www.frcdesign.org/learning-course/stage1/1C/exercise2/"){:target="_blank"} as they can be press fit into the end caps. 

<figure>
      <img src="/img/design-handbook/motion-components/1540needlebearing.png" style="width:70%">
      <figcaption>Needle bearing used in dead axle rollers for 1540's 2025 intake. Allows roller to spin around a rigid axle.</figcaption>
</figure>

### X-Contact

X-Contact bearings operate with completely different use cases and applications than typical ball bearings. They typically have a much larger diameter than most bearings. As a result, they are commonly used in swerve drives or turrets to allow free rotation of these systems. X-Contact bearings are also assembled differently compared to typical bearings.

<figure>
      <img src="/img/design-handbook/motion-components/x-contact-context.png" style="width:70%">
      <figcaption>X-Contact bearing in an MK4 swerve module. Allows wheel to rotate freely.</figcaption>
</figure>

<div style="display: flex; gap: 15px; align-items: flex-start;">
  <figure style="flex: 1;">
    <img src="/img/design-handbook/motion-components/JGKWXv2OdJCRBAJ8O1yNFD2TTZEuUdvi.webp" style="width:90%">
    <figcaption>X-Contact bearing setup. The ball is contacted on 4 points instead of 2 in standard bearings.</figcaption>
  </figure>

  <figure style="flex: 1;">
    <img src="/img/design-handbook/motion-components/TypeC.webp" style="width:90%">
    <figcaption>Standard ball bearing setup. Ball is contacted on 2 points vertically.</figcaption>
  </figure>
</div>

This setup allows X-Contact bearings to withstand much more [thrust](link-url "https://en.wikipedia.org/wiki/Thrust_bearing"){:target="_blank"} force than typical bearings, meaning it can withstand loads laterally rather than rotationally. This is very useful for places where a lot of weight is against the bearing vertically, such as in swerve modules where the bearings must be able to hold the entire weight of the robot. 

### Bushings

A common type of bearing used in FRC are bushings.  Bushing are often used for high torque, low speed applications, such as [dead axle pivots](link-url "https://www.frcdesign.org/learning-course/stage2/2B/introduction/"){:target="_blank}. They are much simpler than ball bearings; instead of using balls to allow for smooth roational movement, axles rotate simply on a greased surface. They usually have a flange but other types can be sourced from non-FRC vendors. 

<figure>
      <img src="/img/design-handbook/motion-components/citrus-bushing.png" style="width:50%">
      <figcaption>Bushing mounted to 1678 2024 shooter, which allows it to pivot freely around an axle.</figcaption>
</figure>

### Other Bearings

There are a wide variety of bearings with limited use in FRC, such as thrust bearings or linear bearings. These types of bearings usually have very specific use cases not relevant to FRC. More information about them can be found on [McMaster-Carr's website](link-url "https://www.mcmaster.com/products/bearings/"){:target="_blank"}, a common vendor in industry.

## Axles

Axles, also known as shafts, are often used to transmit torque in power transmission and facilitate rotational motion. They are one of the most important components in FRC and allow the assembly of everything from rollers and wheels to pivots and arms. There are many types of axles from many vendors, however they can be classified by **material**, **diameter**, and **profile** (i.e. round vs hex). It is critical to consider these variables when designing mechanisms as they can affect the end product immensely. 

<figure>
      <img src="/img/design-handbook/motion-components/axleExample.png" style="width:70%">
      <figcaption>Typical 1/2" rounded hex axle on two bearings, retained with bolts.</figcaption>
</figure>

### Material

Nearly all shafts are made from aluminum (7075/6061) or steel. Aluminum is typically the preferred material in all cases for its ease of manufacturing. 7075 Aluminum shafts can be stronger, though harder to cut and work with. 7075 shafts are often used in solid shafts, whereas 6061 is used in hollow shafts. In all, aluminum shafts are used for many applications such as rollers, gearboxes, etc.

Steel is useful when the shaft diameter must be smaller yet needs to transmit high torque, like in pivot systems and gearboxes. Steel also weighs significantly more than aluminum, which is necessary to take into account.

!!! Important
      Steel axles often require different manufacturing tools than aluminum axles. For assembly, it can be more difficult to slide wheels and other components onto a steel shaft than aluminum. As useful as it may be, be cautious of using it everywhere; it is not the end all be all.

### Diameter

The diameters of FRC shafts vary wildly. The majority vary from 3/8" diameter to 1" diameter, however it is possible to source even larger axles from vendors outside FRC.

The general rule of thumb is that the higher the torque and load, the larger the shaft should be. If too small of an axle is used, no matter the material, it may be susceptible to twisting under high loads. For large cantilevered arms, very wide 2"+ axles are helpful for stability and strength. On the other side, smaller axles can be useful in scenarios where strength isn't as much of an issue for weight savings. 

<figure>
      <img src="/img/design-handbook/motion-components/hexpivotfun.png" style="width:50%">
      <figcaption>Twisted steel hex axle, 1/2" diameter. Was used for pivoting a very large load.</figcaption>
</figure>

### Profile

There are many types of profiles. A common one used in FRC is the **hex profile**, which is useful for its ability to easily transmit rotational forces without any extra tools; gears, pulleys, and other power transmissions only need a hex bore to spin it. There are two types of hex shafts: rounded and standard. The difference is that the edges of the shaft are significantly chamfered in a rounded setup. 

This is in contrast to **round profiles**, where a notch/key is required in order to spin the axle. However, round profiles are especially helpful in dead axle systems where spinning the axle is not needed.

Other profiles include:

**MAXSpline/SplineXL:** REV/WCP brand. Similar to hex but can be used both for live axle and dead axle systems. Capable of transmitting large amounts of torque due to its large diameter.

**Churro/Hex-Lite:** AndyMark/WCP brand. Very similar to hex and works in a pinch but hex is the preferred option.

<figure>
      <img src="/img/design-handbook/motion-components/typesofshaftprofiles.png" style="width:90%">
      <figcaption>Various types of profiles. Left to right: Churro, Hex (standard), MAXSpline, Round (1")</figcaption>
</figure>

## Tips for Manufacturing and Assembly

This section lays out tips and common mishaps with motion components. It also talks about how to assemble bearings and shafts effectively.

### Bearings Retention

Most bearings can be press fit into metal parts, like flanged and needle. Other bearings may require special assembly to prevent from falling out, like standard bearings, where they must be retained by a plate. 

For bearings on polycarbonate or similarly bendy material, it is good practice to include proper bearing retention using "hats" which are bolted to the material and hold the bearing in place. This is needed due to the flexibility of polycarbonate, which may allow bearings to pop out, and is especially important if there are no spacers to properly support the polycarbonate plate. These hats can be bought by a vendor or custom 3D printed.

<figure>
      <img src="/img/design-handbook/motion-components/bearinghat1540.png" style="width:50%">
      <figcaption>3D printed bearing hat on 1540's 2025 end effector.</figcaption>
</figure>

### Shaft Retention

Shafts must always be retained so they don't slip out of bearings. There are several ways to achieve this.

**Bolt and Washer**

Tapping a shaft and screwing a bolt with a washer on is typically best practice. It ensures that a shaft is properly retained between bearings without taking up space, as was seen in the example image for axles. However, this requires that the shaft has a center bore/is hollow, so this solution may not work with all shafts. 

!!! Tip
      Locktite should be used to keep the bolt in place, but NEVER use locktite near polycarbonate! It can destroy the material and cause irreversible cracks.

**Shaft Collars**

Collars are a very quick and easy way to retain shafts. The benefit is that the length of the shaft does not have to be a defined length, unlike with bolt and washer, which makes it very useful for quick builds/prototypes. However, they are typically not best practice to use and should only be used if needed. In addition, they are almost exclusively used for hex and MAXSpline/SplineXL profiles.

<figure>
      <img src="/img/design-handbook/motion-components/lockcollarexample.png" style="width:50%">
      <figcaption>Shaft collar on 1/2" hex axle.</figcaption>
</figure>

**Clips and Rings**

Another way of retaining axles is using clips and rings. They are great practice to use, and may be more convenient than bolt; for round axles, they can be incredibly useful. However, they require certain machining capabilities like access to a lathe that not all teams possess. 

<figure>
      <img src="/img/design-handbook/motion-components/1540retainingring.png" style="width:50%">
      <figcaption>Groove on 1540's 2025 round axle for arm for holding a retaining ring.</figcaption>
</figure>

**Turned Down Axles**

Another way of retaining shafts is by physically cutting into the axle partially. This turned down part of the shaft sits in the bearing while the rest keeps the original profile. This retains a shaft without using other tools like bolts or collars, however it does require the ability to manufacture these parts, usually with a lathe. 

<figure>
      <img src="/img/design-handbook/motion-components/6328hexthing.png" style="width:50%">
      <figcaption>Custom hex axle on 6328's pivot gearbox, 2023. Note that the unaffected part of the hex axle holds the bearing in.</figcaption>
</figure>

!!! Note
      If using flanged bearings, ensure the flanges are pointing inward towards each other. With proper spacing on the axle, this allows both the axle and bearing to be retained properly.

### Shaft Retention with Dead Axles

Dead axles must be rigidly mounted to a part in order to be structural. For tapped shafts, they can just be bolted into a plate, but with other types of axles like round axles, it requires slightly more difficulty. Mounting can be done in many ways:

**COTS Plugs, Blocks, or Shaft Collars:** For MAXSpline/SplineXL systems, the typical way of mounting is using blocks and retaining with shaft collars. These are very vendor specific, for example WCP's billet plugs. For more information, visit [WCP's documentation](link-url "https://docs.wcproducts.com/frc-build-system/spline-and-motionx-system/splinexl-accessories"){:target="_blank} or [REV's documentation](link-url "https://docs.revrobotics.com/ion-build/motion/tubes-bushings-axles#application-example"){:target="_blank}. 

**Tube Nuts:** Hammered into round axles, tube nuts are optimal for low load applications like dead axle rollers. It allows shafts to be bolted directly to a part/plate. They are preferred because they can be easily bought COTS, however they are difficult to use because they must be hammered in precisely; any misalignment can cause inaccuracies and problems down the line. 

!!! Tip
      To improve the precision and strength of tube nuts, try putting two into one end. This can help align an axle better and withstand larger loads, which is especially important in large pivots.

**Billet Parts:** Many teams create custom, billet parts for mounting dead axles or even replacing them. Although significantly stronger than tube nuts, they require much more manufacturing ability than most teams are capable of. 

<figure>
      <img src="/img/design-handbook/motion-components/billet2910tech.png" style="width:50%">
      <figcaption>Custom billet tube plug on 2910's 2025 robot pivot. Holds one end of 2.5" OD custom dead axle. </figcaption>
</figure>

!!! Tip
      If you are interested in billet tube plugs and have a lathe, it is possible to make a lathed version using spacers. A typical spacer wider than the axle's OD can be machined down into a "plug" similar to 2056's plugs, with a flange for holding it in. This plug can be press fit into the tube and secured with a roll pin or screw. See [2056's discussion on Chief Delphi](link-url "https://www.chiefdelphi.com/t/team-2056-op-robotics-2025-technical-binder-release/502550/130"){:target="_blank"} for more information.

<figure>
      <img src="/img/design-handbook/motion-components/2056techplugs.webp" style="width:90%">
      <figcaption>Billet plugs on either end of dead axle for arm of 2056's 2025 robot.</figcaption>
</figure>

### Tolerances

It is important to keep in mind the tolerances of various components to ensure easy assembly. Often, each manufacturer can have their own tolerances. For example, a hex shaft from WCP may have a different tolerance than a bearing from REV Robotics, and may not fit on that bearing. 

Any parts made, like 3D printed parts, should have a large enough tolerance so they may slide onto an axle easily. The recommended tolerance is 0.005" to 0.010" of room. Components transmitting torque, like pulleys and gears, should have less tolerance while other components, like spacers, can have more tolerance. 

### Custom Axles

If you have the manufacturing capabilities (i.e. a lathe) or can order it out of house, custom machining axles may be helpful.

Some vendors, like WCP or AndyMark, sell custom shafts. These [output shafts](link-url "https://wcproducts.com/collections/systems-structure/products/output-shafts"){:target="_blank} are helpful in certain scenarios. However, these are often not necessary and are mostly used to ease assembly or under design constraints. 

<br>