class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        
        curr_window = 0
        max_win = 0
        
        max_count = 0
        
        char_count = {}

        
        for r in range(len(s)):
            char_count[s[r]] = 1 + char_count.get(s[r], 0)
            max_count = max(max_count, char_count[s[r]])
            
            if(r-l+1 - max_count)>k:
                char_count[s[l]]-=1
                l+=1
                
            max_win = max(max_win, r-l+1)
            
        return max_win
            
            
        
        
        