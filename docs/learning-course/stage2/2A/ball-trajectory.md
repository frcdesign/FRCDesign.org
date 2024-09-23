# 2A: Basic Shooter

## Ball Trajectory

In a ball shooter, the trajectory is primarily determined by the exit angle and exit velocity of the game piece, which translates to how hard you launch and where you point the shooter.

<!-- Rigidity is crucial for maintaining trajectory consistency. Any wobbling or flexing in the shooter structure can negatively impact accuracy, as even slight movements can alter the exit angle or velocity, leading to unpredictable shot behavior. -->

<figure>
    <img src="/img/learning-course/stage2-shooter/shot-trajectory.gif" style="width:60%; border:5px solid #ADADAD">
    <figcaption>Team 1678's 2022 shooter ball trajectory.</figcaption>
</figure>

### Reference Design

For 2020, the initiation line on the field can serve as a reference point to estimate your shooting position and angle. The goal's scoring area is forgiving enough to accommodate slight variations in position, making precise alignment less critical. By using a shot distance calculator, you can estimate the optimal shooting parameters.

### Trajectory Calculator

Explore [this 2020 trajectory calculator](https://www.desmos.com/calculator/euvciqv3tr "Desmos 2020 Trajcetory Calculator"){:target="_blank"} to see how adjustments to angle and speed affect your shot. Can you identify a combination of angle and speed that allows for consistent scoring even with some positional variation?
!!! Calculator
    <center><iframe src="https://www.desmos.com/calculator/5fil8alfmd?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe></center>

<br>