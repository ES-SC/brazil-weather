import numpy as np
import csv


txt_file = 'airport_station.txt'
csv_file = 'airport_station.csv'
def pre_format_txt_file(file):
    new_file = ""
    with open(file, 'r') as f:
        for line in f:
            line_str = str(line)
            line_str = line_str.replace("\t",",")
            new_file += line_str
    return new_file


def save_txt_file(text_string):
    # np.savetxt(csv_file, text_string, delimiter=',')
    # f = open(csv_file, "wb")
    # writer = csv.writer(f)
    # entries = text_string.split(",")
    # print(entries)
    # writer.writerows(entries)
    # f.close()
    print(text_string)
    file_list = text_string.split('\n')
    print(type(file_list))
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for line in file_list:
            writer.writerows(line)
            print(line)

if __name__ == '__main__':
    # text = pre_format_txt_file(txt_file)

    # save_txt_file(text)
    # txt_file = txt_file
    # csv_file = csv_file

    # use 'with' if the program isn't going to immediately terminate
    # so you don't leave files open
    # the 'b' is necessary on Windows
    # it prevents \x1a, Ctrl-z, from ending the stream prematurely
    # and also stops Python converting to / from different line terminators
    # On other platforms, it has no effect
    in_txt = csv.reader(open(txt_file, "r"), delimiter='\t')
    out_csv = csv.writer(open(csv_file, 'w'))

    out_csv.writerows(in_txt)




