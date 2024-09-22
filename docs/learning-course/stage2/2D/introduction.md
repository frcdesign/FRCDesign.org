# 2D: Cascade Elevator

## Elevators
Elevators pop up commonly in FRC and are used to move mechanisms in a compact linear fashion. This is usually to reach higher places with a mechanism, reach far out from your frame perimeter, or even climb on a field element. Elevators are typically classified by the way they are "Rigged". Elevator "Rigging" is what allows the motor to transmit motion to each stage. FRC elevators are usually rigged to be either "Cascade" or "Continuous." 

<br>
<figure><img align="left"  src="\img\learning-course\stage2-elevator\2468elevator.gif" width="55%" style="border:5px solid #ADADAD"><img align="right" src="\img\learning-course\stage2-elevator\4414elevator.gif" width="39%" style="border:5px solid #ADADAD"></figure>
<center><figcaption>2468's Cascade Elevator and 4414's Continuous Elevator</figcaption></center>
<br>

Watch the following match videos to see [2468's 2023 Robot with a cascade-rigged elevator](https://www.youtube.com/watch?v=RAFjZgB_72w "2468 2023 Match Footage Video"){target=void} and [4414's 2023 Robot with a continuous-rigged elevator](https://youtu.be/PKPuqpe1Wlg "4414 2023 Match Footage Video"){target=void} in action.

### Utilizing COTS Components

Elevators as designed most typically may be out of the scope of a lower-capability team because of the amount of custom metal parts that need to be bought or manufactured, but once you know how one works and have designed one, you may be able to make one with minimal manufacturing capabalities and time required. This project will be discussing the design of a cascade-rigged elevator over a continuous-rigged elevator due to the availability of COTS parts and minimal manufacturing required for a cascade-rigged elevator.

### Cascade Elevator
Cascade elevators are characterized by the way the stages move. In a cascade rigged system, each elevator stage moves the same distance from its parent stage.

<figure markdown="span">
    ![cascade](/img/learning-course/stage2-elevator/cascade.gif)
    <figcaption>Cascade Motion</figcaption>
</figure>

### Comparison

Cascade elevators have a number of pros and cons when compared to continuous elevators.

| **Pros** | **Cons** |
|----------|----------|
| Cascade elevators are great when you just need to move a mechanism up and down and you don't need more than 3 Elevator stages to reach the desired height. While it is possible to make cascade elevators with more than 3 stages, designing the rigging gets harder, especially if you are width constrained. | Usually things cannot be passed through a cascade elevator because of the rigging, while you can pass things through a continuous elevator. |
| Cascade motion is faster than continuous due to the stages being linked together and continuous effectively being one long stage. | The center of gravity is not optimal in the middle range of extension compared to continuous. |
| All of the major Cascade Elevator components are available as COTS components, which means you can simply stock cascade elevator components and throw it together without worrying about custom manufacturing. | The motors powering a cascade elevator need geared down more to counteract the natural upduction the cascade rigging adds. |

<br>