def find_uniq(arr):
    # your code here
    diffs = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            diffs.append(i)
    if len(diffs) == 1:
        if diffs[0] == 0:
            return arr[0]
        else:
            return arr[-1]
    else:
        return arr[diffs[1]]
