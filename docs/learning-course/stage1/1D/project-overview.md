# 1D: Design Methodology - Simple Swerve Drivebase

## Project Overview
In this stage, you will be designing a swerve drivebase. A drivebase is the mobile platform on which all our other mechanisms are designed around and attached to. With the advent of reliable COTS swerve, designing a swerve drivebase has been made significantly easier and has become the most commonly used competitive drivetrain in FRC. 

A swerve drivebase is composed of four *swerve modules*. Each module has two motors: one for spinning the wheel and one for steering it. This enables the robot to translate in any direction independent of the rotation of the robot. In this project, we'll be using [SDS MK4i modules](https://www.swervedrivespecialties.com/products/mk4i-swerve-module "SDS MK4i Product Page"){:target="_blank"}. There are many other COTS options available, each with their own advantages and tradeoffs. 

<!-- You can learn more about drivetrains on the [Design Handbook](/design-handbook/mechanisms/drivetrain/) page. -->

<figure>
<img src="\img\learning-course\stage1d\SwerveBase\DriveAssy.webp" style="width:80%"></center>
<figcaption>*Stage 1D swerve drivebase project.</figcaption>
</figure>

As with previous exercises, the finished project is available for reference. If you need help, please feel free to ask on [the Discord](https://discord.gg/jHXTdNjYCg "DDS Discord Invite"){:target="_blank"}!

<center>[1D Drivebase Reference](https://cad.onshape.com/documents/6c6044229091a87cf359270b/w/ed9648f0c04c639a2561615a/e/67a7ed0c6038787281325a51 "1D Drivebase Reference Onshape Document"){:target="_blank" .md-button .md-button--primary }</center>

### Drivebase Frame

As was introduced in Stage 1A, robot structures are typically constructed out of aluminum box tubing. The drivebase is no exception to this. Most teams will opt to design their box tubing with a standard 0.5" spacing pattern of 0.196" diameter holes. This enables modularity and allows for easy integration of many COTS components like gussets.

Box tubing extrusions can be purchased at most metal suppliers, but many FRC vendors including [WCP](https://wcproducts.com/collections/systems-structure/products/punched-tubing){:target="_blank"}, [TTB](https://www.thethriftybot.com/products/thrifty-box-extrusion){:target="_blank"}, and [REV](https://www.revrobotics.com/MAXTube/){:target="_blank"} sell box tubing with pre-cut hole patterns which can significantly reduce manufacturing time and equipment requirements.

<br>