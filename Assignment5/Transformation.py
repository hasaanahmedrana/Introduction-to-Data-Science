f = open("customerss.csv", "r")
f2 = open("customerss2.csv", "w")
for line in f:
    r = f.readline()
    r = r.replace('"', '')
    lst = r.split()
    if len(lst) > 3:
        result = ', '.join(lst[:3]) + ' ' + ' '.join(lst[3:])
    else:
        result = ', '.join(lst)  # If the list has 3 or fewer elements, just join with commas

    f2.writelines(f'{result}\n')
