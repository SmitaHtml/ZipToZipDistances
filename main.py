import csv
import tozipdistances


open('ziptozipdistancefile.txt', 'w').close();
file_name = 'zipcodes0.csv';
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    fileziptozipdistance = open("ziptozipdistancefile.txt", "a")
    fileziptozipdistance.write("fromZip, toZip, distanceInMiles\n")
    for row in csv_reader:
        if line_count == 0:
            print(line_count, 'FromZip header: ', row[0], row[1], row[2]);
            line_count += 1
        else:
            fromZip = row[0]
            fromlat = float(row[1])
            fromlong = float(row[2])
            print(line_count, 'FromZip: ', row[0], row[1], row[2]);
            tozipdistances.tozipdistances(file_name, fromZip, fromlat, fromlong, fileziptozipdistance)
            line_count += 1
    fileziptozipdistance.close();
