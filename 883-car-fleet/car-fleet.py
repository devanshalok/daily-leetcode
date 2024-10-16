class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[]
        
        # Make pairs of position and speed and sort them
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
        pairs.sort()
        stack=[]
        
        # Iterate the stack from the top
        # Calculate the time taken by each car to reach target
        for i,j in pairs[::-1]:
            t= (target-i)/j

            # If the top of stack is less than the incoming element 
            # (this indicates that if time is less than incoming its slower and can catch up) 
            if not stack or stack[-1]<t:
                stack.append(t)
            
        return len(stack)