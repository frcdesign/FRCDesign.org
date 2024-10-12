#!/bin/bash

# install manim dependencies
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y build-essential python3.12-dev libcairo2-dev libpango1.0-dev ffmpeg 
# Optional manim dependencies
# texlive texlive-latex-extra

# Pillow dependencies
sudo apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev

# install pip requirements
pip install -r requirements.txt

# add the robot concepts helper library so we can import it anywhere
# this will install any packages specified in setup.py
pip install -e .