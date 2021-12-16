def Merge(array_left,array_right):
    n = len(array_left) + len(array_right)
    i = 0
    j = 0
    array_merged = []
    for k in range(n):
        if array_left[i] < array_right[j]:
            array_merged.append(array_left[i])
            if i == len(array_left)-1:
                array_merged += array_right[j:]
                return array_merged
            else:
                i += 1
        else:
            array_merged.append(array_right[j])
            if j == len(array_right)-1:
                array_merged += array_left[i:]
                return array_merged
            else:
                j += 1


def mergeSort(array):
    if len(array) == 1:
        return array
    else:
        n = int(len(array)/2)
        array_1 = array[0:n]
        array_2 = array[n:]
        array_1 = mergeSort(array_1)
        array_2 = mergeSort(array_2)
        return Merge(array_1,array_2)
        

# Test
if __name__ == "__main__":
    array = [5,4,1,8,7,2,6]
    print(mergeSort(array))
        
