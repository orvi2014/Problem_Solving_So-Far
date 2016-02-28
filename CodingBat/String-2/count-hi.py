def count_hi(str):
    count=0
    for i in range(len(str)-1):
        count += str[i]=='h' and str[i+1]=='i'
    return count
