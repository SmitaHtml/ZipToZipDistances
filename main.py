import csv
import tozipdistances

open('ziptozipdistancefile.txt', 'w').close();
file_name = 'zipcodes0.csv';
input_file_from = csv.DictReader(open(file_name))

line_count = 1
fileziptozipdistance = open("ziptozipdistancefile.txt", "a")
fileziptozipdistance.write("fromZip, toZip, distanceInMiles\n")
for row in input_file_from:
    fromZip = row["zip"]
    fromlat = float(row["lat"])
    fromlong = float(row["long"])
    print (str(line_count) + " From: " + str(row))
    tozipdistances.tozipdistances(file_name, fromZip, fromlat, fromlong, fileziptozipdistance)
    line_count += 1
fileziptozipdistance.close();
