# How to contribute to the docs

# Prerequisites
- [Git Bash](https://git-scm.com/downloads)
- [Python 3.10.6](https://www.python.org/downloads/release/python-3106/)
- [VSCode](https://code.visualstudio.com/)

# Steps
- To clone the github reposity right click your desktop and select "Git Bash Here"
- From there you can execute ```git clone https://github.com/davidsdesignserver/docs.git```
- Close the current git back window and open the cloned folder. It should be named "docs"
- Right click in this folder and open git bash again.
- Execute ```python -m venv venv```
- Execute ```source venv/scripts/activate```
- Execute ```pip install mkdocs-material```
- Execute ```mkdocs serve```

- If everything went smoothly it should say its "Serving on" something like ```http://127.0.0.1:5800```
- This is a local hosted verson of the website you use to have a live preview of the site while editing.
- You can now open the "docs" folder inside of VSCode
- Once inside you should be able to navigate to the bottom left branch icon and create a new branch to start working in.
- Commits to branches other than main will not regenerate the site
- Do not push to main without permission
