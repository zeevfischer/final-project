# import json
# import numpy as np
# from scipy.spatial.distance import euclidean
# from fastdtw import fastdtw
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
#         positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
#     return np.array(positions)
#
# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([abs(palm_velocity['x']), abs(palm_velocity['y']), abs(palm_velocity['z'])])
#     return np.array(velocities)
#
# # Function to extract tip positions
# def extract_tip_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([abs(tip_position['x']), abs(tip_position['y']), abs(tip_position['z'])])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)
#
# # Function to perform DTW with margin of error and extended comparison
# def dtw_with_margin_and_extended_comparison(data1, data2, margin=5, window_size=5):
#     n = len(data1)
#     total_distance = 0
#     for i in range(n):
#         min_distance = float('inf')
#         for j in range(max(0, i-window_size), min(n, i+window_size+1)):
#             distance, _ = fastdtw(data1[i], data2[j], dist=euclidean)
#             if distance < min_distance:
#                 min_distance = distance
#         total_distance += min(min_distance, margin)
#     normalized_distance = total_distance / n
#     return normalized_distance
#
# # Load the data
# data1 = load_json('data_pool_3/sync_left_hand_data.json')
# data2 = load_json('data_pool_3/sync_right_hand_data.json')
#
# # Extract palm positions
# positions1 = extract_palm_positions(data1)
# positions2 = extract_palm_positions(data2)
#
# # DTW with margin and extended comparison for Palm Position
# normalized_distance_position = dtw_with_margin_and_extended_comparison(positions1, positions2, margin=5, window_size=5)
# print("Normalized DTW Distance with Margin (Position):", normalized_distance_position)
# print()
#
# # Extract palm velocities
# velocities1 = extract_palm_velocities(data1)
# velocities2 = extract_palm_velocities(data2)
#
# # DTW with margin and extended comparison for Palm Velocity
# normalized_distance_velocity = dtw_with_margin_and_extended_comparison(velocities1, velocities2, margin=5, window_size=5)
# print("Normalized DTW Distance with Margin (Velocity):", normalized_distance_velocity)
# print()
#
# # Extract tip positions
# tip_positions1 = extract_tip_positions(data1)
# tip_positions2 = extract_tip_positions(data2)
#
# # DTW with margin and extended comparison for Tip Position
# normalized_distance_tip_position = dtw_with_margin_and_extended_comparison(tip_positions1, tip_positions2, margin=5, window_size=5)
# print("Normalized DTW Distance with Margin (Tip Position):", normalized_distance_tip_position)
# print()


############ margin only
# import json
# import numpy as np
# from scipy.spatial.distance import euclidean
# from fastdtw import fastdtw
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
#         positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
#     return np.array(positions)
#
# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([abs(palm_velocity['x']), abs(palm_velocity['y']), abs(palm_velocity['z'])])
#     return np.array(velocities)
#
# # Function to extract tip positions
# def extract_tip_positions(data):
#     positions = []
#     for frame in data:
#         frame_positions = []
#         for finger in frame['fingers']:
#             tip_position = finger['TipPosition']
#             frame_positions.append([abs(tip_position['x']), abs(tip_position['y']), abs(tip_position['z'])])
#         positions.append(np.mean(frame_positions, axis=0))
#     return np.array(positions)
#
# # Function to perform DTW with margin of error
# def dtw_with_margin(data1, data2, margin):
#     distance, path = fastdtw(data1, data2, dist=euclidean)
#     adjusted_distance = max(0, distance - margin)
#     return adjusted_distance, path
#
# # Load the data
# # data1 = load_json('data_pool_2/data4.json')
# # data2 = load_json('data_pool_2/mirrored_data4.json')
#
# data1 = load_json('data_pool_3/sync_left_hand_data.json')
# data2 = load_json('data_pool_3/sync_right_hand_data.json')
# margin = 5
#
# # Extract palm positions
# positions1 = extract_palm_positions(data1)
# positions2 = extract_palm_positions(data2)
#
# # Dynamic Time Warping (DTW) using Palm Position with Margin
# distance_position, path_position = dtw_with_margin(positions1, positions2, margin)
# print("DTW Distance with Margin (Position):", distance_position)
#
# # Normalize DTW distance for Palm Position
# normalized_distance_position = distance_position / len(positions1)
# print("Normalized DTW Distance with Margin (Position):", normalized_distance_position)
# print()
#
# # Extract palm velocities
# velocities1 = extract_palm_velocities(data1)
# velocities2 = extract_palm_velocities(data2)
#
# # Dynamic Time Warping (DTW) using Palm Velocity with Margin
# distance_velocity, path_velocity = dtw_with_margin(velocities1, velocities2, margin)
# print("DTW Distance with Margin (Velocity):", distance_velocity)
#
# # Normalize DTW distance for Palm Velocity
# normalized_distance_velocity = distance_velocity / len(velocities1)
# print("Normalized DTW Distance with Margin (Velocity):", normalized_distance_velocity)
# print()
#
# # Extract tip positions
# tip_positions1 = extract_tip_positions(data1)
# tip_positions2 = extract_tip_positions(data2)
#
# # Dynamic Time Warping (DTW) using Tip Position with Margin
# distance_tip_position, path_tip_position = dtw_with_margin(tip_positions1, tip_positions2, margin)
# print("DTW Distance with Margin (Tip Position):", distance_tip_position)
#
# # Normalize DTW distance for Tip Position
# normalized_distance_tip_position = distance_tip_position / len(tip_positions1)
# print("Normalized DTW Distance with Margin (Tip Position):", normalized_distance_tip_position)
# print()


