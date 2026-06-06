class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        s = ("+", "-", "*", "/")

        for t in tokens:
            print(stack)
            if t in s:
                a = stack[-2]
                b = stack[-1]
                stack.pop()
                stack.pop()
                if t =="+":
                    stack.append(int(a)+int(b))
                elif t =="-":
                    stack.append(int(a)-int(b))
                elif t =="/":
                    stack.append(int(a)/int(b))
                else:
                    stack.append(int(a)*int(b))
            else:
                stack.append(t)
        
        return int(stack[-1])