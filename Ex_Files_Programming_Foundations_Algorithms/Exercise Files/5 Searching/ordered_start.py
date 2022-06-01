# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        pass
        midPt= (lowerIdx + upperIdx) // 2
        if itemlist[midPt] == item:
            return midPt
        if item > itemlist [midPt]:
            lowerIdx = midPt +1
        else:
            upperIdx = midPt -1


    if lowerIdx > upperIdx:
        return None


print(binarysearch(56, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
