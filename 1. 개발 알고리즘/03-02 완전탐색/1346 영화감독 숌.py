n = int(input())
movie = 666

#O(n) 만큼 수행되는데, n=10,000  타임아웃안남.
while n:
    # if n == 0:
        # break
    if "666" in str(movie):
        n -= 1
    movie += 1
    # print(movie)

print(movie - 1)

