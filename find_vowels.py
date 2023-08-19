class Solution:
    def reverseVowels(self, s: str) -> str:
        len1 = len(s)
        a = 0
        b = len1 - 1
        b_yes = 0
        a_yes = 0
        tuple1 = ('a', 'e', 'i', 'o', 'u')
        list1 = list(s)
        print(tuple1)
        while a < b:
            print(a)
            print(b)
            if list1[a] in tuple1:
                a_yes = 1
            else:
                a += 1
                
            if list1[b] in tuple1:
                b_yes = 1
            else:
                b -= 1
            
            if a_yes and b_yes:
                list1[b], list1[a] = list1[a], list1[b]
                a_yes = 0
                b_yes = 0
                a += 1
                b -= 1
        print(list1)
        return "".join(list1)
            
if __name__ == "__main__":
    obj = Solution()
    str1 = obj.reverseVowels("hello")
    print(str1)