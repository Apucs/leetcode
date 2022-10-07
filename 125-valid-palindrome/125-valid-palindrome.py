class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_new = ''.join(filter(str.isalnum, s.lower()))
      
        for i in range(len(s_new)):
            
            n = len(s_new)-1-i
            
            if i< n:
                if s_new[i] != s_new[n]:
                    return False
                
                
        return True
                