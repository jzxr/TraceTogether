import csv,random


with open('99995219_CT.csv', mode='w') as csv_file:
    csv_write = csv.writer(csv_file, delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL,lineterminator = "\n")

    for i in range(25):
        data = []
        datelist = ['20/1/2021','21/1/2021','22/1/2021','23/1/2021','24/1/2021',
        '25/1/2021','26/1/2021','27/1/2021','28/1/2021','29/1/2021',
        '30/1/2021','31/1/2021','1/2/2021','2/2/2021','3/2/2021',
        '4/2/2021','5/2/2021','6/2/2021','7/2/2021','8/2/2021',
        '9/2/2021','10/2/2021','11/2/2021','12/2/2021','13/2/2021']
        data.append(datelist[i])

        for i in range(10):
            data.append(random.randrange(80000000,99999999))

        csv_write.writerow(data)