from pathlib import Path
import os

# Get the current path and the mapreduce paths
current_dir = os.getcwd()
all_paths = Path(current_dir).glob("**/*")
all_mapreduce_paths = [x for x in all_paths if (x.is_file() and x.stem in ["mapper", "reducer"])]

# Make mapreduce paths executable
for pth in all_mapreduce_paths:
    os.system(f"chmod +x {pth}")