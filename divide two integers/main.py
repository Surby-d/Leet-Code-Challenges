class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quo = int(dividend/divisor)
        e, s = 2**31 -1, -2**31
        if quo<s:
            return s
        elif quo>e:
            return e
        else:
            return quo
