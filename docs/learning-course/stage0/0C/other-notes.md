# 0C: Navigating Onshape

## Other Notes

### Organization Practices
One of the big reasons Onshape is desirable for FRC is its collaboration capabilities, but that means nothing when nobody can read or work with your CAD. Different subsystem leads will have to collaborate and view other separate subsystems. None of the easy communication and collaboration can be done without good organization and naming practices.

Make it annoyingly clear what sketches and features do what. Name sketches and features, and try to use folders. Sort by parts or groups of parts (e.g. tubes, gussets, bellypan). The instance list in assemblies can also get very messy and slow down your workflow, so keep similar instances in folders. And finally, just make sure to name tabs. This will all make a big difference for the readability of your CAD by other people and yourself.

### Assemblies
Assemblies are an important part of Onshape. They are where all of the parts get put together. They can be very slow and difficult to modify if not done correctly. 

When creating an assembly, it's important to create a new assembly for each separate moving component, and then link them together in a main subsystem assembly, and then again in a main robot assembly.. This will make you model easier to work with and reduce lag.

### Versions and History
Every action by every user is saved in the history, and can be rolled back to or created a version at. When assemblies are linked between documents, documents have to be versioned. This reduces loading times as well, since it's only referencing a single static version and not constantly attempting to update. Versions cannot be deleted, and branches can be created and merged for changes, similar to git.

<br>