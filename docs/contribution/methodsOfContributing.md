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
### Prerequisites
- [Git Bash](https://git-scm.com/downloads)
- [Python 3.10.6](https://www.python.org/downloads/release/python-3106/)
- [VSCode](https://code.visualstudio.com/)
- [GitHub Desktop](https://desktop.github.com/)

### Steps
- To clone the github repositoryy right click your desktop and select "Git Bash Here"
- From there you can execute ```git clone https://github.com/davidsdesignserver/dds-manual.git```
- Close the current git bash window and open the cloned folder. It should be named "docs"
- Right click in this folder and open git bash again.
- Execute ```py -m venv venv```
- Open the runlocal.sh file with git bash (./runlocal.sh)
- If everything went smoothly it should say its "Serving on" something like ```http://127.0.0.1:5800```
- This is a local hosted version of the website you use to have a live preview of the site while editing.
- You can now open the "docs" folder inside of VSCode
- The local preview of the site only updates when you save files, so turn on vscode auto save.
- Once inside you should be able to navigate to the bottom left branch icon and create a new branch to start working in.
- Commits to branches other than main will not regenerate the site
- Do not push to main without permission
