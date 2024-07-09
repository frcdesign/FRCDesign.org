source venv/scripts/activate 
pip install git+https://${INSIDERS}@github.com/squidfunk/mkdocs-material-insiders.git
pip install -e mkdocs-material
pip install mkdocs-glightbox
pip install mkdocs-git-revision-date-localized-plugin
pip install pymdown-extensions pyyaml
pip install mkdocs-git-committers-plugin-2
pip install "mkdocs-material[imaging]"
mkdocs serve
