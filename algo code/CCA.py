# '''
# In summary, CCA helps in understanding the extent to which two multidimensional
# datasets are related to each other by finding the linear combinations of the
# variables in each set that are maximally correlated.
# This can be particularly useful in analyzing synchronization in movement data,
# as it quantifies the degree of similarity in the patterns of the two datasets.
# '''
#
# import json
# import numpy as np
# from sklearn.cross_decomposition import CCA
#
# # Function to load JSON data
# def load_json(file_path):
#     with open(file_path, 'r') as file:
#         data = [json.loads(line) for line in file]
#     return data
#
# # Function to extract palm positions
# def extract_palm_positions(data):
#     positions = []
#     for frame in data:
#         palm_position = frame['PalmPosition']
#         positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
#     return np.array(positions)
#
# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
#     return np.array(velocities)
#
# # Function to extract tip positions
# def extract_tip_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)
#
# # Function to align lengths of two arrays
# def align_lengths(arr1, arr2):
#     min_len = min(len(arr1), len(arr2))
#     return arr1[:min_len], arr2[:min_len]
# # Load the data
# # data1 = load_json('data_pool_2/data4.json')
# # data2 = load_json('data_pool_2/mirrored_data4.json')
# # data2 = load_json('data_pool_2/suffle.json')
#
#
# # data1 = load_json('data_pool_3/sync_right_hand_data.json')
# # data2 = load_json('data_pool_3/sync_left_hand_data.json')
#
# data1 = load_json('data_pool_3/unsync_right_hand_data.json')
# data2 = load_json('data_pool_3/unsync_left_hand_data.json')
#
# # Extract palm positions
# positions1 = extract_palm_positions(data1)
# positions2 = extract_palm_positions(data2)
# positions1, positions2 = align_lengths(positions1, positions2)
#
# # Canonical Correlation Analysis (CCA) using Palm Position
# cca = CCA(n_components=1)
# cca.fit(positions1, positions2)
# X_c, Y_c = cca.transform(positions1, positions2)
# correlation_position = np.corrcoef(X_c.T, Y_c.T)[0, 1]
# print("CCA Correlation (Position):", correlation_position)
#
# # Extract palm velocities
# velocities1 = extract_palm_velocities(data1)
# velocities2 = extract_palm_velocities(data2)
# velocities1, velocities2 = align_lengths(velocities1, velocities2)
#
# # Canonical Correlation Analysis (CCA) using Palm Velocity
# cca.fit(velocities1, velocities2)
# X_c, Y_c = cca.transform(velocities1, velocities2)
# correlation_velocity = np.corrcoef(X_c.T, Y_c.T)[0, 1]
# print("CCA Correlation (Velocity):", correlation_velocity)
#
# # Extract tip positions
# tip_positions1 = extract_tip_positions(data1)
# tip_positions2 = extract_tip_positions(data2)
# tip_positions1, tip_positions2 = align_lengths(tip_positions1, tip_positions2)
#
# # Canonical Correlation Analysis (CCA) using Tip Position
# cca.fit(tip_positions1, tip_positions2)
# X_c, Y_c = cca.transform(tip_positions1, tip_positions2)
# correlation_tip = np.corrcoef(X_c.T, Y_c.T)[0, 1]
# print("CCA Correlation (Tip Position):", correlation_tip)

