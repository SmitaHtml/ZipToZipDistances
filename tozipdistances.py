import csv
import distance

def tozipdistances(file_name, fromZip, fromlat, fromlong, fileziptozipdistance):

    with open(file_name) as csv_file_inner:
        csv_reader_inner = csv.reader(csv_file_inner, delimiter=',')
        line_count = 0
        for row in csv_reader_inner:
            if line_count == 0:
                #print('         ToZip: Ignore column header');
                line_count += 1
            else:
                toZip = row[0]
                tolat = float(row[1])
                tolong = float(row[2])
                #print('         ', line_count,'ToZip: ', toZip, tolat, tolong);
                distance.distance(fromZip, fromlat, fromlong, toZip, tolat, tolong, fileziptozipdistance)
                line_count += 1

if __name__ == '__main__':
    tozipdistances()
