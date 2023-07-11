def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i+=1
        elif stk and stk[-1]<arr[i]:
            stk.append(arr[i])
            i+=1
        elif stk and stk[-1]>=arr[i]:
            stk.pop()
        
    return stk