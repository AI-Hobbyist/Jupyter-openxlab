import sys
from jupyter_core.command import main

sys.argv = [
    "jupyter",
    "lab",
    "--ip=0.0.0.0",
    "--port=7860",
    "--allow-root",
    "--no-browser",
]

main()
