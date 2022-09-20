from PyOS.core import Configure

Configure(
    run_file="./run.py",
    # OS settings
    name="anOS",
    default_bios = [],
    default_user = "root",
    run_after_seconds = 1
)

# This file is the main entry point for your OS.