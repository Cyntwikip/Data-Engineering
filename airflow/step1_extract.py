import pandas as pd

def extract(source_url: str, output_file: str) -> None:
    print("Extracting data from source...")
    columns = ['A' + str(i) for i in range(1, 17)]
    df = pd.read_csv(source_url, names=columns)
    df.to_csv(output_file, index=False)
    print(f"Data extracted and saved to {output_file}")