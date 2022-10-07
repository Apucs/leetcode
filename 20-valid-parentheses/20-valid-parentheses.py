class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        # if len(s)<2: return False
        
        for c in s:
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
                # print(stack)
                
            if c==")":
                
                if len(stack)!=0 and stack[-1]== "(":
                    # print("before popping:", stack)
                    stack.pop()
                    # print("after popping:", stack)
                else: return False
                    
                    
            elif c=="}":
                if len(stack)!=0 and stack[-1]== "{":
                    # print("before popping:", stack)
                    stack.pop()
                    # print("after popping:", stack)
                    
                else: return False


            elif c=="]":
                if len(stack)!=0 and stack[-1]== "[":
                    # print("before popping:", stack)
                    stack.pop()
                    # print("after popping:", stack)
                else: return False

        
        return len(stack)==0
                
        
        