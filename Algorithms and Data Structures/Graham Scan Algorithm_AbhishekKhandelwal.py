#Abhishek Khandelwal
def slope(q):
    x0,y0 = lowest_point
    x1,y1 = q
    #print lowest_point,q
    #print float(y0-y1)/(x0-x1)
    return float(y0-y1)/(x0-x1)

n = int(raw_input("Enter number of Points"))
points = []
lowest_point = (100,100)
for i in xrange(n):
    point = tuple(map(int,raw_input().split()))
    points.append(point)
    if point[1]<lowest_point[1]:
        lowest_point = point
    elif point[0]<lowest_point[0] and point[1]==lowest_point[1]:
            lowest_point = point

points.remove(lowest_point)
points.sort(key = slope)
print points
