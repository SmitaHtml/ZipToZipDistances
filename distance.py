import geopy
import geopy.distance

def distance(fromZip, fromlat, fromlong, toZip, tolat, tolong, fileziptozipdistance):

    coords_1 = (fromlat, fromlong)
    coords_2 = (tolat, tolong)

    #coords_1 = (fromlat, fromlong)
    #coords_2 = (tolat, tolong)

    try:
        ziptozipdistance = geopy.distance.geodesic(coords_1, coords_2).miles
        #successfull distance calculation
        print ("                From zip: ", fromZip, " To zip: ", toZip, "Distance is: ", ziptozipdistance)
        fileziptozipdistance.write(str(fromZip) + ", " + str(toZip) + ", " + str(ziptozipdistance) + "\n")

    except ValueError:
        #error in distance calculation
        if fromlat < -90 or fromlat > 90:
            print ("                From zip: ", fromZip, " To zip: ", toZip, "Error: Latitude must be in the [-90; 90] range.")
            fileziptozipdistance.write(fromZip, toZip, "Error: Latitude must be in the [-90; 90] range." + "\n")
        else:
            print ("                From zip: ", fromZip, " To zip: ", toZip, "Error: value error.")
            fileziptozipdistance.write(fromZip, toZip, "Error: value error."+ "\n")

if __name__ == '__main__':
    distance()
