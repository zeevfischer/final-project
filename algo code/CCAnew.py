# # import json
# # import numpy as np
# # from sklearn.cross_decomposition import CCA
# #
# #
# # # Function to load JSON data
# # def load_json(file_path):
# #     with open(file_path, 'r') as file:
# #         data = [json.loads(line) for line in file]
# #     return data
# #
# #
# # # Function to extract palm positions
# # def extract_palm_positions(data):
# #     positions = []
# #     for frame in data:
# #         palm_position = frame['PalmPosition']
# #         positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
# #     return np.array(positions)
# #
# #
# # # Function to extract palm velocities
# # def extract_palm_velocities(data):
# #     velocities = []
# #     for frame in data:
# #         palm_velocity = frame['PalmVelocity']
# #         velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
# #     return np.array(velocities)
# #
# #
# # # Function to extract tip positions
# # def extract_tip_positions(data):
# #     positions = []
# #     for frame in data:
# #         frame_positions = []
# #         for finger in frame['fingers']:
# #             tip_position = finger['TipPosition']
# #             frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
# #         positions.append(np.mean(frame_positions, axis=0))
# #     return np.array(positions)
# #
# #
# # # Function to perform CCA with window analysis and error margin
# # def controlled_cca(data1, data2, margin=0, window_size=4):
# #     n = min(len(data1), len(data2))  # Use the length of the shortest sequence
# #     # cca = CCA(n_components=1,max_iter=1000)
# #     correlations = []
# #
# #     for i in range(n - window_size):
# #         # min_corr = None
# #         local_avg = []
# #
# #         # Compare the subsequence from data1 with a subsequence from data2
# #         subsequence1 = data1[i:i + window_size]
# #         # best_subsequence2 = None
# #
# #         for j in range(max(0, i - window_size), min(n - window_size, i+1)):
# #             subsequence2 = data2[j:j + window_size]
# #
# #             # Perform CCA on the subsequences
# #             # X_c, Y_c = cca.fit_transform(subsequence1, subsequence2)
# #             corr = np.corrcoef(subsequence1.T, subsequence2.T)[0, 1]
# #             print(f"CCA comparison: Subsequence starting at {i} of data1 with subsequence starting at {j} of data2: Correlation = {corr}")
# #             local_avg.append(corr)
# #
# #             # if min_corr is None or corr > min_corr:
# #             #     min_corr = corr
# #             #     best_subsequence2 = subsequence2
# #         correlations.append(np.mean(local_avg))
# #
# #         # # Apply margin of error
# #         # if min_corr is not None:
# #         #     adjusted_corr = min_corr if min_corr > margin else 0
# #         #     correlations.append(adjusted_corr)
# #
# #     # Calculate the average correlation over the entire sequence
# #     average_corr = np.mean(correlations)
# #     return average_corr, correlations
# #
# #
# # # Load the data
# # data1 = load_json('data_pool_3/sync_right_hand_data.json')
# # data2 = load_json('data_pool_3/sync_left_hand_data.json')
# #
# # # data1 = load_json('data_pool_3/unsync_right_hand_data.json')
# # # data2 = load_json('data_pool_3/unsync_left_hand_data.json')
# #
# # # Extract palm positions
# # positions1 = extract_palm_positions(data1)
# # positions2 = extract_palm_positions(data2)
# #
# # # Perform CCA with window analysis for Palm Position
# # average_corr_position, correlations_position = controlled_cca(positions1, positions2, margin=0.0, window_size=4)
# # print("Average CCA Correlation (Position) with Margin and Window Analysis:", average_corr_position)
# #
# # # Extract palm velocities
# # velocities1 = extract_palm_velocities(data1)
# # velocities2 = extract_palm_velocities(data2)
# #
# # # Perform CCA with window analysis for Palm Velocity
# # average_corr_velocity, correlations_velocity = controlled_cca(velocities1, velocities2, margin=0.0, window_size=4)
# # print("Average CCA Correlation (Velocity) with Margin and Window Analysis:", average_corr_velocity)
# #
# # # Extract tip positions
# # tip_positions1 = extract_tip_positions(data1)
# # tip_positions2 = extract_tip_positions(data2)
# #
# # # Perform CCA with window analysis for Tip Position
# # average_corr_tip, correlations_tip = controlled_cca(tip_positions1, tip_positions2, margin=0.0, window_size=4)
# # print("Average CCA Correlation (Tip Position) with Margin and Window Analysis:", average_corr_tip)
#
#
# # import json
# # import numpy as np
# # from sklearn.cross_decomposition import CCA
# # from sklearn.exceptions import ConvergenceWarning
# # import warnings
# #
# # # Function to load JSON data
# # def load_json(file_path):
# #     with open(file_path, 'r') as file:
# #         data = [json.loads(line) for line in file]
# #     return data
# #
# # # Function to extract palm positions
# # def extract_palm_positions(data):
# #     positions = []
# #     for frame in data:
# #         palm_position = frame['PalmPosition']
# #         positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
# #     return np.array(positions)
# #
# # # Function to extract palm velocities
# # def extract_palm_velocities(data):
# #     velocities = []
# #     for frame in data:
# #         palm_velocity = frame['PalmVelocity']
# #         velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
# #     return np.array(velocities)
# #
# # # Function to extract tip positions
# # def extract_tip_positions(data):
# #     positions = []
# #     for frame in data:
# #         frame_positions = []
# #         for finger in frame['fingers']:
# #             tip_position = finger['TipPosition']
# #             frame_positions.append([tip_position['x'], tip_position['y'], tip_position['z']])
# #         positions.append(np.mean(frame_positions, axis=0))
# #     return np.array(positions)
# #
# # # Function to perform CCA with window comparison and margin of error
# # def controlled_cca(data1, data2, margin=0.0, window_size=5):
# #     n = min(len(data1), len(data2))  # Use the length of the shortest sequence
# #     correlations = []
# #
# #     for i in range(n - window_size + 1):
# #         window_correlations = []
# #         for j in range(max(0, i - window_size + 1), min(n, i + 1)):
# #             cca = CCA(n_components=1, max_iter=1000)
# #             try:
# #                 # X_c, Y_c = cca.fit_transform(data1[i:i + window_size], data2[j:j + window_size])
# #                 corr = np.corrcoef(data1[i:i + window_size].T, data2[j:j + window_size].T)[0, 1]
# #                 adjusted_corr = max(0, corr - margin)
# #                 window_correlations.append(adjusted_corr)
# #                 print(f"Window {i}: CCA Correlation = {corr}, Adjusted Correlation = {adjusted_corr}")
# #             except ConvergenceWarning:
# #                 print(f"Window {i}: CCA did not converge, skipping this window.")
# #                 continue
# #
# #         if window_correlations:
# #             avg_corr = np.mean(window_correlations)
# #             correlations.append(avg_corr)
# #
# #     average_corr = np.mean(correlations) if correlations else 0
# #     return average_corr, correlations
# #
# # # Load the data
# # data1 = load_json('data_pool_3/sync_right_hand_data.json')
# # data2 = load_json('data_pool_3/sync_left_hand_data.json')
# #
# # # Extract palm positions
# # positions1 = extract_palm_positions(data1)
# # positions2 = extract_palm_positions(data2)
# #
# # # Perform controlled CCA for Palm Position
# # average_corr_position, correlations_position = controlled_cca(positions1, positions2, margin=0.0, window_size=5)
# # print("Average CCA Correlation (Position):", average_corr_position)
# # print("All Window Correlations (Position):", correlations_position)
# #
# # # Extract palm velocities
# # velocities1 = extract_palm_velocities(data1)
# # velocities2 = extract_palm_velocities(data2)
# #
# # # Perform controlled CCA for Palm Velocity
# # average_corr_velocity, correlations_velocity = controlled_cca(velocities1, velocities2, margin=0.0, window_size=5)
# # print("Average CCA Correlation (Velocity):", average_corr_velocity)
# # print("All Window Correlations (Velocity):", correlations_velocity)
# #
# # # Extract tip positions
# # tip_positions1 = extract_tip_positions(data1)
# # tip_positions2 = extract_tip_positions(data2)
# #
# # # Perform controlled CCA for Tip Position
# # average_corr_tip, correlations_tip = controlled_cca(tip_positions1, tip_positions2, margin=0.0, window_size=5)
# # print("Average CCA Correlation (Tip Position):", average_corr_tip)
# # print("All Window Correlations (Tip Position):", correlations_tip)
#
#
# import json
# import numpy as np
# from sklearn.cross_decomposition import CCA
#
#
# # Function to load JSON data
# def load_json(file_path):
#     with open(file_path, 'r') as file:
#         data = [json.loads(line) for line in file]
#     return data
#
#
# # Function to extract palm positions
# def extract_palm_positions(data):
#     positions = []
#     for frame in data:
#         palm_position = frame['PalmPosition']
#         positions.append([palm_position['x'], palm_position['y'], palm_position['z']])
#     return np.array(positions)
#
#
# # Function to extract palm velocities
# def extract_palm_velocities(data):
#     velocities = []
#     for frame in data:
#         palm_velocity = frame['PalmVelocity']
#         velocities.append([palm_velocity['x'], palm_velocity['y'], palm_velocity['z']])
#     return np.array(velocities)
#
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
#
# # Function to compare each line from data1 with a progressively increasing window of lines from data2
# def compare_with_window(data1, data2, window_size=5):
#     correlations = []
#     n = len(data1)
#
#     cca = CCA(n_components=1, max_iter=1000)  # CCA object initialized here for efficiency
#
#     for i in range(n):
#         local_avg = []
#         start_index = max(0, i - window_size + 1)
#         end_index = i + 1
#         print(f"\nComparing line {i} from data1 with lines {start_index} to {end_index - 1} from data2:")
#
#         for j in range(start_index, end_index):
#             X_c, Y_c = cca.fit_transform(data1[i].reshape(-1, 1), data2[j].reshape(-1, 1))  # Reshaping for CCA
#             corr = np.corrcoef(X_c.T, Y_c.T)[0, 1]
#             local_avg.append(corr)
#             print(f"  Line {i} from data1 with Line {j} from data2: Correlation = {corr}")
#
#         avg_corr = np.mean(local_avg)
#         correlations.append(avg_corr)
#         print(f"Average correlation for line {i}: {avg_corr}")
#
#     # Calculate the overall average correlation
#     average_corr = np.mean(correlations)
#     return average_corr
#
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
# # Compare Palm Positions with Window Analysis
# average_corr_position = compare_with_window(positions1, positions2, window_size=5)
# print("\nAverage Correlation (Position) with Window Analysis:", average_corr_position)
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
# # Compare Palm Velocities with Window Analysis
# average_corr_velocity = compare_with_window(velocities1, velocities2, window_size=5)
# print("\nAverage Correlation (Velocity) with Window Analysis:", average_corr_velocity)
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
# # Compare Tip Positions with Window Analysis
# average_corr_tip = compare_with_window(tip_positions1, tip_positions2, window_size=5)
# print("\nAverage Correlation (Tip Position) with Window Analysis:", average_corr_tip)
#
#
#
# import json
# import numpy as np
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
# # Function to compare a single line from data1 with a window of lines from data2
# def compare_line_with_window(data1, data2, window_size=5):
#     correlations = []
#     n = len(data1)
#
#     for i in range(n):
#         local_corrs = []
#         start_index = max(0, i - window_size + 1)
#         end_index = i + 1
#
#         print(f"\nComparing line {i} from data1 with lines {start_index} to {end_index - 1} from data2:")
#
#         for j in range(start_index, end_index):
#             corr = np.corrcoef(data1[i], data2[j])[0, 1]
#             local_corrs.append(corr)
#             print(f"  Line {i} from data1 with Line {j} from data2: Correlation = {corr}")
#
#         avg_corr = np.mean(local_corrs)
#         correlations.append(avg_corr)
#         print(f"Average correlation for line {i}: {avg_corr}")
#
#     # Calculate the overall average correlation
#     average_corr = np.mean(correlations)
#     return average_corr
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
# # Compare Palm Positions with Window Analysis
# average_corr_position = compare_line_with_window(positions1, positions2, window_size=5)
# print("\nAverage Correlation (Position) with Window Analysis:", average_corr_position)
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
# # Compare Palm Velocities with Window Analysis
# average_corr_velocity = compare_line_with_window(velocities1, velocities2, window_size=5)
# print("\nAverage Correlation (Velocity) with Window Analysis:", average_corr_velocity)
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
# # Compare Tip Positions with Window Analysis
# average_corr_tip = compare_line_with_window(tip_positions1, tip_positions2, window_size=5)
# print("\nAverage Correlation (Tip Position) with Window Analysis:", average_corr_tip)
#
#
