# 2A: Full Detail Drivebase

## Electronics Mounting

To make wiring the robot and later inspecting the wiring easier, enough space should be left around each electrical component. You should work with your electrical teammates to determine the best location for the various control system parts. Teams typically try to mount their electronics on the bellypan, permitted there is space. 

!!! Example
    <center><img src="\img\learning-course\stage2-drivebase\elec\elecPic.png" style="width:80%"></center>
    <center><figcaption>Example layout of various different electronic components on a bellypan.</figcaption></center>

### Electronic Components

A list of typical electrical components found on FRC robots is provided below, as well as a recommended mounting location. Again, mounting locations are highly dependent on the rest of your robot, make sure to always coordinate with your electrical team to decide what is best.


!!! note "FRC Electrical Components"
    | **Component** | **Function** | **Suggested Location** | **Image** |
    |---|---|---|---|
    | REV Power Distribution Hub (PDH) or  CTRE Power Distribution Panel (PDP) | Distributes power to all other components | Bellypan | ![PDH](\img\learning-course\stage2-drivebase\elecComponents\pdh.webp) |
    | Main Breaker | Is used to turn on/off the robot and protect electronics from events with extremely high current drawn | Somewhere easily accessible and close to the PDH and Battery | ![Main Breaker](\img\learning-course\stage2-drivebase\elecComponents\mbreak.webp) |
    | RoboRIO | Central controller for all robot operations | Bellypan | ![RoboRIO](\img\learning-course\stage2-drivebase\elecComponents\rio.webp) |
    | Integrated motor controller (eg: Falcon 500, Kraken X60) | Powers and controls the  integrated motor | No electrical mounting required | ![Integrated motor controller](\img\learning-course\stage2-drivebase\elecComponents\kx60.webp) |
    | Discrete motor controller  (eg: Spark Max, Talon SRX) | Required to power and control some motors  (eg: NEO, CIM) | Near the controlled motor  or on the bellypan | ![Discrete motor controller](\img\learning-course\stage2-drivebase\elecComponents\smax.webp) |
    | Robot Radio | Allows the robot to establish wireless connections to the field or driver station | Follow Vivid Hosting's [radio mounting guidelines](https://frc-radio.vivid-hosting.net/getting-started/usage/mounting-your-radio "Vivid Hosting Radio Mounting Guidelines"){:target="_blank"}. | ![Robot Radio](\img\learning-course\stage2-drivebase\elecComponents\vh109.webp) |
    | Robot Signal Light (RSL) | Indicates whether the robot is on and enabled/disabled | Somewhere easily visible | ![Robot Signal Light](\img\learning-course\stage2-drivebase\elecComponents\rsl.webp) |
    | Inertial Measurement Unit (IMU) | Used to determine robot heading and acceleration | Close to the center is best practice (on Bellypan or VHB tape to attach to RoboRIO) | ![Inertial Measurement Unit](\img\learning-course\stage2-drivebase\elecComponents\imu.webp) |
    | Voltage Regulator Module | Can be used for custom circuits | Bellypan | ![Voltage Regulator Module](\img\learning-course\stage2-drivebase\elecComponents\vrm.webp) |
    | Pneumatics Hub | Controls pneumatic components | Bellypan | ![Pneumatics Hub](\img\learning-course\stage2-drivebase\elecComponents\pcm.webp) |