import sys
input = sys.stdin.readline
MAX = sys.maxsize
sys.setrecursionlimit(10**6)
    
dp = [] 
def go(num,rem):
	global dp
	if num >= N:
		return 0
	
	elif dp[num][rem] != MAX:
		return dp[num][rem]
	
	else:
	 	#다음 줄에 작성하기
		next_rem = M - arr[num]
		dp[num][rem] = rem * rem + go((num + 1), next_rem)
		
		#현재 줄에 작성할 수 있는 경우, 최솟값 찾기
		if arr[num] < rem and rem > 0:
			next_rem = rem - arr[num] - 1
			dp[num][rem] = min(dp[num][rem], go((num + 1), next_rem))
	return dp[num][rem]

if __name__ == "__main__":
	N, M = map(int,input().split())
	arr = list( int(input()) for _ in range(N) )
	dp = list( [MAX] * (M+1) for _ in range(N) )
	
	answer = go(1, M - arr[0])
	print(answer)