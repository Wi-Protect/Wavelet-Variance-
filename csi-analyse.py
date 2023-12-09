import pandas as pd

chunk_size = 10
file_path = './csi_data.csv'

# Read the file in chunks of 10 lines
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Process each chunk of data
    print(chunk)
