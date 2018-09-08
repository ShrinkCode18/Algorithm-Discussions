# Convex Hull
**Presented by Kushashwa Ravi Shrimali (https://github.com/krshrimali)**

**Convex Hull:** Minimum bounding shape around the given input points. 

**Existing Algorithms** (Notable)

1. Sklanksy Algorithm - 1972 and 1982 - Both were proved wrong.
2. Graham Scan Algorithm O(nlogn)
3. Chan's Algorithm O(nlogn)

We discussed Graham Scan Algorithm and it's implementation.

Working:

Input: Input Points / Contours (for an image)

1. **Select bottom most point**

```cpp
struct Point {
  int x, y;
};

Point p0; // Bottom most point

// Find bottom most point
// In case of same y values - choose left most point
void findBottomMostPoint(Point points[], int n) {
  int ymin = points[0].y;
  for(int i = 1; i < n; i++) {
    int y = points[i].y;
    
    // Pick bottom most point
    if((y < ymin) || (ymin == y && points[i].x < points[min].x))
      ymin = points[i].y, min = i;
  }

  // Place bottom most point at first position
  swap(points[0], points[min])
}
```

2. **Sort Points** (Quick sort, based on polar angle from bottom most point)

```cpp
// sort the rest n-1 points based on polar angles from bottom most point
p0 = points[0]; // bottom most point
// for compare function: reference [1]
qsort(&points[1], n-1, sizeof(Point), compare);
```

3. **Accept and Reject Points**

Choose 3 points such that:

Traverse the path and remove concave points from the path. For three points
(point next to top of the stack, top of the stack and previous to top), if the
orientation is clock-wise then reject, else accept.

For code: reference [1]

### References

1.
[https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/](Geeksforgeeks:
Graham Scan Algorithm)

2. [http://www.dcs.gla.ac.uk/~pat/52233/slides/Hull1x1.pdf](Graham Scan Slides)

3.
[https://www.learnopencv.com/convex-hull-using-opencv-in-python-and-c/](Convex
Hull in C++ and Python - OpenCV) by Kushashwa Ravi Shrimali

