class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        sec=0
        while True:
            i=0
            while i <len(position)-1:
                if position[i+1]-position[i]<=distance :
                    position.pop(i)
                    speed.pop(i)
                    continue
                i+=1 
            y= sorted(speed)
            if speed==y:
                return len(position)
            sec+=1
            for i in range(len(position)):
                position[i]+=speed[i]*sec