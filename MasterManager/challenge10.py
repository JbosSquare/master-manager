a, pos= ["1"], 30
for i in range(1, pos+1):
    response, last, count = '', '', 0
    for c in a[i-1]:
        if(last != '' and last != c):
            response += str(count)+last
            count = 1
        else:
            count += 1
        last = c
    response += str(count)+last
    a.append(response)
print(len(a[30]))
print(a[-1])