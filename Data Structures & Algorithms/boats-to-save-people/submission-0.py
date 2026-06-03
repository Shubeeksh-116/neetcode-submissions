class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j = 0,len(people)-1
        res = []
        while i<=j:
            if (people[i]+people[j])>limit:
                res.append([people[j]])
                j-=1
            else:
                res.append([people[i],people[j]])
                j-=1
                i+=1
        return len(res)