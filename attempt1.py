
import timeit

n = int(input(''))
lst = []
lst_file_names = set()
for i in range(0, n):
    file = input('f ')
    s_file = file
    f_format = ''
    print(lst_file_names)
    if file in lst_file_names:
        end_index = file.find('.')
        if end_index == -1:
            file += "("+str(lst_file_names.count(s_file))+")"
            lst.append(file)
            lst_file_names.append(s_file)
        else:
             lst_file_names.append(file)
             file_name = file[0:end_index]

             f_format = s_file[end_index:len(s_file)]

             file_name += "("+str(lst_file_names.count(file)-1)+")"+ f_format
             lst.append(file_name)
    else:
        lst.append(file)
    
sorted(lst)
print(lst)
print(lst_file_names)
time_taken = timeit.timeit()
print(f"Время выполнения: {time_taken} секунд")

