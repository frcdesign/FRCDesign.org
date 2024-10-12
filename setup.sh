#!/bin/bash

# install manim dependencies
# Install add-apt-repository
# sudo apt-get update
# sudo apt-get install -y software-properties-common
# Get python repo
# sudo add-apt-repository -y ppa:deadsnakes/ppa
# sudo apt-get update
# sudo apt-get install -y python3.12-dev
# Manim dependencies
# sudo apt-get install -y build-essential libcairo2-dev libpango1.0-dev ffmpeg 

# Optional manim dependencies
# texlive texlive-latex-extra

# Pillow dependencies
# sudo apt-get install -y libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    # libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    # libharfbuzz-dev libfribidi-dev libxcb1-dev

# install pip requirements
# Use sudo to get access to filesystem
# Note: Do not use --root-user-action to disable sudo warning since Github Actions's pip doesn't support it
pip install .