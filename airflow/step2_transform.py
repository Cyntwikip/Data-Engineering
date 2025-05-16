import pandas as pd

def transform(input_file: str, output_file: str) -> None:
    print("Transforming data...")
    df = pd.read_csv(input_file)
    # Example transformation: Drop rows with missing values
    df = df.dropna()
    # Rename columns for clarity
    df.columns = [f"Feature_{i}" for i in range(1, len(df.columns) + 1)]
    df.to_csv(output_file, index=False)
    print(f"Data transformed and saved to {output_file}")