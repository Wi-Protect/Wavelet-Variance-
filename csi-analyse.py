import pandas as pd

chunk_size = 10
file_path = './csi_data.csv'

# Read the file in chunks of 10 lines
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Process each chunk of data
    # print(list(chunk['amplitude1']))
    
    csis = []
    for i in range(64):
        amplitudes = []
        phases = []
        amplitudes = (list(chunk['amplitude'+str(i+1)]))
        phases = (list(chunk['phase'+str(i+1)]))

        csis.append([complex(r, i) for r,i in zip(amplitudes, phases)])

        # print(csis)
    print(len(csis[0]))
    

    
