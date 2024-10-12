#!/bin/bash
# A trivial wrapper for build_animations.py
source venv/bin/activate
exec "python3" "-m" "build_animations" "$@"
