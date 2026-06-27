class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for op in s:
            if op == "*":
                result = result[:len(result) - 1]
            elif op == "#":
                result += result
            elif op == "%":
                result = result[::-1]
            else:
                result += op
        
        return result