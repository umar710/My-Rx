def find_min_platforms(arr, dep):
    def time_to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    arr = [time_to_minutes(t) for t in arr]
    dep = [time_to_minutes(t) for t in dep]

    arr.sort()
    dep.sort()

    platform_needed = 0
    max_platforms = 0
    i, j = 0, 0
    n = len(arr)

    while i < n and j < n:

        if arr[i] <= dep[j]:
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:
            
            platform_needed -= 1
            j += 1

    return max_platforms


arr = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(find_min_platforms(arr, dep))  # Output: 3

arr = ["9:00", "9:40"]
dep = ["9:10", "12:00"]
print(find_min_platforms(arr, dep))  # Output: 1