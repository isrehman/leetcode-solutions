class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Bağlayan mötərizə → açan mötərizə mapping
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # Bağlayan mötərizədirsə
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:  # Açan mötərizədirsə
                stack.append(char)
        
        return not stack