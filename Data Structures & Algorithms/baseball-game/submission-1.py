class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in range(len(operations)):
            o = operations[i]
            if o == "+":
                s.append(str(int(s[-1])+int(s[-2])))
            elif o == "D":
                s.append(str(int(s[-1])*2))
            elif o == "C":
                s.pop()
            else:
                s.append(o)
        print(s)
        tot = 0
        for i in s:
            tot+=int(i)
        return tot