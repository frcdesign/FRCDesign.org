---
title: Style Guide
description: The style guide for contribution according to the goals of the website.
---

# Contribution Style Guide

## Futureproofing and Usefulness

To make the content you write useful for teams of all resource levels, while maintaining validity in the future, the goal isn’t to go broad and shallow, but rather to go extra deep so you can equip students with the understanding of the underlying fundamentals behind concepts which they can then apply to their own unique situations. Pros and cons are context dependent while fundamentals are universal.

At the same time, things that aren’t easily accessible and/or commonly used by teams, like billet chassis and ball drive, shouldn’t be included to prevent confusion.

On the other hand, including small details that you’d only discover through actually making the thing tends to be a lifesaver for everyone (such as electrical taping cat-tongue tape to make it not peel).

### Why is this important?

1. We don’t need to figure out the pros and cons of everything for students to make a decision. New products come out all the time, and equipping them with the skills lets students find creative solutions that no one would think of for their circumstances.

2. This enables students to understand WHY a team would make a certain decision and figure out tradeoffs without us explicitly telling them.

3. It makes it significantly less intensive to future proof and maintain. If the meta shifts, having to redo sections to stay competitive is time consuming. If the project dies and is no longer maintained, the information stays useful for way longer.

4. The small details are often the experience gap between the most reliable successful robots and not. It’s a lifesaver for teams without experience, and reduces the review workload on design mentors with experience.

### To make this easier, here are a few tips:

1. You can usually find extremes for each concept to make it more obvious. (stealth wheels vs brass flywheels for inertia.)

2. It may be useful to find one or two meta team applications and figure out what fundamental trade offs are made for that decision. This helps learners understand how these concepts relate to each other. This also applies to mechanism examples.

3. “how to cad xyz” and IRL nuances are very useful for certain applications. Examples include sketching linkages or tensioner placement depending on load.

## Inspired by gm0's Style Guide

Don’t deal in absolutes.

- Only a Sith deals in absolutes
- Use pros/cons lists to compare options
- Explain WHY something is good or bad
  - For example, we all know deadaxle pivots are better than liveaxle. But don’t just say they’re better, say: "Deadaxles have a higher second moment of area as the torque being directly transferred to the part. As a result your pivot is significantly more robust and less prone to breaking.
    ”
  - Similarly, we know the Kraken motors are generally good. But explain why they are good, e.g. “We would recommend using Krakens on your drivetrain because they are extremely high torque motors and will improve your acceleration. In addition, they have integrated Talon FX motor controllers that make them easier to wire and feature a high resolution encoder which will help the precision of your swerve odometry. Keep in mind that Kraken motors are not yet compatible with stock REV Maxswerve modules and require an extra adaptor from WCP to mate with other existing modules.”
- Still emphasize that teams are free to explore and innovate, but help set realistic expectations (see the following point)

FRCDesign.org is a guide **from a competitive standpoint**.

- Try to leave out stuff that doesn’t work well and is unpopular; if it is popular it is worth explaining the disadvantages (See tank drive vs mecanum drive; explaining tank drive, as a relatively popular and simple drivetrain makes sense, but mecanum drive, a drivetrain that no longer makes sense in the era of swerve and has little-to-no pushing power or traction.)
- Try to leave opinions out as much as possible. Do not speak authoritatively on stuff you do not have first-hand experience with whenever possible

Keep in mind that FRC design trends are temporary and transient.

- Just because something is popular one season doesn’t mean it’s the end all be all. There was a time when WCD and sheet metal superstructures was all the rage, but that doesn’t mean that we should recommend them in this guide. Try your best to think about why something is popular, and what benefits in design, function, and execution they actually bring to the table.

<!-- Adding examples of mechanisms really helps with knowledge transfer.

Credit the teams: Caption Format is: [Team Number] [Team Name], (Relevant Accomplishment), [Season], (description)

[]s mean all the time, ()s means when relevant

If you have multiple pictures by the same part from the same team only credit them on the last one to avoid repetition.

Examples

11115 Gluten Free, Finalist Alliance Captain (Detroit), Relic Recovery, springloaded

8417 ‘Lectric Legends, Rover Ruckus, TPU intake flaps

7236 Recharged Green, Rover Ruckus, Misumi SAR3 -->

## Standards

### File Formats:

- Compress images to .webp format using [squoosh](https://squoosh.app/ "sqoosh Image Compressor"){:target="\_blank"}
- Embed longer videos using a Youtube embed, and shorter videos with a webm file
- Add images by using `<center><img src="absolute link" width="x%"></center>`

### Brand Standards

Adhere to brand standards when possible.

- Abide by FIRST® Trademark guidelines, available [here](https://www.firstinspires.org/sites/default/files/uploads/resource_library/UseofUSFIRSTandLEGOGroupTrademarksandCopyrightedMaterials.pdf "FIRST Trademark Guidelines"){:target="\_blank"}
- The first instance of _FIRST_ and FRC on a page should include ® (i.e, FIRST®)
- Always capitalize and italize the name _FIRST_
- Do NOT use a possessive on the _FIRST_ name (e.g, FIRST’s)
<!-- It’s gm0 not GM0 damn it; look at the logo. -->
- This also applies to team names: spell them how they are officially spelled
- Check [The Blue Alliance](https://www.thebluealliance.com/ "The Blue Alliance"){:target="\_blank"} if you don't know how to spell a team's name

You can use “you” when writing, when it makes writing less awkward. However, try avoiding excessively using it.

### Links:

- External links should open in a new tab: `[Link Text](link_url "Link Title"){:target="_blank"}`
  - Links to CAD documents should use a large centered button: `<center markdown>[Link Text](link_url "Link Title"){:target="_blank" .md-button .md-button--primary}</center>`
  - Link titles for Onshape documents should be `[Document name] Onshape Document`
- Internal links should open in the current tab and use a relative link: `[Link Text](relative_link "Link Title")`
  - Link titles for internal links should be in the format: `"[Page Name] Page"`

<br>
