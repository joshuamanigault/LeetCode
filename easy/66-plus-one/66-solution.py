class Solution:
    def plusOne(self, digits: list) -> list:
        num = int("".join(map(str, digits))) + 1
        num = str(num)
        return list(map(int, num))
        
        