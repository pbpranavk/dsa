def find_max_sum(arr,n):
    dp = [0] * n

    if n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    elif n == 3:
        dp[0]=arr[0]
        dp[1]=arr[1]
        dp[2]=arr[2]+arr[0]
        return max(dp[2],dp[0])
    else:
        dp[0]=arr[0]
        dp[1]=arr[1]
        dp[2]=arr[2]+arr[0]
        for i in range(3,n):
            dp[i]=arr[i]+max(dp[i-2],dp[i-3])

        return max(dp[n-1],dp[n-2]);

arr = [5, 5, 10, 100, 10, 5]
print(find_max_sum(arr, len(arr)))