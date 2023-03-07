
def search(r,c,start,n):
    global R,C,ans
    nn = (n//2)**2

    if R >= r+n//2 and C >= c+n//2: #11
        rstart = r+n//2
        cstart = c+n//2
        start += nn*3
    
    elif R >= r+n//2 and C < c+n//2: #10
        rstart = r+n//2
        cstart = c
        start += nn*2
    
    elif R < r+n//2 and C >= c+n//2: #01
        rstart = r
        cstart = c+n//2
        start += nn*1
    
    else: #00
        rstart = r
        cstart = c
        start += nn*0
    
    if n==2:
        ans = start 
        return
    
    search(rstart,cstart,start,n//2)

    if ans != 0 : 
        return


N,R,C = map(int,input().split())
# cnt = 0 
ans = 0

# if R==0 and C==0:
#     print(0)


search(0,0,0,2**N)

print(ans)


