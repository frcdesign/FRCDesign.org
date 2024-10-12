# https://github.com/devcontainers/images/tree/main/src/python
FROM mcr.microsoft.com/devcontainers/python:dev-3.12

# Add sudo so setup.sh runs correctly
# Also install some developer convenience utilities
RUN apt-get update && apt-get install -y sudo man vim less
RUN apt-get update

# add build.sh alias to .bashrc
# for some reason source is not a valid command, so use . instead
# ARG WORKSPACE
# RUN echo alias build=\"bash ${WORKSPACE}/build.sh\" >> ~/.bashrc && . ~/.bashrc