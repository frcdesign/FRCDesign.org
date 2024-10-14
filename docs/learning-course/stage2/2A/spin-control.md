# 2A: Basic Shooter

## Spin Control


### Spin

When using a single flywheel shooter, spherical game pieces can acquire spin due to the static nature of one side of the shooter. In 2022, excessive spin was problematic as it caused the game piece to bounce out of the goal. To address this, backrollers were introduced to counteract the spin by rotating in the opposite direction. While some spin can enhance shot stability—beneficial in games like 2017, where a steep arc trajectory was advantageous—it needed to be carefully managed in 2022 to avoid negatively impacting shot accuracy.

<center>
<video width="600" controls>
<source src="\img\learning-course\stage2-shooter\bounceout.webm" type="video/webm">
Your browser does not support the video tag.
</video>
<center> *Bounceout caused by too much spin. Credit: FRC Team 7492* </center>
</center>

### Back Rollers

Reducing friction helps transfer more energy into the shot by minimizing the energy lost to spinning the ball. This can be achieved by using low-friction materials on the hood or incorporating back rollers, which further decrease friction and improve shot efficiency.

<figure><center>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/1b8spBWIAT4?si=daEZUNFTRv_rsYMn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <figcaption> This high speed shooter video uses PTFE tape to lower the friction on the hood backing to reduce some of the spin. This led to a higher exit velocity by 2 miles per hour. </figcaption>
</center></figure>


Back rollers increase energy transfer to the ball in three key ways:

1. They reduce the amount of spin imparted to the game piece, converting more energy into forward motion and increasing shooting speed.
2. They decrease drag by ensuring both sides are powered, allowing for greater compression and more effective energy transfer.
3. They increase the number of contact points, improving overall energy transfer to the game piece.

Back rollers should rotate in the opposite direction to the shooter. This can be achieved by adding additional motor(s) to the back rollers or by using gears and belts to link the main flywheel to the back rollers. Linking the two sides mechanically can simplify software control. By changing the speed of the back rollers, you can control the amount of spin imparted onto the game piece.

<figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QZKDnRvLhrA?si=9ZoKnbHI4jayoux0&amp;start=5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <figcaption>Observe how the ball spins as it travels along the shooter path. Despite the presence of back rollers, some spin is still evident. </figcaption>
</figure>

<br>