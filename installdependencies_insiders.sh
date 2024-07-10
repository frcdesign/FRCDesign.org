# You must run this with the Git for Windows SDK shell, navigating to the cloned repository (cd ~/Documents/GitHub/[repository name]) and run ./installdependencies_insiders.sh
# After installing the Git SDK, check the version of python with py --version and make sure it's 3.12.4. If it's not, install python 3.12.4 from the Windows Store and check again.

# Create the file with your token
echo "Enter the token for INSIDERS access:"
read INSIDERS
echo "INSIDERS=$INSIDERS" >> .env


# Installing python, git, and gcc
echo
echo Installing python and pip
pacman -Syu  # Update package database and core system packages
pacman -S python3-pip
pacman -S python-devel
pacman -S base-devel mingw-w64-x86_64-toolchain mingw-w64-x86_64-python3-setuptools mingw-w64-x86_64-python3-cffi

#Installing git, gcc, and zlib
echo
echo "Installing git, gcc, and pillow dependencies"
pacman -S git
pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-zlib mingw-w64-x86_64-libjpeg-turbo mingw-w64-x86_64-libpng mingw-w64-x86_64-freetype mingw-w64-x86_64-lcms2 mingw-w64-x86_64-libimagequant mingw-w64-x86_64-libraqm mingw-w64-x86_64-tcl mingw-w64-x86_64-tk mingw-w64-x86_64-libwebp
echo 'export PATH="/mingw64/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
export PKG_CONFIG_PATH="/mingw64/lib/pkgconfig:$PKG_CONFIG_PATH"
export CFLAGS="-I/mingw64/include"
export LDFLAGS="-L/mingw64/lib"

# Creating a virtual environment
echo
echo "Creating a virtual environment"
rm -rf venv
py -m venv venv
source venv/scripts/activate 

#Installing mkdocs-material
echo
echo "Installing mkdocs-material"
venv/scripts/pip install mkdocs-material

#Installing the Insiders Edition of mkdocs-material
echo
echo "Installing the Insiders Edition of mkdocs-material; it may take a while"
venv/scripts/pip install git+https://${INSIDERS}@github.com/davidsdesignserver/mkdocs-material-insiders.git

#Installing the rest of the plugin stuff
echo
echo "Installing the rest of the plugin stuff"
venv/scripts/pip install mkdocs-glightbox
venv/scripts/pip install mkdocs-git-revision-date-localized-plugin
venv/scripts/pip install pymdown-extensions pyyaml
venv/scripts/pip install "mkdocs-material[imaging]"
venv/scripts/pip install mkdocs-git-committers-plugin-2
pacman -S mingw-w64-ucrt-x86_64-pngquant
