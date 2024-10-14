---
title: Methods of Contributing
description: A guide to publically contributing to the website, including setting up an IDE and local preview for editing.
---

# Methods of Contributing

## Public Contribution
Anyone can create content for the website without markdown knowledge or github, though it is preferred you learn how to use both to lessen the workload of other contributors.

In [the discord server](https://discord.gg/jHXTdNjYCg "FRC Design Discord Server"){:target="_blank"}, go to the ["website-discussion" channel](https://discord.com/channels/1120162219502608426/1233961750639018104 "#website-discussion Discord Channel"){:target="_blank"} and ask if you can contribute the thing you want to by filling out this template:

    Issue/content:
    Solution or Notes about the execution of the content:
    When do you plan on finishing?:
    Using an alternate platform or forking on Github?:

This is to make sure you don't waste your time if it's not something that won't get put on the website or something that someone has already started working on.

If you're given approval to start working on it, an internal contributor will make a new post in the ["public-website-contribution" forum channel](https://discord.com/channels/1120162219502608426/1233993910817259663 "#public-website-contribution Discord Forum Channel"){:target="_blank"} or direct you an existing post to work with and supplement another contributor if the content or issue has already started to be addressed.

When you start on your work, you may choose to either:

1. Fork the repository on Github and submit pull requests for your work to be accepted (if you're more programming-savvy)
2. Work on an alternate platform such as Google Docs or Notion and let an internal contributor port it over to the website when you're done

## Setting up Github and VS Code For Contributing
### Install Prerequisites
Make sure to download the correct versions for the OS that you have (Windows, Mac, or Linux).

Windows installers will almost always need to be the 64-bit version if there is a distinction.

- The latest version of [Git Bash](https://git-scm.com/downloads "Git Bash Download"){:target="_blank"}
    - Follow instructions for your OS
    - Use all default options for installation
- [Python 3.10.6](https://www.python.org/downloads/release/python-3106/ "Python 3.10.6 Download"){:target="_blank"}
    - When the installer opens, make sure to select "Add Python 3.10 to PATH" at the bottom and click "Install Now"
    - For Windows users, you have the option of disabling the PATH length limit at the end; this can be helpful for other projects but is not required for contributing to the website
- [VSCode](https://code.visualstudio.com/ "VSCode"){:target="_blank"}
    - Download the stable build for your OS
    - Use all default options for installation, except creating a desktop icon if you want
- [GitHub Desktop](https://desktop.github.com/ "Github Desktop"){:target="_blank"} (Optional - you can also use git interface in VSCode)
    - After installing, select "Sign in to GitHub.com"
    - Sign in or sign up for a new GitHub account, then click "Authorize Desktop"
        - If you choose to sign up, you must verify your account with a captcha at the end of the registration and an emailed code
        - If the captcha fails, try disabling a privacy extension that might be interfering
        - Set up the rest of your account (you may choose to sign up for GitHub education but that isn't required, the free version is fine)
        - If it doesn't take you to the authorization page after signing up, go back to the GitHub Desktop application, press "Cancel", the select "Sign in to GitHub.com" again
    - Allow your browser to open GitHub Desktop
    - Click "Finish"
    

### Steps to Start Writing Contributions

**For Public Contributors:**

1. Go to [the repository website](https://github.com/davidsdesignserver/FRCDesign.org "FRC Design Github Repository"){:target="_blank"}
2. Click "Fork" near the top right, then click "Create Fork" on the next screen
3. Open GitHub Desktop and select "Clone a repository from the Internet..." or go to ```file -> Clone repository...``` in the very top left
4. Under "GitHub.com", select your forked ```[username]/FRCDesign.org``` repository  and click "Clone"
5. After it clones the repository (downloads a copy of it to your computer), it will ask how you plan to use the fork. Select "To contribute to the parent project" and click "Continue"

**For Internal Contributors (added to the main repository):**

1. Open GitHub Desktop and select "Clone a repository from the Internet..." or go to ```file -> Clone repository...``` in the very top left
2. Under "GitHub.com", select the ```davidsdesignserver/FRCDesign.org``` repository and click "Clone"
3. After it clones the repository (downloads a copy of it to your computer), it will ask how you plan to use the fork. Select "To contribute to the parent project" and click "Continue"

**How to Write and Pull Request Contributions**

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

    !!! tip
        All the website files and folders are contained in the ```docs``` folder, except the ```mkdocs.yml``` file which contains the directory for the sidebar of the website

6. Whenever you reach a good point to stop where you want to save your changes to the cloud, you want to make what's called a "commit", which is where the changes are saved to the branch. You then have to "push" any commits to get them uploaded to the cloud, otherwise they will remain local. You can do this through VS Code or GitHub Desktop, but we'll go through GitHub Desktop to keep all version control actions centralized there.
7. Open Github Desktop and make sure "Changes" on the sidebar is selected. All changes selected in the sidebar will be added to the commit (the changes are "staged" for the commit). Type a summary of the commit (description optional) and press "Commit to [branch]".
8. Click the button to push the commit(s) you've made to the cloud (either up above or in the middle of the screen).

    !!! tip
        Clicking the "Fetch origin" button will fetch any commits to the current branch that anyone else has made and pushed to the cloud

9. To keep your code up to date with the original repository's main branch, open the "branch" menu at the top of the screen and click "Update from main". If some commits get pulled to your branch from main, you can push to update your branch in the cloud again.

    !!! tip
        Make sure to update your branch from main frequently! If you don't, you may have to resolve big conflicts between your changes and changes someone else made to main. If you encounter conflicts, just follow the prompts in GitHub Desktop to open the conflicts in VS Code and solve them there. Once all conflicts are resolved, switch back to GitHub Desktop to complete the merge.

10. Once you're satisfied enough with your set of changes to request to add them to the main website, and have committed all changes, checked for updates, and pushed all commits, create a pull request through the menu in the middle of GitHub Desktop. This will bring you to the website where you can describe the changes you made and want to pull to the website and assign an issue that it will fix. One of the internal contributors will review your pull request after you submit it and will either approve it and merge it with the main branch or make comments about things that need fixed before it can get merged.

To recap the contribution steps, do the combination of creating and publishing a branch, making changes and commits, updating from main, pushing commits, and creating a pull request.


### How to Get The Local Preview of the Website Running
You can get a local hosted version of the website to have a live preview of the site while editing.

1. Open the repository in VS Code (doesn't matter which branch)
2. Toggle the bottom panel on if there isn't one with the shortcut ```Ctrl + J```
3. Click the dropdown next to the + on the top righthand side of the bottom panel and click "Git Bash"
4. Run the command ```py -m venv venv``` to create a virtual environment (FIRST TIME)
5. Run the command ```./installdependencies.sh``` to install all needed python packages (FIRST TIME)
6. Run the command ```./runlocal.sh``` to start the server
7. If everything went smoothly it should say its "Serving on" something like ```http://127.0.0.1:8000```

Make sure to run ```./runlocal.sh``` in Git Bash every time you open VS Code to edit.

!!! Tip
    After clicking on the terminal in the bottom panel, you can use Ctrl + C to terminate the local website hosting.

!!! Note
    When you switch branches using GitHub Desktop, the local preview will follow without any problems

