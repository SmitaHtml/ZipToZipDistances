import geopy
import geopy.distance
import sys

def distance(fromZip, fromlat, fromlong, toZip, tolat, tolong, fileziptozipdistance):

    coords_1 = (fromlat, fromlong)
    coords_2 = (tolat, tolong)

    #coords_1 = (fromlat, fromlong)
    #coords_2 = (tolat, tolong)

    try:
        if fromlat < -90 or fromlat > 90 or tolat < -90 or tolat > 90:
            print ("        From zip: ", fromZip, " To zip: ", toZip, " Error: Latitude must be in the [-90; 90] range.")
            errorrow = str(fromZip) + ", " + str(toZip) + ", " + " Error: Latitude must be in the [-90; 90] range." + "\n"
            fileziptozipdistance.write(errorrow)
        else:
            ziptozipdistance = geopy.distance.geodesic(coords_1, coords_2).miles
            if ziptozipdistance < 200:
                print ("        From zip: ", fromZip, " To zip: ", toZip, " Distance is: ", ziptozipdistance)
                fileziptozipdistance.write(str(fromZip) + ", " + str(toZip) + ", " + str(ziptozipdistance) + "\n")
            else:
                print ("        From zip: ", fromZip, " To zip: ", toZip, " Distance is >= 200 miles")
                fileziptozipdistance.write(str(fromZip) + ", " + str(toZip) + " Distance is >= 200 miles\n")
    except ValueError:
        #error in distance calculation
            print ("        From zip: ", fromZip, " To zip: ", toZip, " Error: value error.")
            valueerrorrow = str(fromZip) + ", " + str(toZip) + ", " + " Error: value error." + "\n"
            fileziptozipdistance.write(valueerrorrow)

if __name__ == '__main__':
    distance()
