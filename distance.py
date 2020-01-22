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
            errorrow = str(fromZip) + ", " + str(toZip) + ", " + "Error: Latitude must be in the [-90; 90] range." + "\n"
            fileziptozipdistance.write(errorrow)
        else:
            ziptozipdistance = geopy.distance.geodesic(coords_1, coords_2).miles
            fileziptozipdistance.write(str(fromZip) + ", " + str(toZip) + ", " + str(ziptozipdistance) + "\n")
    except ValueError:
        #error in distance calculation
            valueerrorrow = str(fromZip) + ", " + str(toZip) + ", " + "Error: value error." + "\n"
            fileziptozipdistance.write(valueerrorrow)

if __name__ == '__main__':
    distance()
