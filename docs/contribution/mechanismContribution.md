# Contributing to Mechanism Examples

The [mechanism examples](../mechanism-examples/index.md "Mechanism Examples Page"){:target="_blank"} pages are the ones that would benefit the most from outside contribution. You can add examples from other teams, of course, but adding your own mechanism and going behind the design and performance on it will be ideal. If adding an example from another team, try to interview them for their input and more accurate information.

**Criteria for Mechanism Examples:**

- It must have been actually built and used at a competition
- You must show both the good parts and the bad parts. What was it designed for? Why were certain decisions made? How easy was it to build and manufacture? How did it actually perform? What went well and what would be changed if it was redesigned?
- Go into detail about specific parts of the design, such as the materials and parts used and why, any specific mechanisms or processes, etc.
- Detailed pictures of the CAD and/or the actual robot. Preferably public CAD made in or uploaded to Onshape. 
- Extra media and links if available and applicable.

## Adding Mechanism Examples

As was described in [methods of contributing](methodsOfContributing.md "Contribution Guide Page"), there are two methods:

1. Writing the contribution on a separate platform (such as Google Docs) and getting an internal contributor to add it to the website
2. Forking and making a pull request on GitHub

The first method is pretty self explanatory, but if you choose to fork and make a pull request on GitHub, there is some formatting required. Make sure to follow the contribution guide on the [methods of contributing](methodsOfContributing.md "Contribution Guide Page") page to get up and running with GitHub and VS Code.

## Adding a Mechanism Category (OPTIONAL)

If you need to add a mechanism category, you must add a landing page for the mechanism examples in that category and a grid card to the [mechanism examples landing page](../mechanism-examples/index.md "Mechanism Example Index Page").

### Adding the Folders and Files

1. Create a new folder under `mechanism-examples` with the name of the new mechanism category. All mechanism example pages and the landing page for the category will be in this folder. 

    !!! Note
        If there are multiple types of the mechanism (such as with elevators and intakes), you can create multiple folders in that with the landing pages in each separate folder. For example, the folder `elevator` contains the folders `cascade` and `continuous`, both of which contain a landing page `index.md`.

