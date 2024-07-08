source venv/scripts/activate 
pip install mkdocs-material
pip install mkdocs-glightbox
pip install mkdocs-git-revision-date-localized-plugin
pip install mkdocs-git-committers-plugin-2
pip install pymdown-extensions pyyaml
export GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
python generate_mkdocs_config.py
mkdocs serve
