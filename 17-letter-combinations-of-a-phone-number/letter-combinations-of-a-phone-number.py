class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letters={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        if digits=='':
            return []

        stack=[]
        res=[]
        length=len(digits)

        stack.append("")

        while len(stack)>0:
            current=stack.pop()

            if len(current)==length:
                res.append(current)

            else:
                num_index=len(current)
                letters_stack=letters[digits[num_index]]

                for letter in letters_stack:
                    stack.append(current +letter)

        return res
        