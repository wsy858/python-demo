import csv


def read(file_name):
    with open(file_name)as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            print(str(row[0]))


if __name__ == '__main__':
    read(r"E:\Users\Desktop\query-impala-258060.csv")
