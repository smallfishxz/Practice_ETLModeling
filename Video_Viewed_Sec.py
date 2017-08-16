# This is built on top of the max points in interval ranges overlaps, and return only the not_watched seconds.
# Please refer to the txt file for correct idea.

def points_in_interval(L):
    intervals = []
    n = len(L)
    for i in range(0, n):
        a, b = L[i][0], L[i][1]
        intervals.append((int(a), 1))
        intervals.append((int(b), -1))
    print(intervals)

    intervals.sort(key=lambda i: (i[0], -i[1]))
    print(intervals)
    s = 0
    r = []
    non_views = 0
    # the non_viewed intervals start from 0 and end as 1
    for i, pair in enumerate(intervals):
        pair = intervals[i]
        s = s + pair[1]
        # if s == 1:
        #   r.append((pair[0], 1))
        # First append all starting point with value as 0
        if s == 0:
          r.append((pair[0], 0))
          j = i + 1
          # Find the first point with value as 1 to append as one interval in the final interval range
          # At the same time add this difference betwee the start point and end point to the non_views
          while j < len(intervals):
            if intervals[j][1] == 1:
              r.append((intervals[j][0], 1))
              non_views += intervals[j][0] - pair[0]
              break
            else:
              j += 1

    return (r, non_views)

print(points_in_interval([[2,5],[3,6],[7,8],[20,30],[40,80]]))
