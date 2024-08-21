# 2C: Deadaxle Pivot

# What is a Rotary Mechanism? 
Rotary mechanisms allow us to pivot objects or mechanisms through a rotational movement. These are typically done through wrists or arms. There are two ways 

### What is a Dead Axle?
Dead axles are the preferred way of holding a pivoting mechanism. The mechanism is then directly powered through a different means. This tends to be significantly stronger since you can have a larger axle and there is no risk of twisting.

### What is a Live Axle?
Live axles are most commonly thought of when doing pivots. Teams commonly do this through a hex axle and hub, but this is heavily not recommended due to the risk of twisting, as well as being extremely weak due to the small diameter.

That being said, live axles can be strong if using the appropriate live axle shaft, such as SplineXL or MAXSpline.

## Concepts

### Strength

The first concept we need to keep in mind is how are we going to securely hold our rotary mechanism? If it is too weak, it may break or bend. The most common solution to this is dead axles.

Dead axles are a type of axle that doesn't move and your object rotates around it. As a result you can have much stronger axles which are more rigid and allow for a more consistent motion. This is typically done through the strength of the axle, in addition to the fact that the shaft isn't able to be twisted. 

The main factor that impacts strength of a dead axle is the diameter of the axle. As the diameter increases, the strength increases proportionally. This is significantly more important than material choice. You may see teams use steel hex shaft that twists, but a large diameter round tube of 0.75 inches or greater would probably be strong enough.

In extreme cases, you may find massive diameters of 2+ inches, though these are not common. 6061 round aluminum tube with a 1/16 thickness is the most common choice for the maximum strength to weight. Common sizes are 0.75 inches and 7/8 inches.

### Friction

Since your mechanism is pivoting on the axle, you need to reduce the friction. This is typically done either through bushings or bearings. Bushings are the most common choice, since they are strong, package smaller, and work fine for the application.

(insert bushing picture)
You can also use bearings for pivots, but you may need to do research in order to properly spec the loads. Bearings are typically used for extremely large diameter pivots greater than 1 inch. 

(insert bearing picture)


### Power 
Since the axle is dead, you need to directly power your pivot instead of pivoting on an axle. 

u can use chain, belt, or gear rack depending on application
most common is chain 
belt not greaet since it is prone to skipping and needs to be perfect cc or slightly tighter

gear rack is used for certain niches when you need large gear reduction 

### Tensioning

turnbuckle
uh
pivoting tensioner
spartan tensioner
physically move the object tensioner

When powering with a chain, you need to tension to reduce backlash. Backlash increases the amount of slop in your pivot, which makes it less accurate. 

### Other backlash sources

Other backlash sources include

- Hex interfaces

    - For every hex to gear interface, there is gap which adds backlash. Utilizing shim tape (insert mcmaster link), you can reduce this backlash significantly. 3 pieces of tape in a "triangle" formation is enough.

- Sprocket Clocking

    - Make sure your sprockets are clocked correctly.

- Mounting slop 

    - Depending on how you mount, you may have some slop due to the bolt to hole interface. 

- Stages

    - In general, the amount of stages multiples the amount of backlash you have. It is best to stay 3 stages or lower, with one stage being the pivot reduction. 


## Application 
In the above fundamentals, you can see that there are different options for different use cases. You can mix these concepts and make the tradeoffs in order to best fit your use application and scope. 
 
### Wrist (insert wrist picture here)
Wrists are rotary mechanisms that are typically short and light. You can find both live axle and dead axle applications for wrists. 
bearings or bushings 

### Large Pivots
Large pivots include things such as pink arms, pivoting elevators, and arms. 
chain, 35 chain
big axle
dead axle good
could use thin bearings but bushings more common

### Pivot
bearings or bushings are common
In some games like 2024, you may pivots full mechanisms such as a shooter to adjust your shot angle. 

## Rules for Design:
1. Try to make whatever "arm" you are pivoting as short as physically possible. This makes it easier to program, design, and build. For the majority of pick and place games, you want to generally start with a linear mechanism, and then add a short wrist if necessary. 
2. Make sure that your axle is fully supported. This can be done through tube or nesting in plate. 
3. Make sure the support structure is rigid. 
4. 


# Project

We'll be designing a simple dead axle that is attached to an elevator. 



<br>

