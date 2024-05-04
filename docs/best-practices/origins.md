<style>
.right{
    float:right;
}

.left{
    float:left;
}
</style>

# Origins
[image of origin cube]

## The Importance of Intelligent Origins
As with many good practices in CAD, smart origins are another good practice to make future you's life easier. Intelligent origins allow designers to leverage default geometry (Top/Right/Front Planes, Origin Point) in their models. Designers can utilize these planes for robust axes of symmetry and references. 


<details>
<summary>Examples of good and bad part origins</summary>
<br>
When modeling non-FRC parts, especially in non-multi-body workflow, origins are typically located on key features that have symmetry about them. The following examples help illustrate this.

TODO: add examples of good and bad part origins

</details>

However, it should be noted that with multi-body part modeling (As opposed to say, a 1 part per file workflow in Solidworks), origins for parts are not quite as critical since there are multiple parts in a single file. For FRC CAD, the purpose of origin is two fold:
1. We must have the same origin point across all part studios and assemblies so that the master sketch origin is respected.
2. To unify the robot CAD and robot software origin point. By having the same origin, the robot can be seamlessly exported to AdvantageScope and Camera transformations more easily measured measured. 

Although definitions may vary from team to team, the origin of an FRC robot is typically defined as the ***center of the drivebase, on floor level***.

In the following sections, we introduce a few different methods of locating an origin.


