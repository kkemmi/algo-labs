def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def can_place_cows(stalls, n, c, min_dist):
    count = 1
    last_position = stalls[0]

    for i in range(1, n):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]

            if count == c:
                return True

    return False


def largest_min_distance(stalls, n, c):
    if c <= 1:
        return 0


    stalls = merge_sort(stalls)

    left = 1
    right = stalls[-1] - stalls[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place_cows(stalls, n, c, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result