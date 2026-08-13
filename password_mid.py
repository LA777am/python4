class Solution:
    def passwordStrength(self, password: str) -> int:
        score=0
        done= set(password)
        for i in done:
            if not i.isalnum():
                score+=5
            elif i.islower():
                score+=1
            elif i.isupper():
                score+=2
            else:
                score+=3
    
        return score 
            