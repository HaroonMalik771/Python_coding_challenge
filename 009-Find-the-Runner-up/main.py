if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winnerlist = list(arr)
    runnerlist = set(winnerlist)
    runnerlist.remove(max(runnerlist))
    print(max(runnerlist))    # Print the maximum element in runnerlist (which is now the highest)
