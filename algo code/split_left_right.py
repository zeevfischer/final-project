import json

# Function to split JSON data based on the "isleft" key
def split_json_by_hand(input_file, left_output_file, right_output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    left_hand_data = []
    right_hand_data = []

    for line in lines:
        data = json.loads(line)
        if data['isleft']:
            left_hand_data.append(data)
        else:
            right_hand_data.append(data)

    with open(left_output_file, 'w') as left_file:
        for entry in left_hand_data:
            json.dump(entry, left_file)
            left_file.write('\n')

    with open(right_output_file, 'w') as right_file:
        for entry in right_hand_data:
            json.dump(entry, right_file)
            right_file.write('\n')

# Example usage
input_file = 'data_pool_3/unsync.json'  # Replace with your file name
left_output_file = 'data_pool_3/unsync_left_hand_data.json'
right_output_file = 'data_pool_3/unsync_right_hand_data.json'

split_json_by_hand(input_file, left_output_file, right_output_file)
