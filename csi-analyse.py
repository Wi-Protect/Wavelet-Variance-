import pandas as pd
from wavelet_check import wavelet_amplitude_variance, wavelet_phase_variance

chunk_size = 10
file_path = './csi_data.csv'

# Read the file in chunks of 10 lines
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Process each chunk of data
    # print(list(chunk['amplitude1']))
    
    # csis = []
    amplitudes_variances = []
    phases_variances = []
    for i in range(64):
        # amplitudes = []
        # phases = []
        amplitudes = (list(chunk['amplitude'+str(i+1)]))
        phases = (list(chunk['phase'+str(i+1)]))
        csi = [complex(r, i) for r,i in zip(amplitudes, phases)]

        # print("Amplitude Variance Channel " + str(i+1) + " = " + str(wavelet_amplitude_variance(csi, 'db4', 2)))
        # print("Phase Variance Channel " + str(i+1) + " = " + str(wavelet_phase_variance(csi, 'db4', 2)))

        amplitudes_variances.append(wavelet_amplitude_variance(csi, 'db4', 2))
        phases_variances.append(wavelet_phase_variance(csi, 'db4', 2))

        # csis.append([complex(r, i) for r,i in zip(amplitudes, phases)])
    
    print(len(amplitudes_variances))
    # print(len(phases_variances))



        # print(csis)
    # print(len(csis[0]))
    

    
