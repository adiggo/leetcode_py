class Solution(object):
    def addOperators(self, num, target):
        res = []
        self.dfs(res, [], num, 0, target, 0, 0)
        return res

    def dfs(self, res, exps, num, index, target, prev, multi):
        if index == len(num):
            if target == prev:
                res.append(''.join(exps))
            return

        for i in xrange(index, len(num)):
            # for prefix 0, only '0' allowed
            if num[index] == '0' and i != index:
                break
            cur_s = num[index: i + 1]
            cur = int(cur_s)

            if index == 0:
                exps.append(cur_s)
                self.dfs(res, exps, num, i + 1, target, cur, cur)
                exps.pop()
            else:
                exps.append('+')
                exps.append(cur_s)
                self.dfs(res, exps, num, i + 1, target, prev + cur, cur)
                exps.pop()
                exps.pop()

                exps.append('-')
                exps.append(cur_s)
                self.dfs(res, exps, num, i + 1, target, prev - cur, -cur)
                exps.pop()
                exps.pop()

                exps.append('*')
                exps.append(cur_s)
                self.dfs(res, exps, num, i + 1, target, prev - multi + multi * cur, multi * cur)
                exps.pop()
                exps.pop()
