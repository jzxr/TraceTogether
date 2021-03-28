import os
import csv

infected = input("Enter the infected person's number: ")  # ask the user for infected, use raw_input() on Python 2.x

root_dir = "/Users/jasminezheng/Desktop/SIT/CSC1008 Data Structure and Algorithm /Group2_TraceTogether/TraceTogether/Data Sets/Location SE Data"  # path to the root directory to search
for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
    for filename in files:  # iterate over the files in the current dir
        file_path = os.path.join(root, filename)  # build the file path
        try:
            with open(file_path, "rb") as f:  # open the file for reading
                # read the file line by line
                for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                    try:
                        line = line.decode("utf-8")  # try to decode the contents to utf-8
                    except ValueError:  # decoding failed, skip the line
                        continue
                    if infected in line:  # if the infected exists on the current line...
                        # print(file_path)  # print the file path
                        # break  # no need to iterate over the rest of the file
                        with open(file_path, newline='') as f:
                            reader = csv.reader(f)
                            try:
                                for row in reader:
                                    infectedDate = row[1]
                                    infectedCheckIn = row[2]
                                    infectedCheckOut = row[3]
                                    if infected in row:
                                        print(row)
                                    if row[1] == infectedDate:
                                        if infectedCheckIn < row[3] and infectedCheckOut > row[2]:
                                            potential = []
                                            potential.append(row[0])
                                            print (potential)
                            except csv.Error as e:
                                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
                        break
        except (IOError, OSError):  # ignore read and permission errors
            pass


# aperiaFile = csv.reader(open('Data Sets/Location SE Data/APERIAMALL.csv'))
# # aperiaReader = csv.reader(aperiaFile)
# # balestierplazaFile = file('BALESTIER PLAZA.csv', 'r')
# # balestierplazaReader = csv.reader(balestierplazaFile)
# # csmFile = file('CITY SQUARE MALL.csv', 'r')
# # csmReader = csv.reader(csmFile)
# # jcubeFile = file('JCUBE.csv','r')
# # jcubeReader = csv.reader(jcubeFile)
# # jpFile = file('JURONG POINT.csv','r')
# # jpReader = csv.reader(jpFile)
# # npFile = file('NORTHPOINT.csv','r')
# # npReader = csv.reader(npFile)
# # pioneermallFile = file('PIONEER MALL.csv','r')
# # pioneermallReader = csv.reader(pioneermallFile)
# # sitnypFile = file('SIT-NYP.csv','r')
# # sitnypReader = csv.reader(sitnypFile)
# # zhongshanFile = file('ZHONGSHAN MALL.csv','r')
# # zhongshanReader = csv.reader(zhongshanFile)

