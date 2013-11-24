from ti.leetcode.LeetcodeProblem import LeetcodeProblem


class GrayCode(LeetcodeProblem):
    def solve(self, n):
        i = 0
        res = [0]
        base = 1

        while i < n:
            copy = [x + base for x in res]
            copy.reverse()
            res += copy

            i += 1
            base *= 2
        return res

    def verify(self, input, s1, s2):
        return s1 == s2

    def input(self):
        from Parser import parseOneInt
        return parseOneInt(open(self.inputPath))

    def output(self):
        from Parser import parseIntArray
        for o in parseIntArray(open(self.outputPath)):
            yield o[0]

problem = GrayCode
