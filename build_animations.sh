#!/bin/bash
# A trivial wrapper for build_animations.py
source .venv/bin/activate
exec "python" "-m" "animations.build_animations" "$@"
