# 1E: Subsystem Workflow - Detailing the Drivebase

## Electronics Mounting

To make wiring the robot and later inspecting the wiring easier, enough space should be left around each electrical component. You should work with your electrical teammates to determine the best location for the various control system parts. Teams typically try to mount their electronics on the bellypan, permitted there is space. 

!!! Example
    <figure>
        <img src="../images/elec/elec-example.webp" style="width:80%">
        <figcaption>Example layout of various different electronic components on a bellypan. (Photo Credit: FRC 3647)</figcaption>
    </figure>

### Electronic Components

A list of typical electrical components found on FRC robots is provided below, as well as a recommended mounting location. Again, mounting locations are highly dependent on the rest of your robot, make sure to always coordinate with your electrical team to decide what is best.


!!! note "FRC Electrical Components"
    | **Component** | **Function** | **Suggested Location** | **Image** |
    |---|---|---|---|
    | REV Power Distribution Hub (PDH) or  CTRE Power Distribution Panel (PDP) | Distributes power to all other components | Bellypan | ![PDH](../images/elec-components/pdh.webp) |
    | Main Breaker | Is used to turn on/off the robot and protect electronics from events with extremely high current drawn | Somewhere easily accessible and close to the PDH and Battery | ![Main Breaker](../images/elec-components/mbreak.webp) |
    | RoboRIO | Central controller for all robot operations | Bellypan | ![RoboRIO](../images/elec-components/rio.webp) |
    | Integrated motor controller (eg: Falcon 500, Kraken X60) | Powers and controls the  integrated motor | No electrical mounting required | ![Integrated motor controller](../images/elec-components/kx60.webp) |
    | Discrete motor controller  (eg: Spark Max, Talon SRX) | Required to power and control some motors  (eg: NEO, CIM) | Near the controlled motor  or on the bellypan | ![Discrete motor controller](../images/elec-components/smax.webp) |
    | Robot Radio | Allows the robot to establish wireless connections to the field or driver station | Follow Vivid Hosting's [radio mounting guidelines](https://frc-radio.vivid-hosting.net/getting-started/usage/mounting-your-radio "Vivid Hosting Radio Mounting Guidelines"){:target="_blank"}. | ![Robot Radio](../images/elec-components/vh109.webp) |
    | Robot Signal Light (RSL) | Indicates whether the robot is on and enabled/disabled | Somewhere easily visible | ![Robot Signal Light](../images/elec-components/rsl.webp) |
    | Inertial Measurement Unit (IMU) | Used to determine robot heading and acceleration | Close to the center is best practice (on Bellypan or VHB tape to attach to RoboRIO) | ![Inertial Measurement Unit](../images/elec-components/imu.webp) |
    | Voltage Regulator Module | Can be used for custom circuits | Bellypan | ![Voltage Regulator Module](../images/elec-components/vrm.webp) |
    | Pneumatics Hub | Controls pneumatic components | Bellypan | ![Pneumatics Hub](../images/elec-components/pcm.webp) |

<br>