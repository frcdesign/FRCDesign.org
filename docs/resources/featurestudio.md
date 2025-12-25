!!! note
    For many teams, writing your own FeatureScripts is not necessary. There are plenty of pre-made FeatureScripts addressed [here]()

## Syntax

### Variables and Constants
In Feature Studio, you can define a variable with `var name = value`. Later in code, when you use name, it will use the value associated with it. Additionally, if the value is assigned once and never changed, you can change the declaration to `const name = value`.

### Functions
A function is a block of code that is easily reusable and preforms a specific task. To define a function, you type `function myFunctionName()`. If you need to pass things into the function, you can use the syntax `function myFunctionName(var1 is Type)`. To execute the function, you can call it with the syntax `myFunctionName(var1)`

### Common Patterns
Typically, variable names are expected to be in camelCase(ex: var1, thisIsVar1, i, j). Boolean variables should be prefixed with do(ex: doFlip, doFillEntirePart). 

Top-level constants should be in UPPERCASE_WITH_UNDERSCORES(ex: INCHES_TO_FEET, PI, E). Only do this if you know this value will never change. Also, code should always adhere to the DRY(Don't Repeat Yourself) principle. Take the following code for instance:

```ts
const circle1 = 3.14159 * 3 * 3;
const circle2 = 3.14159 * 7 * 7;
```

This code correctly calculates the area of 2 circles, but it is hard to read. We have unnecessarily repeated the PI * R^2 formula. This could be reformatted as:

```ts
const PI = 3.14159;

function calcCircleArea(radius is number){
  return PI * radius * radius;
}

const circle1 = calcCircleArea(3);
const circle2 = calcCircleArea(7);
```

### Creating a FeatureScript
After creating a new document, click the plus icon on the bottom left. Create a Feature Studio. Next, click on the New Feature button on the top left. It will insert the following code:

```ts
annotation { "Feature Type Name" : "My Feature", "Feature Type Description" : "" }
export const myFeature = defineFeature(function(context is Context, id is Id, definition is map)
    precondition
    {
        // Define the parameters of the feature type
    }
    {
        // Define the function's action
    });
```

Let's go line-by-line through this code. 

`annotation {...}` is talked about in depth later in the course. In short, it tells the UI what to display.

`export const myFeature =` exports the feature so Onshape can discover it.

`defineFeature(function(context is Context, id is Id, definition is map){` calls defineFeature and passes it your code. `context` contains the geometry, `id` is a unique id for this feature, `definition` contains user-supplied values

`precondition{` contains the code that tells Onshape what inputs your FeatureScript needs.

`{` contains the code that tells onshape what to do.

To run your code, use the shortcut `ctrl+s` or click the commit button, then navigate to the Part Studio tab and type your FeatureScript name into the search bar.
## Precondition Body

### Annotation
The `annotation{...}` syntax helps the user to attach extra information to the next statement that does not change the program's core logic, but provides metadata that Onshape can use. It takes in a map object(`{"key": "value"}`). Here are some of the most common keys:

- `"Name"`: Display name for a variable
- `"Filter"`: Specifies predicates for a feature script input.
- `UIHint"`: Changes the default display of an input. Can be any of [these](https://cad.onshape.com/FsDoc/library.html#UIHint)
- `"Feature Type Name"`: Display name for a feature
- `"Default"` sets a default value for an input.

### Predicates

Predicates are used to restrict user input by controlling what kinds of entities a user is allowed to select. There are three commonly used types of predicates: [EntityType](https://cad.onshape.com/FsDoc/library.html#EntityType), [GeometryType](https://cad.onshape.com/FsDoc/library.html#GeometryType), and [SketchObject](https://cad.onshape.com/FsDoc/library.html#SketchObject). To use these predicates, you can combine them with logical operators(and: `&&`, or: `||`, not: `!`).

```ts
//the user can only select cylindrical faces
annotation{
  ...
  "Filter": EntityType.FACE && GeometryType.CYLINDER
  ...
}
```

### Geometry Validation

Another way to guarantee that the user is selecting only valid inputs is with the `is___`-type functions. For example, `isInteger` guarantees that the value passed into it is an integer by throwing an error if its not. Likewise, the `isAngle` function will ensure that its parameter is an angle. This is slightly different from a predicate, however, because predicates enforce their restriction at compile time; if your predicate specifies a face, you must select a face because onshape will literally not let you select anything else. With these functions, you can still type in invalid values, but the feature script will throw an error.

### User Input

To get user input, you must specify in the `definition` variable what type of input you want. For example, if you wanted to take in a message to display to the user, you would state `definition.specialMessage is string`. This tells onshape that it should a field called specialMessage and have it take in a string.

<center markdown>![alt text](../images/featurestudio/no-annotation-input.webp)</center>

Even though it works, it is not pretty. Many users expect to see Special Message for an input field label, not specialMessage. Additionally, it could be hard to for the user to know what that field even does. This is where annotations come into play. With `annotation{}`, we can tell onshape to display `Special Message` and tell it what description to display. Here is the complete code for the featurescript:

```ts
FeatureScript 2837;
import(path : "onshape/std/common.fs", version : "2837.0");

annotation { "Feature Type Name" : "My Feature", "Feature Type Description" : "" }
export const myFeature = defineFeature(function(context is Context, id is Id, definition is map)
    precondition
    {
        annotation { "Name" : "Special Message", "Description" : "Text to engrave into selected face"}
        definition.specialMessage is string;
    }
    {
        // Define the function's action
    });
```
<center markdown> ![alt text](../images/featurestudio/annotated-input.webp) </center>

Clicking the Feature Parameters button on the top left(has a p and is to the right of the New Feature button) will allow you to automatically insert many different types of inputs.

## Function Body

### Queries

Queries contain IDs for geometry. Onshape does this so that even if the geometry changes, the Query will still evaluate to the correct geometry. Queries can give you access to many different types of functions. For example, `qAdjacent` will find all adjacent elements to a query. Most functions will only return one query even if there are multiple geometry elements selected. This is because queries are allowed to contain multiple different geometry elements. To split them up, you can use `qEvaluate` to turn it into a list of queries. Common query functions include:

- `qAdjacent`
- `qSubtraction` / `qUnion`
- `qNthElement`
- `areQueriesEquivalent`

All of their documentation/use cases are available [here](https://cad.onshape.com/FsDoc);

### IDs
Every operation in Feature Studio must have a unique ID. The `id` variable is given to your FeatureScript at runtime that you should append before each assigned ID. ID's are stored hierarchically and each routine should have a unique ID prefix. The `+` operator tells Onshape to make a new level. Take for instance the following pseudocode:

```ts
// create a sketch with ID `rect1ID`
const rect1ID = id+"r"+1
createRect(rect1ID); 

// extrude the sketch identified by `rect1ID`
const extrude1ID = id+"e"+1
extrude(extrude1ID, rect1ID); 
```
This creates a valid hierarchy. Each parent element is comprised of unique children. When Onshape executes this, it looks like this:

<center markdown>![](../images/featurestudio/featurestudio-ex1.gif){width=80%}</center>

Now, lets look at an example of what an invalid hierarchy would look like.

```ts
// create a sketch with ID `rect1ID`
const rect1ID = id+"r"+1
createRect(rect1ID); 

// extrude the sketch identified by `rect1ID`
const extrude1ID = id+"e"+1
extrude(extrude1ID, rect1ID); 

// create a sketch with ID `rect2ID`
const rect2ID = id+"r"+2
createRect(rect2ID); 

// extrude the sketch identified by `rect2ID`
const extrude2ID = id+"e"+2
extrude(extrude2ID, rect2ID); 
```

It's hierarchy looks like this.

<center markdown>![](../images/featurestudio/featurestudio-ex2.gif){width=80%}</center>

Notice how there the order of creation is id->r, id->e, id->r. Onshape does not allow two nonconsecutive levels with the same name. However, as one final example, let's look at what onshape DOES allow.

```ts
// create a sketch with ID `rect1ID`
const rect1ID = id+"r"+1
createRect(rect1ID); 

// create a sketch with ID `rect2ID`
const rect2ID = id+"r"+2
createRect(rect2ID); 

// extrude the sketch identified by `rect1ID`
const extrude1ID = id+"e"+1
extrude(extrude1ID, rect1ID); 

// extrude the sketch identified by `rect2ID`
const extrude2ID = id+"e"+2
extrude(extrude2ID, rect2ID); 
```

<center markdown>![](../images/featurestudio/featurestudio-ex3.gif){width=80%}</center>

Onshape allows this even though the "r" level is repeated because they are consecutive, unlike the previous example. Notice how previously the order was id->r, id->e, id->r, id->e, whereas this one was id->r, id->r, id->e, id->e.

There are additional examples + explanations [here](https://cad.onshape.com/FsDoc/library.html#Id);

### Sketches

To create a sketch, use the `newSketch(context, "id", {"face": queryOfPlanarFace})`, or if you only have a `Plane` object, use `newSketch(context, "id", {"face": planeObject})`. Planes can be created with the `plane(origin, normal, x)` function. To draw on the plane use functions prefixed with `sk`, such as:

- `skCircle`
- `skEllipse`
- `skBezier`
- `skRectangle`
- `skConstraint`

As always, all descriptions of these function are available on the [documentation](https://cad.onshape.com/FsDoc).

To finish a sketch, use the `skSolve(sketch)` function.

To do any operations on a sketch, get it's associated query with the function `qSketchRegion`

### Operations

Operations modify or create geometry in the Part Studio. The take in queries to produce modified bodies. Almost all operations are prefixed with `op`. The most common operations are:

- `opExtrude`
- `opRevolve`
- `opBoolean`
- `opFillet`
- `opTransform`
- `opPattern`

Every `op___` function has a detailed signature and examples in the [Standard Library Documentation](https://cad.onshape.com/FsDoc).

### Debugging

Often when making FeatureScripts, you run into errors that occur during runtime. To help with this, onshape has exposed the `debug` function. Given a context and a variable, it will print it out and highlight it if it can. You can also optionally specify a color. For example, if you wanted to find all adjacent elements to a face, but for some reason it wasn't returning what you wanted, you could highlight the face like this: 

```ts
...
const face = qNthElement(qEverything(EntityType.FACE), 0);
debug(context, face);
//optionally specify color: `debug(context, face, DebugColor.BLACK)`
```

## Additional Resources

Don't forget every function has detailed descriptions in the [Standard Library Documentation](https://cad.onshape.com/FsDoc). 