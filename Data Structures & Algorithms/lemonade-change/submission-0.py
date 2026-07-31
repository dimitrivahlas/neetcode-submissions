class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for b in bills:
            if b == 5:
                five +=1
            elif b == 10:
                ten +=1
                if five > 0:
                    five -= 1
                else: 
                    return False
            else:
                diff = b-5
                if diff == 15 and five > 0 and ten >0:
                    five -=1
                    ten -=1
                elif diff == 15 and five >= 3:
                    five -=3
                else:
                    return False
        return True
                
