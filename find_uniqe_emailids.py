class Solution:
    def numUniqueEmails(self, emails) -> int:
        set1 = set()
        for i in emails:
            new_email = ""
            list2 = i.split('@')
            if '+' in list2[0]:
                new_email = list2[0].split('+')[0]
            
            if '.' in list2[0]:
                if new_email:
                    new_list = new_email.split(".")
                    new_email = "".join(new_list)
                else:
                    new_list = list2[0].split(".")
                    new_email = "".join(new_list)
                    
            if not new_email:
                new_email = list2[0]
            
            if new_email:
                str1 = "{}@{}".format(new_email, list2[1])
                #print(str1)
                set1.add(str1)
                
            new_email = ""
        print(set1)
        return len(set1)
                            
if __name__ == "__main__":
    obj = Solution()
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    l = obj.numUniqueEmails(emails=emails)
    print(l)
    
    #5 = true
    #6 = true
    #7 = true
    #8 = 1, 1,