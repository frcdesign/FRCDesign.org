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
### Install Prerequisites
Make sure to download the correct versions for the OS that you have (Windows, Mac, or Linux).

Windows installers will almost always need to be the 64-bit version if there is a distinction.

- The latest version of [Git Bash](https://git-scm.com/downloads)
    - Follow instructions for your OS
    - Use all default options for installation
- [Python 3.10.6](https://www.python.org/downloads/release/python-3106/) 
    - When the installer opens, make sure to select "Add Python 3.10 to PATH" at the bottom and click "Install Now"
    - For Windows users, you have the option of disabling the PATH length limit at the end; this can be helpful for other projects but is not required for contributing to the website
- [VSCode](https://code.visualstudio.com/)
    - Download the stable build for your OS
    - Use all default options for installation, except creating a desktop icon if you want
- [GitHub Desktop](https://desktop.github.com/)
    - After installing, select "Sign in to GitHub.com"
    - Sign in or sign up for a new GitHub account, then click "Authorize Desktop"
        - If you choose to sign up, you must verify your account with a captcha at the end of the registration and an emailed code
        - If the captcha fails, try disabling a privacy extension that might be interfering
        - Set up the rest of your account (you may choose to sign up for GitHub education but that isn't required, the free version is fine)
        - If it doesn't take you to the authorization page after signing up, go back to the GitHub Desktop application, press "Cancel", the select "Sign in to GitHub.com" again
    - Allow your browser to open GitHub Desktop
    - Click "Finish"
    

### Steps for Public Contributors

1. 

### Steps for Internal Contributors (added to the main repository)

2. To clone the github repositoryy right click your desktop and select "Git Bash Here"
- From there you can execute ```git clone https://github.com/davidsdesignserver/dds-manual.git```
- Close the current git bash window and open the cloned folder. It should be named "docs"
- Right click in this folder and open git bash again.

### How to Get Local Preview Running:
- Execute ```py -m venv venv```
- Open the runlocal.sh file with git bash (./runlocal.sh)
- If everything went smoothly it should say its "Serving on" something like ```http://127.0.0.1:5800```
- This is a local hosted version of the website you use to have a live preview of the site while editing.
- You can now open the "docs" folder inside of VSCode
- The local preview of the site only updates when you save files, so turn on vscode auto save.
- Once inside you should be able to navigate to the bottom left branch icon and create a new branch to start working in.
- Commits to branches other than main will not regenerate the site
- Do not push to main without permission

### Git Lingo