2. In the root folder of the new category, create a new file called `.meta.yml` and copy the following code into it:

    ``` yml
    social:
        cards_layout_dir: layouts
        cards_layout: mechanism_fundamentals_wide
    ```
    This sets the size of image you will use for the social card for embeds for the whole category. You can choose between `mechanism_fundamentals_wide` or `mechanism_fundamentals_tall` for the `cards_layout` option. 

    Images have to be 1:1.545 or 1.545:1, any size. More information provided [here](mechanismContribution.md#adding-an-image-for-the-example "Adding images section")

3. Create the landing page(s) for the category, named `index.md`. Only one of these can be made per folder.

    Copy this template for the category landing page and fill it out with your information:

    ``` md
    ---
    title: page-title
    image: link-to-social-card-image
    ---
    
    
    # page-title
    description
    
    <div class="grid cards" markdown>
    
    -   <center>[![](link-to-mechanism-image)](link-to-page)</center>
    
        ---
    
        description-about-unique-aspects-of-example
        
        [:octicons-arrow-right-24: page title](link-to-page)
    
    </div>
    
    <br>

    ```

    The following is the code for the drivebase examples landing page:
    
    ```
    ---
    title: Drivebase Examples
    image: docs/img/mechanism-examples/drivebase/2910_2023_dt.webp
    ---
    
    
    # Swerve Drivebases
    The drivebase is the single most important part of your robot, providing a bed for every other subsystem to build off. Examples of different drivebases can provide inspiration for electronics layout, bellypan shapes, and structural cross members for mounting, all of which can be a hard but crucial part of designing a robot, as accessibility and maintainability need to be preserved even as subsystems get placed on top of the robot.
    
    <div class="grid cards" markdown>
    
    -   <center>[![](../../img/mechanism-examples/drivebase/2910_2023_dt.webp)](2910_2023_dt.md)</center>
    
        ---
    
        A custom plate to keep the radio and breaker accessible, holes with grommets to allow wires to pass through the cross members
        
        [:octicons-arrow-right-24: 2910 Charged Up Drivebase](2910_2023_dt.md)
    
    -   <center>[![](../../img/mechanism-examples/drivebase/972_2024_dt.webp)](972_2024_dt.md)</center>
    
        ---
    
        A central 2x2 cross member, a brainpan, and citrus bumper mounting plates.
        
        [:octicons-arrow-right-24: 972 Brainpan Drivebase](972_2024_dt.md)
    
    </div>
    
    <br>
    ```

### Adding a Grid Card to the Mechanism Examples Landing Page

All grid cards are contained in the `<div class="grid cards" markdown>` div. See the [mkdocs-material docs about grid cards](https://squidfunk.github.io/mkdocs-material/reference/grids/#using-card-grids "MKdocs Card Documentation"){:target="_blank"} for more information.

Copy and paste the following code into the div and replace all template information with your own.

``` md
-   <center>[![](link-to-image)](link-to-category-page)</center>

    ---

    Example Description
    
    [:octicons-arrow-right-24: category-name](link-to-category-page)
```

!!! Note
    Leave a line break in the code between each card, otherwise the card content will merge.

The following is the code for the drivebase examples grid card:

``` md
-   <center>[![](../img/mechanism-examples/drivebase/2910_2023_dt.webp)](drivebase/index.md)</center>

    ---

    Swerve drivebases with examples of electronics layout
    
    [:octicons-arrow-right-24: Swerve Drivebases](drivebase/index.md)
```

## Adding a Mechanism Example Page

Adding a mechanism example page to an already existing category requires a few things to be done. The page has to be created, a grid card for it must be created in the category landing page, and an standard image for the example needs to be created. 


### Creating the Page

Create a new `.md` file in the category folder for your example. 

Copy the following template into it and fill out the information using Markdown formatting:

```
---
image: link-to-social-card-image
---

# mechanism-example-name

<figure markdown="span">
    [![alt-text](link-to-image){height=80% width=80%}](link-to-cad){target = "_blank"}
<figcaption>caption</figcaption>
</figure>

### Links
[CAD Link](link){target = "_blank"}

## Behind the Design

<br>
```

The following is an example of the 2910 Charged Up Drivebase page without content written:

```
---
image: docs\img\mechanism-examples\drivebase\2910_2023_dt.webp
---

# 2910 Charged Up Drivebase

<figure markdown="span">
[![2910 Charged up Drivebase](../../img/mechanism-examples/drivebase/2910_2023_dt.webp){height=80% width=80%}](https://cad.onshape.com/documents/28a885d3b8ad7de567efebbd/w/33b7dd39d54ec1ab15f2e2aa/e/d78c591638c349b708e238e6){target = "_blank"}
<figcaption>Swerve drivetrain featuring MK4I swerve modules, a pocketed bellypan, and a billet brass frame-rail for weight distribution.</figcaption>
</figure>

### Links
[CAD Link](https://cad.onshape.com/documents/28a885d3b8ad7de567efebbd/w/33b7dd39d54ec1ab15f2e2aa/e/d78c591638c349b708e238e6){target = "_blank"}

## Behind the Design

<br>
```

Add any images you use for your page in `/docs/img/mechanism-examples/[category]/[example]/`.

### Adding an Image for the Example

Check the category's .meta.yml for the default card layout (tall or wide). This will be the orientation of the 1:1.545 image you will use for the mechanism example.

1:1.545 is the aspect ratio of a picture outputted from Onshape's "print" function using the "tabloid" paper size. You can select landscape or portrait from there for wide or tall. 

!!! Tip
    For images you already have, you can use GIMP and a calculator to crop an image by adding pixels to get it to the desired aspect ratio.

## Adding Pages to Site Navigation

Any new pages added have to be added to the site navigation.

Follow the standard formatting presented in the `mkdocs.yml file` to add more pages, categories, and landing pages as necessary:

``` yml title="mkdocs.yml"
 - Mechanism Examples:
      - mechanism-examples/index.md
      - Drivebases:
        - mechanism-examples/drivebase/index.md
        - 2910's Charged Up Drivebase: mechanism-examples/drivebase/2910_2023_dt.md
        - 972's Brainpan Drivebase: mechanism-examples/drivebase/972_2024_dt.md
      - Shooters:
        - mechanism-examples/shooter/index.md
        - Andrew's Hyperhive Shooter: mechanism-examples/shooter/small.md
        - 1678's Rapid React Shooter: mechanism-examples/shooter/citrus.md
      - Slapdown Intakes:
        - mechanism-examples/intake/slapdown/index.md
        - 4414-Style Intake: mechanism-examples/intake/slapdown/4414style.md
        - Washed Beavertail Intake: mechanism-examples/intake/slapdown/washed.md
        - Low Pivot Slapdown Intake: mechanism-examples/intake/slapdown/low.md
        - 6423's Crescendo Slapdown Intake: mechanism-examples/intake/slapdown/6423otb.md
      - 4 Bar Intakes:
        - mechanism-examples/intake/4bar/index.md
        - 1678's Rapid React Intake: mechanism-examples/intake/4bar/1678.md
        - Andrew's Four-Bar Intake: mechanism-examples/intake/4bar/clean.md
        - Vaughn's Four-Bar Intake: mechanism-examples/intake/4bar/vaughn4bar.md
```
As you can see, the formatting goes:

``` yml
- Mechanism Examples:
    - mechanism-examples/index.md
    - Category 1:
        - link-to-category-landing-page
        - Mechanism 1: link-to-mech-1-page
        - Mechanism 2: link-to-mech-2-page
```

Thanks for your contribution!

<br>