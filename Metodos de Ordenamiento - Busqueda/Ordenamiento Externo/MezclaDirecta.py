import os

temp_file_counter = 0  # Contador global para nombres de archivo temporales

def read_next_run(file):
    last_value = None
    run = []
    while True:
        position = file.tell()
        line = file.readline().strip()
        if not line:
            break
        value = line
        if last_value is not None and value < last_value:
            file.seek(position)
            break
        run.append(value)
        last_value = value
    return run

def merge_runs(run1, run2):
    index1, index2 = 0, 0
    merged = []
    while index1 < len(run1) and index2 < len(run2):
        if run1[index1] < run2[index2]:
            merged.append(run1[index1])
            index1 += 1
        else:
            merged.append(run2[index2])
            index2 += 1
    merged.extend(run1[index1:])
    merged.extend(run2[index2:])
    return merged

def external_direct_merge_sort(input_file_path, output_file_path):
    global temp_file_counter
    temp_file_paths = []
    with open(input_file_path, 'r') as input_file:
        while True:
            run = read_next_run(input_file)
            if not run:
                break
            temp_file_path = f'temp_{temp_file_counter}.txt'
            temp_file_counter += 1
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write('\n'.join(run))
            temp_file_paths.append(temp_file_path)
            print(f"Created temp file: {temp_file_path}")

    while len(temp_file_paths) > 1:
        new_temp_files = []
        for i in range(0, len(temp_file_paths), 2):
            if i+1 < len(temp_file_paths):
                print(f"Merging: {temp_file_paths[i]} and {temp_file_paths[i+1]}")
                with open(temp_file_paths[i], 'r') as file1,open(temp_file_paths[i+1], 'r') as file2:
                    run1 = file1.read().splitlines()
                    run2 = file2.read().splitlines()
                    merged_run = merge_runs(run1, run2)
                    new_temp_file_path = f'temp_{temp_file_counter}.txt'
                    temp_file_counter += 1
                    with open(new_temp_file_path, 'w') as new_temp_file:
                        new_temp_file.write('\n'.join(merged_run))
                    new_temp_files.append(new_temp_file_path)
                    print(f"Created merged temp file: {new_temp_file_path}")
                os.remove(temp_file_paths[i])
                os.remove(temp_file_paths[i+1])
            else:
                new_temp_files.append(temp_file_paths[i])
        temp_file_paths = new_temp_files
    
    if temp_file_paths:
        os.rename(temp_file_paths[0], output_file_path)
        print(f"Final sorted file: {output_file_path}")

# Uso del programa
input_file_path = '/home/francisco/Documents/large_text_file.txt'
output_file_path = 'sorted_text_file.txt'
external_direct_merge_sort(input_file_path, output_file_path)
