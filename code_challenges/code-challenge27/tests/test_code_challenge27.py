from code_challenge27.merge_sort import merge_sort, merge

def test_merge_sort():
    arr = [8,4,23,42,16,15]
    assert [4, 8, 15, 16, 23, 42] == merge_sort(arr)

    arr2 = [20,18,12,8,5,-2]
    assert [-2, 5, 8, 12, 18, 20] == merge_sort(arr2)

    arr3 = [2,3,5,7,13,11]
    assert [2,3,5,7,11,13] == merge_sort(arr3)

    arr4 = [5,12,7,5,5,7]
    assert [5,5,5,7,7,12] == merge_sort(arr4)