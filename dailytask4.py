def combination(n,r):
    if r>n-r:  # Use the smaller of r and n-r for efficiency
        r=n-r
    result=1
    for i in range(r):
        result=result*(n-i)//(i+1)
    return result

def pascals_triangle(n):
    t=[]
    for i in range(n):
        row=[]
        for j in range(i+1):
            row.append(combination(i,j))
        t.append(row)
    return t

rows=6
triangle=pascals_triangle(rows)
for row in triangle:
    print(row)

    

    #  aptitude
    # amount of water=3/8v
    # amount of syrup=5/8v
    #
    # amount of water left=3/8-3/8
    # amount of syrup left=5/8-5/8
    #
    # final answer=1/5