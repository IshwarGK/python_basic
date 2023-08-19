class Solution:
    def largestValues(self, root):
        list1 = []
        a = 0
        round1 = 0
        len1 = len(root) - 1
        while a >= len1:
            if round1 == 0:
                list1.append(root[0])
                round1 = 1
                a = 1
                continue
            
            round1 += 1
            num1 = max(root[a:2**rount1])
            list1.append(num1)
            a = 2**round1
        
        return list1

if __name__ == "__main__":
    obj = Solution()
    ans = obj.largestValues([1,3,2,5,3,None,9])
    print(ans)
    