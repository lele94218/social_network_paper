import os
read_path = 'F:\\paper\\myPython\\py2.7\\new_data\\'
write_path = 'F:\\paper\\myPython\\py2.7\\raw_data\\'
for subdir, dirs, files in os.walk(read_path):
    for file in files:
        print file
        file_path = subdir + os.path.sep + file
        read_in = open(file_path, 'r')
        write_out = open(write_path + file, 'w')
        for line in read_in.readlines():
            list1 = line.split(' ')
            for each in list1:
                if each[:7] == 'http://' or each[:8] == 'https://' or each[:4] == 'www.' or each[:4] == 'WWW.':
                    continue
                tmp = each.replace('#', ' ')
                write_out.write(tmp + ' ')
        read_in.close()
        write_out.close()
                    
                    
