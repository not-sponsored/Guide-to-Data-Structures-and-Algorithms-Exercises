data_arr = str(input('Enter list in csv: ')).split(',')
data_arr = [int(x) for x in data_arr]

print(f'default {sorted(data_arr)}')
for i in range(0, len(data_arr)):
    min_val = data_arr[i]
    for j in range(i+1, len(data_arr)):
        if data_arr[j] < data_arr[i]:
            min_val = data_arr[j]
    
    if min_val != data_arr[i]:
        data_arr[i], data_arr[j] = data_arr[j], data_arr[i] 

print(f'default {sorted(data_arr)}')
print(f'selection sort {data_arr}')
