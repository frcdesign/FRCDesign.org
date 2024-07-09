source venv/scripts/activate 
pip install mkdocs-material
pip install mkdocs-glightbox
pip install mkdocs-git-revision-date-localized-plugin
pip install pymdown-extensions pyyaml
pip install "mkdocs-material[imaging]"
export GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
python generate_mkdocs_config.py
mkdocs serve
