#!/bin/bash

# install manim dependencies
# Add add-apt-repository
sudo apt-get install -y software-properties-common
# Get python repo
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
# Install dev python and other versions
sudo apt-get install -y build-essential python3.10-dev libcairo2-dev libpango1.0-dev ffmpeg 

# Optional manim dependencies
# texlive texlive-latex-extra

# Pillow dependencies
sudo apt-get install -y libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev

# install pip requirements
pip install --editable .