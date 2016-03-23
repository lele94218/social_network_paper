import os
read_path = 'F:\\paper\\myPython\\py2.7\\final_raw\\'
write_path = 'F:\\paper\\myPython\\py2.7\\_final_raw\\'
for subdir, dirs, files in os.walk(read_path):
    for file in files:
        print file
        file_path = subdir + os.path.sep + file
        read_in = open(file_path, 'r')
        write_out = open(write_path + file, 'w')
        for line in read_in.readlines():
            list1 = line.split(' ')
            for list in list1:
                filter(lambda ch: ch in 'abcdefghijklmnopqrstuvwxyz0123456789\'', list)
                write_out.write(list + ' ')
        read_in.close()
        write_out.close()
                    
                    
