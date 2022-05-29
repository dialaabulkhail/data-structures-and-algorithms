from code_challenge28.quick_sort import quicksort

def test_Quick_sort():
    arr = [8,4,23,42,16,15]
    assert [4, 8, 15, 16, 23, 42] == quicksort(arr)

    arr2 = [20,18,12,8,5,-2]
    assert [-2, 5, 8, 12, 18, 20] == quicksort(arr2)

    arr3 = [2,3,5,7,13,11]
    assert [2,3,5,7,11,13] == quicksort(arr3)

    arr4 = [5,12,7,5,5,7]
    assert [5,5,5,7,7,12] == quicksort(arr4)