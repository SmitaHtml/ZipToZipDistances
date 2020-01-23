import csv
import distance

def tozipdistances(file_name, fromZip, fromlat, fromlong, fileziptozipdistance):

    input_file_to = csv.DictReader(open(file_name))
    line_count = 1
    for row in input_file_to:
        toZip = row["zip"]
        tolat = float(row["lat"])
        tolong = float(row["long"])
        print ("    " + str(line_count) + " To: " + str(row));
        distance.distance(fromZip, fromlat, fromlong, toZip, tolat, tolong, fileziptozipdistance)
        line_count += 1

if __name__ == '__main__':
    tozipdistances()
