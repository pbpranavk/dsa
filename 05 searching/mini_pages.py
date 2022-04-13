# TODO:Redo this

def is_possible(arr, n , m, curr_min):
    students_req = 1
    curr_sum = 0

    for i in range(n):
        if arr[i] > curr_min:
            return False

        if curr_sum + arr[i] > curr_min:
            students_req += 1
            curr_sum = arr[i]

            if students_req > m:
                return False
        else:
            curr_sum += arr[i]
    return True


def find_pages(arr, n, m):
    sum = 0

    if n < m:
        return -1

    for ele in arr:
        sum += ele

    start = 0
    end = n-1
    result = 10 ** 9

    while start < end:
        mid = (start + end) // 2
        if is_possible(arr, n , m ,mid):
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result

arr = [12, 34, 67, 90]

print(find_pages(arr, len(arr), 2))