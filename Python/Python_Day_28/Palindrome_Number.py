class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True
        else:
            rev_num=0 
            num=x
            for i in range(len(str(x))):
                rev_num=rev_num*10+num%10
                num=num//10
            if rev_num==x:
                return True
            else:
                print(rev_num,'from 2')
                return False
                

        