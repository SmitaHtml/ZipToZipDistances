import csv
import geopy
import geopy.distance

try:

    infile_name = "zipcodes0.csv";
    open_fromzip_infile = csv.DictReader(open(infile_name));

    outfile_name = "outfile.csv";
    open(outfile_name, 'w').close(); # deletes output file content
    open_outfile = open(outfile_name, "a");
    open_outfile.write("fromZip, fromLat, fromLong, toZip, toLat, toLong, distanceBetweenZipsInMiles\n")

    from_line_count = 1
    for fromziprow in open_fromzip_infile:
        fromzip = fromziprow["zip"]
        fromlat = fromziprow['lat']
        fromlong = fromziprow['long']
        print(str(from_line_count) + " " + str(fromzip) + ",  " + str(fromlat) + ",  " + str(fromlong));
        open_tozip_infile = csv.DictReader(open(infile_name));
        to_line_count = 1

        for toziprow in open_tozip_infile:
            tozip = toziprow["zip"]
            tolat = toziprow['lat']
            tolong = toziprow['long']
            print("     " + str(to_line_count) + " " + str(tozip) + ",  " + str(tolat) + ",  " + str(tolong));

            coords_1 = (fromlat, fromlong)
            coords_2 = (tolat, tolong)
            try:
                ziptozipdistance = geopy.distance.geodesic(coords_1, coords_2).miles #calculates distance between two coordinates with lat and long
                if ziptozipdistance < 200:
                    print ("            From zip: ", fromzip, " To zip: ", tozip, " Distance is: ", ziptozipdistance, "\n")
                    outputrow = str(fromziprow['zip'] + ", " + fromziprow["lat"] + ", " + fromziprow["long"] + ", " + toziprow['zip'] + ", " + toziprow["lat"] + ", " + toziprow["long"] + ", " + str(ziptozipdistance))
                    open_outfile.write(outputrow + "\n");
            except Exception as e:
                #print("Exception encountered: {}".format(e))
                print("           " + str(fromzip) + ", " + str(tozip) + ", " + " Error encountered: {}".format(e) + "\n")
                outputrow = str(fromziprow['zip'] + ", " + fromziprow["lat"] + ", " + fromziprow["long"] + ", " + toziprow['zip'] + ", " + toziprow["lat"] + ", " + toziprow["long"]) + ", " + " Error encountered: {}".format(e)
                open_outfile.write(outputrow + "\n")
                pass

            to_line_count += 1
        from_line_count += 1

except Exception as e:
    print("Exception encountered: {}".format(e))
