# Methods of Contributing

## Public Contribution
Anyone can create content for the website without markdown knowledge or github, though it is preferred you learn how to use both to lessen the workload of other contributors.

In [the discord server](https://discord.gg/jHXTdNjYCg), go to the ["website-feedback" channel](https://discord.com/channels/1120162219502608426/1233961750639018104) and ask if you can contribute the thing you want to by filling out this template:

    Issue/content:
    Solution or Notes about the execution of the content:
    When do you plan on finishing?:
    Using an alternate platform or forking on Github?:

This is to make sure you don't waste your time if it's not something that won't get put on the website or something that someone has already started working on.

If you're given approval to start working on it, an internal contributor will make a new post in the ["public-website-contribution" forum channel](https://discord.com/channels/1120162219502608426/1233993910817259663) or direct you an existing post to work with and supplement another contributor if the content or issue has already started to be addressed.

When you start on your work, you may choose to either:

1. Fork the repository on Github and submit pull requests for your work to be accepted (if you're more programming-savvy)
2. Work on an alternate platform such as Google Docs or Notion and let an internal contributor port it over to the website when you're done

## Setting up Github and VS Code For Contributing

1. Install [Visual Studio Code](https://code.visualstudio.com/).

    - This should not be confused with Visual Studio, which has a Purple logo and is a different Microsoft product.
    - Download the stable build for your OS
    - Use all default options for installation, except creating a desktop icon if you want

2. Contributing involves managing and saving to an online copy of the website files saved on GitHub called a **repository**. Decide how you want to interact with your repository:

    - **GitHub Desktop** uses a graphical menu with nice buttons to achieve all the different needed functions to interact with your repository. This requires a separate download but can be more intuitive for people newer to programming to access. Viewing commit (save) history and managing conflicts can also be made easier through this program. There is a tutorial for using GitHub Desktop lower on this page.

    - Instead of GitHub Desktop, you can choose to just use **VS Code**'s native git functions instead. This can lead to a faster workflow once you get it down, but can be less intuitive as it's all command- and text-based.

3. Start by creating a GitHub account if you don't already have one.
    - If you choose to sign up, you must verify your account with a captcha at the end of the registration and an emailed code
    - If the captcha fails, try disabling a privacy extension that might be interfering
    - Set up the rest of your account (you may choose to sign up for GitHub education but that isn't required, the free version is fine)

4. Create a 'fork' of the original repository. *Disregard if you are an internal contributor and have edit access to the original repository*
    - Go to [the repository website](https://github.com/frcdesign/FRCDesign.org)
    - Click "Fork" near the top right, then click "Create Fork" on the next screen
    - Forking a repository means create a branch of the original website repository owned by you. You make your changes here, submit your changes to be reviewed, then they get merged into the original website repository.

5. Now 'clone' the repository to your computer.
    - Cloning a repository just means creating a copy of the repository's files on your computer for you to edit or run

=== "GitHub Desktop"

    **Set Up GitHub Desktop**

    1. Install [GitHub Desktop](https://desktop.github.com/)
    2. After installing, select "Sign in to GitHub.com"
    3. Sign in with your GitHub account
    4. Allow your browser to open GitHub Desktop
    5. Click "Finish"

    **Clone the Repository**

    1. Open GitHub Desktop and select "Clone a repository from the Internet..." or go to ```file -> Clone repository...``` in the very top left.
    2. Under "GitHub.com", select the repository (your forked ```[username]/FRCDesign.org``` repository) and click "Clone".
    3. After it clones the repository (downloads a copy of it to your computer), it will ask how you plan to use the fork. Select "To contribute to the parent project" and click "Continue".
    4. Click "Open in Visual Studio Code" on the homepage or under the `Repository` menu at the top.

=== "VS Code"

    1. Sign in to GitHub in VS Code by clicking the profile icon in the bottom left corner
        - Follow the prompts in your browser to sign in
    2. Open the Command Palette in VS Code (`Ctrl + Shift + P` or `F1` in some cases)
    3. Search for and select "Git: Clone"
    4. Type or paste the url to the repository you made by forking.
    5. Select where you want to clone the repository with the file explorer
    6. Open the folder you just cloned onto your computer using either the pop-up that shows up after it's finished cloning or `File > Open Folder`

### Setting Up a Local Preview With Docker

1. Install the "Dev Containers", and "Docker" extensions in VS Code. This can be done by clicking on the extensions icon on the left side of the screen, searching for the extension, and clicking install.

2. Install Docker Desktop, either from [the website](https://www.docker.com/) or by searching for `Dev Containers: Install Docker` in the Command Palette (`Ctrl + Shift + P` or `F1` in some cases).
    - The installation process will require you to restart your computer

    - When opening Docker for the first time, you will be asked to "Sign in." You don't need to create an account; you can hit the skip button instead and it will still work.

3. Open Docker Desktop and VS Code.

4. In VS Code, open the Command Palette and search for and select `Dev Containers: Reopen in Container`.
    - If you open VS Code after opening Docker, a pop-up may show up in the bottom right asking if you want to reopen VS Code in a container. This also works.
    - VSCode should re-open inside a dev container. Note this may take a few minutes the first time you do it, but will be much faster on subsequent loads.

5. Launch a local version of the website by pressing `Ctrl + Shift + B` (this runs the 'development' VS Code Task), then opening [localhost:8000](http://localhost:8000/) in your browser. 

6. Make edits to `.md` files in `/docs` to contribute. Any changes you make should be reflected in the version of the website running on your browser.

7. Use `Ctrl + C` to force the locally hosted website to stop when you're done.

TIP: After clicking on the terminal in the bottom panel, you can use Ctrl + C to terminate the local website hosting.

### Review/Summary of Steps to Repeat After Setup is Complete

1. Open Docker Desktop
2. Open VS Code (through either GitHub Desktop or just normally)
3. Make sure the folder/workspace is open and it connects to the dev container.
    - Sometimes it will automatically open the previous workspace it was last in and try to connect to the dev container. This will fail if Docker Desktop is not open.
    - If the repository folder does not automatically open in VS Code, open it manually and run the `Dev Containers: Reopen in Container` command.
    - GitHub Desktop will open VS Code in the current repository and branch selected
4. Use the `Ctrl + Shift + B` keyboard shortcut to run the local preview.
5. Open the local preview in your browser.
6. Start editing.

NOTE: When you switch branches using GitHub Desktop or VS Code, the your files and local preview will follow without any problems.

## How to Write and Pull Request Contributions

1. Create a new branch by going to the "Current branch" dropdown at the top of GitHub Desktop, pressing "New branch", naming it and clicking "Create branch".
    - Typically you want to make changes in branches (not main), then do what's called a "pull request" to get those changes "pulled" and merged over to the original main branch
    - Name the branch something related to the overall changes you're making, e.g. "contributors-guide" or "3A-cleanup". You should expect to delete the branch after a pull request, so keep it specific enough to your changes
    - Make sure to publish the branch by clicking the button for it that shows up after you create a new branch
2. Click "Open in Visual Studio Code" to open VS Code.
3. If you get a pop-up that says "Do you trust the authors of the files in this folder?", check the box next to "Trust the authors of all files in the parent folder 'GitHub'" (for no further popups when you clone repositories in the future) and click "Yes, I trust the authors".
4. Set up VS Code how you like if this is your first time running it (themes, extensions).
    - The "Code Spell Checker" extension is suggested
    - Enable autosave in the ```file``` menu by toggling it on
5. Make a set of changes.
    - All the website files and folders are contained in the ```docs``` folder, except the ```mkdocs.yml``` file which contains the directory for the sidebar of the website

6. Whenever you reach a good point to stop where you want to save your changes to the cloud, you want to make what's called a "commit", which is where the changes are saved to the branch. You then have to "push" any commits to get them uploaded to the cloud, otherwise they will remain local. You can do this through VS Code or GitHub Desktop, but we'll go through GitHub Desktop to keep all version control actions centralized there.
7. Open Github Desktop and make sure "Changes" on the sidebar is selected. All changes selected in the sidebar will be added to the commit (the changes are "staged" for the commit). Type a summary of the commit (description optional) and press "Commit to [branch]".
8. Click the button to push the commit(s) you've made to the cloud (either up above or in the middle of the screen).
    - Clicking the "Fetch origin" button will fetch any commits to the current branch that anyone else has made and pushed to the cloud

9. To keep your code up to date with the original repository's main branch, open the "branch" menu at the top of the screen and click "Update from main". If some commits get pulled to your branch from main, you can push to update your branch in the cloud again.
    - Make sure to update your branch from main frequently! If you don't, you may have to resolve big conflicts between your changes and changes someone else made to main. If you encounter conflicts, just follow the prompts in GitHub Desktop to open the conflicts in VS Code and solve them there. Once all conflicts are resolved, switch back to GitHub Desktop to complete the merge.

10. Once you're satisfied enough with your set of changes to request to add them to the main website, and have committed all changes, checked for updates, and pushed all commits, create a pull request through the menu in the middle of GitHub Desktop. This will bring you to the website where you can describe the changes you made and want to pull to the website and assign an issue that it will fix. One of the internal contributors will review your pull request after you submit it and will either approve it and merge it with the main branch or make comments about things that need fixed before it can get merged.

To recap the contribution steps, do the combination of creating and publishing a branch, making changes and commits, updating from main, pushing commits, and creating a pull request.


<!-- ### How to Get The Local Preview of the Website Running
You can get a local hosted version of the website to have a live preview of the site while editing.

1. Open the repository in VS Code (doesn't matter which branch)
2. Toggle the bottom panel on if there isn't one with the shortcut ```Ctrl + J```
3. Click the dropdown next to the + on the top righthand side of the bottom panel and click "Git Bash"
4. Run the command ```py -m venv venv``` to create a virtual environment (FIRST TIME)
5. Run the command ```./installdependencies.sh``` to install all needed python packages (FIRST TIME)
6. Run the command ```./runlocal.sh``` to start the server
7. If everything went smoothly it should say its "Serving on" something like ```http://127.0.0.1:8000```

Make sure to run ```./runlocal.sh``` in Git Bash every time you open VS Code to edit.

Tip: After clicking on the terminal in the bottom panel, you can use Ctrl + C to terminate the local website hosting.

Note: When you switch branches using GitHub Desktop, the local preview will follow without any problems -->