import json
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

'''
Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences that may vary in speed.
The main idea is to align the sequences in a way that minimizes the total distance between them.
This can handle sequences of different lengths and can align sequences even if they are out of phase.

Here we are working with a distance so we need to use abs on all the data !!!
'''


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
        positions.append([abs(palm_position['x']), abs(palm_position['y']), abs(palm_position['z'])])
    return np.array(positions)


# Function to extract palm velocities
def extract_palm_velocities(data):
    velocities = []
    for frame in data:
        palm_velocity = frame['PalmVelocity']
        velocities.append([abs(palm_velocity['x']), abs(palm_velocity['y']), abs(palm_velocity['z'])])
    return np.array(velocities)


# Function to extract tip positions
def extract_tip_positions(data):
    positions = []
    for frame in data:
        frame_positions = []
        for finger in frame['fingers']:
            tip_position = finger['TipPosition']
            frame_positions.append([abs(tip_position['x']), abs(tip_position['y']), abs(tip_position['z'])])
        positions.append(np.mean(frame_positions, axis=0))
    return np.array(positions)


# Function to perform DTW with manual control over the window size and margin of error
def controlled_dtw(data1, data2,file1,file2, margin=0, window_size=5):
    n = min(len(data1), len(data2))  # Use the length of the shortest sequence
    total_distance = 0

    for i in range(n):
        min_distance = float('inf')

        # Compare the current frame from data1 with a range of frames from data2
        for j in range(max(0, i - window_size), min(n, i+1)):
            # Perform DTW on small subsequences around the current index
            distance, _ = fastdtw(data1[i:i + 1], data2[j:j + 1], dist=euclidean)
            print(f"DTW comparison frame {file1[i]['frameId']} of data1 with frame {file2[j]['frameId']} of data2: Distance = {distance}")

            if distance < min_distance:
                min_distance = distance

        # Apply margin of error
        adjusted_distance = max(0, min_distance - margin)
        total_distance += distance

        print(f"Frame {file1[i]["frameId"]}: Min Distance = {min_distance}, Adjusted Distance = {distance}")

    # Normalize the total distance by the number of frames
    normalized_distance = total_distance / n
    return normalized_distance , total_distance


# Load the data
# data1 = load_json('data_pool_2/data4.json')
# data2 = load_json('data_pool_2/suffle.json')

# data1 = load_json('data_pool_3/sync_right_hand_data.json')
# data2 = load_json('data_pool_3/sync_left_hand_data.json')

data1 = load_json('data_pool_3/unsync_right_hand_data.json')
data2 = load_json('data_pool_3/unsync_left_hand_data.json')

# data1 = load_json('data_pool_4/temp1.json')
# data2 = load_json('data_pool_4/temp2.json')

# Extract palm positions
positions1 = extract_palm_positions(data1)
positions2 = extract_palm_positions(data2)

# Controlled DTW comparison for Palm Position
normalized_distance_position , dist_Position = controlled_dtw(positions1, positions2,data1,data2, margin=0, window_size=5)
print("DTW Distance with Margin (Position):", dist_Position)
print("Normalized Controlled DTW Distance with Margin (Position):", normalized_distance_position)
print()

# Extract palm velocities
velocities1 = extract_palm_velocities(data1)
velocities2 = extract_palm_velocities(data2)

# Controlled DTW comparison for Palm Velocity
normalized_distance_velocity, dist_Velocity = controlled_dtw(velocities1, velocities2,data1,data2, margin=0, window_size=5)
print("DTW Distance with Margin (Velocity):", dist_Velocity)
print("Normalized Controlled DTW Distance with Margin (Velocity):", normalized_distance_velocity)
print()

# Extract tip positions
tip_positions1 = extract_tip_positions(data1)
tip_positions2 = extract_tip_positions(data2)

# Controlled DTW comparison for Tip Position
normalized_distance_tip_position,dist_Tip_pos = controlled_dtw(tip_positions1, tip_positions2,data1,data2, margin=0, window_size=5)
print("DTW Distance with Margin (Tip Position):", dist_Tip_pos)
print("Normalized Controlled DTW Distance with Margin (Tip Position):", normalized_distance_tip_position)
print()
