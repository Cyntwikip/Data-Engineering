import pandas as pd
import os, shutil

def load(input_file: str, output_file:str) -> None:
    print("Copying file from input to output folder...")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    # Copy the file
    shutil.copy(input_file, output_file)

    print(f"File copied to '{output_file}'")