## 분할 정복 기법

반복 알고리즘O(n)

분할 정복 기반의 알고리즘 O(logn)



병합 정렬

여러 개의 정렬된 자료를 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식



```python
# 병합 정렬 과정

# 49, 10, 30, 2, 16, 8, 31, 22

# 단점: 메모리를 많이 사용함

def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr
    else:
        left = []
        right = []
        middle = length // 2
        for x in range(0, middle):
            left.append(arr[x])
        for y in range(middle, length):
            right.append(arr[y])
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)

def merge(left, right):
    result = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            elif left[0] > right[0]:
                result.append(right.pop(0))
        elif left and not right:
            result.append(left.pop(0))
        elif not left and right:
            result.append(right.pop(0))
    return result


my_list = [49, 10, 30, 2, 16, 8, 31, 22]
print(merge_sort(my_list))

```

퀵 정렬

```python

```

상태공간트리를 구축하여 문제를 해결