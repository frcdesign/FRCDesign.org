---
image: docs/img/mechanism-examples/pivots/2910/2910pivot.webp
---

<style>

td, th , table{
   border: none!important;
}

td{
  text-align: left !important;
  vertical-align: middle !important;
}

table tr:hover{
    background-color: transparent !important;
}

</style>

# 2910's 2023 Dead Axle Pivot

<figure markdown="span">
[![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/2910pivot.webp){height=60% width=60%}](https://cad.onshape.com/documents/43505c3f750efb19e995ad36/w/e246489aced2d23991a0f2a1/e/0237a300633b2cf31e173173?renderMode=0&uiState=663907354e7bd8067caebdc4){target = "_blank"}
<figcaption>This dead axle pivot was created by 2910 just recently in the 2023 season and has already been utilized by a number of different teams, including Hall of Fame Team 359 Hawaiian Kids that next year in 2024, who ranked #20 in the world using this pivot as the base for their robot.</figcaption>
</figure>

### Links

[CAD Document](https://cad.onshape.com/documents/43505c3f750efb19e995ad36/w/e246489aced2d23991a0f2a1/e/0237a300633b2cf31e173173?renderMode=0&uiState=663907354e7bd8067caebdc4 "CAD Document Link"){:target="_blank" .md-button .md-button--primary}

[CAD and Tech Binder Release ChiefDelphi Thread](https://www.chiefdelphi.com/t/2910-cad-and-tech-binder-release-2023/436653 "Tech Binder Chief Delphi Thread"){:target="_blank"}

[Match Video](https://www.youtube.com/watch?v=LzgU0rbpWqY "2910 Match Video"){:target="_blank"}

## Behind the Design

The pivot is driven by 2 mirrored dual falcon 500 gearboxes. These gearboxes are incredibly compact and thoughtful design decisions have been made throughout the whole pivot to reduce part count. One method utilized in this gearbox is to use a Thunderhex bearing retention technique in which each shaft is turned down from 1/2" Hex to 13.75mm (Thunderhex diameter) on each end, which fully constrains each flange bearing as long as the two plates are compressed. This both reduces part count, design complexity, and makes the gearboxes easier to assemble and service, requiring only 5 bolts to swap out the entire motor plate (motors included) and the entire gearset.

||||
|:-:|:-:|:-:|
|<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/2910gearbox.webp){height=60% width=60%}</figure>|<figure markdown="span">![Thunderhex Pivot](../../img/mechanism-examples/pivots/2910/thunderhex_example.webp){height=100% width=100%}<figcaption>Thunderhex bearing retention technique utilizing turned hex flanges, bearing flanges, and fixed plates.</figcaption></figure>|<figure markdown="span">![Exploded View](../../img/mechanism-examples/pivots/2910/2910_exploded.webp){height=60% width=60%}</figure>|

All of these plates are heavily lightened to increase the robots top speed and acceleration capabilities (F=ma), and to keep the center of gravity low. The gearboxes and even motor placement on the gearboxes are as low and central as possible to improve the robots center of mass. Lower center of mass helps to reduce tipping and gives the robot an advantage in pushing battles.

The second stage shaft runs across the robot to link the two gearboxes, which is essential to eliminate any torsion in the arm that would be caused by unevenly driving each side of the pivot independently.

|||
|:-:|:-:|
|<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/pivot_link.webp){height=60% width=60%}</figure>|<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/bearings.webp){height=100% width=100%}<figcaption>Wheel Support Reference from REV ION Robot Basics Guide</figcaption></figure>|

The third stage is an additional reduction that doubles as a tensioning mechanism,  reusing the mechanical link shaft as an idler shaft to pivot around, adjusting the center to center distance of the final chain run. Tightening the bolt (shown in red in the diagram below) pulls the lever back, applying tension to the chain. The planet gear & sprocket shaft uses the same ½” to 13.75mm diameter hex shaft technique to reduce part count. Using a chain for the final reduction and power transmission is optimal due to its exeptional tensile strength and ability to absorb shock loads.

<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/planetgear_idler.webp){height=80% width=80%}</figure>

The main pivot itself is a massive dead axle fixed into the triangular superstructure. Triangles are strong! This (almost) right angle superstructure is incompressible, as when a force is applied to compress any side there is always an opposite side in tension to counteract that force. This dead axle assembly is very simple, with 3 custom parts that are all easily manually machineable on a lathe. The large dead axle has two end caps and a single bolt through from one end to the other to hold the whole axle assembly together.

|||
|:-:|:-:|
|<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/deadaxle_retention.webp){height=100% width=100%}</figure>|<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/aframe2.webp){height=100% width=100%}</figure>|

|||
|:-:|:-:|
|<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/6328/triangles.webp){height=100% width=100%}</figure>|<figure markdown="span">![2910 Dead Axle Pivot](../../img/mechanism-examples/pivots/2910/triangles2.webp){height=100% width=100%}</figure>|

<br>
