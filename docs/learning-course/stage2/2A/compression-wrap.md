# 2B: Basic Shooter

## Compression & Wrap

### Compression

The purpose of compression is to efficiently transfer energy from the flywheel to the game piece. The softer the game piece, the more compression is needed for effective energy transfer. Insufficient compression causes slipping, resulting in poor energy transfer, while excessive compression increases power requirements and reduces efficiency. Prototyping is essential to find the right balance. For games with hard game pieces, like in 2017, compression can be also achieved using a foam backing.

### Wrap

Wrap refers to the duration the game piece stays in contact with the flywheel. A longer wrap time allows for more consistent energy transfer. For the underlying physics, see [Impulse (Wikipedia)](https://en.wikipedia.org/wiki/Impulse_(physics) "Impulse Wikiepdia Page"){:target="_blank"}.

???+ Video "Not Enough Compression/Contact Time"
    <figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/5OoCSAgqm3s?si=ougTDRU_EV1QIwa3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </figure>
    <figcaption>This is what it may look like if you do not have enough compression. See how loud the shooter is compared to how far the shot actually goes (Warning: Loud Audio / Swearing)</figcaption>

???+ Video "Good Contact Time and Compression"
    <figure>
    <iframe width="320" height="560" src="https://www.youtube.com/embed/9DEJG6eoeaQ" frameborder="0" allowfullscreen></iframe>
    </figure>
    <figcaption>This is what it looks like if you have good contact time and compression with the exact same robot. (Warning: Loud Audio)</figcaption>

[Stealth wheels](https://www.andymark.com/products/stealth-wheels-options "Stealth Wheel Product Page"){:target="_blank"}, Solid roller wheels, ([WCP Solid Roller Wheels](https://wcproducts.com/products/solid-roller-wheels "WCP Solid Rubber Wheel Product Page"){:target="_blank"}), and Colson wheels are chosen commonly because of their lack of compression and soft grippy silicone surface. These are all good options for shooter wheels to prototype in a build season. 


### Reference Design

The example design uses 4 inch diameter roller wheels. The diameter allows for enough contact time while being small enough to reasonably package. 


### Feeder

A wheel or set of belts is commonly used to feed game pieces into the flywheel. The design depends on the game and the specific feeding strategy. For instance, in the 2020 game, it is advantageous to power both sides of the feeder due to the sticky nature of the power cell. In the example, a single compliant wheel is employed to direct the game pieces into the shooter.
<br>
<figure><img align="left"  src="\img\learning-course\stage2-shooter\2910shooter.gif" width="47%" style="border:5px solid #ADADAD"><img align="right"  src="\img\learning-course\stage2-shooter\1690shooter.gif" width="42%" style="border:5px solid #ADADAD"></figure>
<center><figcaption>Observe how the game pieces are fed into 2910's and 1690's robot.</figcaption></center>

<br>