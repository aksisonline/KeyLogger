def process_input(input_sequence):
    return [i.strip("'") for i in input_sequence.split(' ')]

input_file_path = 'C:/Users/<type_your_pc_name>/output'

with open(input_file_path, 'r') as input_file:
    input_sequence = input_file.read()

processed_sequence = process_input(input_sequence)

for k in processed_sequence:
    if len(k) <=2 :
        print(k,end='')

if input():
    exit()
