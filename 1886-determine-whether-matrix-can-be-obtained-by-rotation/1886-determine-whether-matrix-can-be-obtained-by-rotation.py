class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        if mat==target: return True
        
        def rotation90(matrix):
            
            l, r = 0, len(matrix)-1
        
            while l<r:
                for i in range(r-l):
                    top, bottom = l, r

                    topLeft = matrix[top][l+i]

                    matrix[top][l+i] = matrix[bottom-i][l]
                    matrix[bottom-i][l] = matrix[bottom][r-i]
                    matrix[bottom][r-i] = matrix[top+i][r]
                    matrix[top+i][r] = topLeft

                l+=1
                r -= 1
                top+=1
                bottom-=1
            
            return matrix
                
        rotated_mat = mat
        for i in range(3):
            rotated_mat = rotation90(rotated_mat)
            if rotated_mat==target:
                return True
        
        return False