# new
# import json
# import numpy as np
# from sklearn.cross_decomposition import CCA
#
# # Function to load JSON data
# def load_json(file_path):
#     with open(file_path, 'r') as file:
#         data = [json.loads(line) for line in file]
#     return data
#
# # Function to extract palm positions
# def extract_palm_positions(data):
#     positions = []
#     for frame in data:
#         palm_position = frame['PalmPosition']
#         positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
#     return np.array(positions)
#
# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
#     return np.array(velocities)
#
# # Function to extract tip positions
# def extract_tip_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)
#
# # Load the data
# data1 = load_json('data_pool_3/unsync_right_hand_data.json')
# data2 = load_json('data_pool_3/unsync_left_hand_data.json')
#
# # Extract palm positions
# positions1 = extract_palm_positions(data1)
# positions2 = extract_palm_positions(data2)
#
# # Ensure both datasets are of the same length
# min_len = min(len(positions1), len(positions2))
# positions1 = positions1[:min_len]
# positions2 = positions2[:min_len]
#
# # Canonical Correlation Analysis (CCA) using Palm Position
# cca = CCA(n_components=1)
# X_c, Y_c = cca.fit_transform(positions1, positions2)
# correlation_position = np.corrcoef(X_c.T, Y_c.T)[0, 1]
# print("CCA Correlation (Position):", correlation_position)
#
# # Extract palm velocities
# velocities1 = extract_palm_velocities(data1)
# velocities2 = extract_palm_velocities(data2)
#
# # Ensure both datasets are of the same length
# min_len = min(len(velocities1), len(velocities2))
# velocities1 = velocities1[:min_len]
# velocities2 = velocities2[:min_len]
#
# # Canonical Correlation Analysis (CCA) using Palm Velocity
# X_c, Y_c = cca.fit_transform(velocities1, velocities2)
# correlation_velocity = np.corrcoef(X_c.T, Y_c.T)[0, 1]
# print("CCA Correlation (Velocity):", correlation_velocity)
#
# # Extract tip positions
# tip_positions1 = extract_tip_positions(data1)
# tip_positions2 = extract_tip_positions(data2)
#
# # Ensure both datasets are of the same length
# min_len = min(len(tip_positions1), len(tip_positions2))
# tip_positions1 = tip_positions1[:min_len]
# tip_positions2 = tip_positions2[:min_len]
#
# # Canonical Correlation Analysis (CCA) using Tip Position
# X_c, Y_c = cca.fit_transform(tip_positions1, tip_positions2)
# correlation_tip = np.corrcoef(X_c.T, Y_c.T)[0, 1]
# print("CCA Correlation (Tip Position):", correlation_tip)
'''
Positive Correlation: Indicates that as the movement of one hand increases in a particular direction, the movement of the other hand also increases in the same direction. This is typical for synchronized hand movements.
Negative Correlation: Indicates that as the movement of one hand increases in a particular direction, the movement of the other hand decreases in the opposite direction. This can happen if the hands are moving in opposite directions, which might still be synchronized but mirrored.
using the window dose not worck !!!!
using CCA dose not worck
'''
# new 2
import json
import numpy as np
from sklearn.cross_decomposition import CCA

# Function to load JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data

# Function to extract palm positions
def extract_palm_positions(data):
    positions = []
    for frame in data:
        palm_position = frame['PalmPosition']
        positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
    return np.array(positions)

# Function to extract palm velocities
def extract_palm_velocities(data):
    velocities = []
    for frame in data:
        palm_velocity = frame['PalmVelocity']
        velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
    return np.array(velocities)

# Function to extract tip positions
def extract_tip_positions(data):
    positions = []
    for frame in data:
        frame_positions = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
        positions.append(np.mean(frame_positions, axis=0))
    return np.array(positions)

# Load the data
data1 = load_json('data_pool_3/sync_right_hand_data.json')
data2 = load_json('data_pool_3/sync_left_hand_data.json')
cca = CCA(n_components=1, max_iter = 1000)

# Extract palm positions
positions1 = extract_palm_positions(data1)
positions2 = extract_palm_positions(data2)

# Ensure both datasets are of the same length
min_len = min(len(positions1), len(positions2))
positions1 = positions1[:min_len]
positions2 = positions2[:min_len]

# Direct Correlation Analysis using Palm Position
X_c, Y_c = cca.fit_transform(positions1, positions2)
correlation_position = np.corrcoef(positions1.T, positions2.T)[0, 1]
# correlation_position = np.corrcoef(X_c.T, Y_c.T)[0, 1]
print("Direct Correlation (Position):", correlation_position)

# Extract palm velocities
velocities1 = extract_palm_velocities(data1)
velocities2 = extract_palm_velocities(data2)

# Ensure both datasets are of the same length
min_len = min(len(velocities1), len(velocities2))
velocities1 = velocities1[:min_len]
velocities2 = velocities2[:min_len]

# Direct Correlation Analysis using Palm Velocity
X_c, Y_c = cca.fit_transform(velocities1, velocities2)
correlation_velocity = np.corrcoef(velocities1.T, velocities2.T)[0, 1]
# correlation_velocity = np.corrcoef(X_c.T, Y_c.T)[0, 1]
print("Direct Correlation (Velocity):", correlation_velocity)

# Extract tip positions
tip_positions1 = extract_tip_positions(data1)
tip_positions2 = extract_tip_positions(data2)

# Ensure both datasets are of the same length
min_len = min(len(tip_positions1), len(tip_positions2))
tip_positions1 = tip_positions1[:min_len]
tip_positions2 = tip_positions2[:min_len]

# Direct Correlation Analysis using Tip Position
X_c, Y_c = cca.fit_transform(tip_positions1, tip_positions2)
correlation_tip = np.corrcoef(tip_positions1.T, tip_positions2.T)[0, 1]
# correlation_tip = np.corrcoef(X_c.T, Y_c.T)[0, 1]
print("Direct Correlation (Tip Position):", correlation_tip)

