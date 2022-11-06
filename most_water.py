def maxArea(hieght: list[int]) -> int:
    max_area = None
    for i in range(len(hieght)):
        for j in range(i, len(hieght)):
            area = (j - i) * min(hieght[i], hieght[j])
            if max_area == None or max_area < area:
                max_area = area

    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
