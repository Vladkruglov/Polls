class Solution:
    def isValid(s: str) -> bool:    
        dict={')':'(','}':'{',']':'['}
        stack = []
        brackets=['(', ')', '{', '}', '[', ']']
        garbage=[]
        for i in s:
            if i not in brackets:
                garbage.append(i)
                i=+1
            elif i not in dict:
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != dict[i]:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        

                
if __name__ == "__main__":
    s = input("string for isValid: ")
    print(Solution.isValid(s))