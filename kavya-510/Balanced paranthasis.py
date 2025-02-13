def Balanced(s):
    stack=[]
    for ch in s:
        if ch=='{'or ch=='['or ch=='{':
            stack.append(ch)
        elif not stack:#len(stack)==0
            return 'Not Balanced'
        elif ch=='}':
            if stack[-1]=='{':
                stack.pop()
            else:
                return "Not Balanced"
        elif ch==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                return"not Balanced"
        elif ch==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                return"not Balanced"
    return "Not Balanced"if stack else "Balanced"
if __name__=="__main__":
    s=input()
    print(Balanced(s))
