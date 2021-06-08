coordinatesList = [[33.747252,-112.633853],[-33.867886, -63.987],[41.303921, -81.901693],[-33.350534, -71.653268]]

for x in coordinatesList:
    for y in x:
        if y < 0:
            print(y)

longitude = []
for x in coordinatesList:
    longitude.append(x[1])
print(longitude)

latitude = []
for x in coordinatesList:
    latitude.append(x[0])
print(latitude)

# //longitude = [] // for loop in coordinate longitude longitude = coordinatesList[0][1];
# -112.633853
# -63.987
# -81.901693
# -71.653268