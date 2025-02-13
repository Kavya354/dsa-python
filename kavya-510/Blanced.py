def isBalanced(s):
    stk=[]
    pairs={'}':'{',']':'[',')':'('}
    for val in s:
        if val in '{[(':
            stk.append(val)
        elif val in']})':
            if not stk or stk[-1]!=pairs[val]:
                return 'Not Balance'
            else:
                stk.pop()
    return 'balanced'if len(stk)==0 else 'Not Balanced'
if __name__=="__main__":
    s=input()
    print(isBalance(s))