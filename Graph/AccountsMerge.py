"""
Solution (DFS):
Runtime 70% O(Elog(E))
Memory 21% O(E * A)

Attempt 2 (Union Find):
Runtime 6% O(E^2)
Memory 54% O(E) (num emails)

Attempt 1 (Union Find):
Runtime 5% O(E^2)
Memory 54% O(E) (num emails)
"""


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, x: int):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)

        self.parent[xParent] = yParent


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = [False] * len(accounts)
        emailToAccount = defaultdict(list)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                emailToAccount[email].append(i)

        def dfs(acct: int, emails: List[str]):
            if visited[acct]:
                return
            visited[acct] = True

            for email in accounts[acct][1:]:
                emails.add(email)
                for nextAcct in emailToAccount[email]:
                    dfs(nextAcct, emails)

        res = []
        for ind, account in enumerate(accounts):
            if visited[ind]:
                continue
            name = account[0]
            emails = set()
            dfs(ind, emails)
            res.append([name] + sorted(emails))

        return res

    def accountsMergeAttempt2(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = UnionFind(len(accounts))

        emailToAcct = {}
        for ind, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcct:
                    unionFind.union(emailToAcct[email], ind)
                else:
                    emailToAcct[email] = ind

        emailGroup = defaultdict(list)
        for email, acct in emailToAcct.items():
            parentGroup = unionFind.find(acct)
            emailGroup[parentGroup].append(email)

        res = []
        for acct, emails in emailGroup.items():
            res.append([accounts[acct][0]] + sorted(emails))

        return res

    def accountsMergeAttempt1(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToNameAndNumber = {}
        counter = 0
        for name, *emails in accounts:
            for email in emails:
                if email not in emailToNameAndNumber:
                    emailToNameAndNumber[email] = (name, counter)
                    counter += 1
        print(emailToNameAndNumber)
        numToEmails = {num: email for email, (name, num) in emailToNameAndNumber.items()}

        unionFind = UnionFind(len(emailToNameAndNumber.keys()))
        for name, *emails in accounts:
            for i in range(1, len(emails)):
                emailXNum = emailToNameAndNumber[emails[i - 1]][1]
                emailYNum = emailToNameAndNumber[emails[i]][1]
                unionFind.union(emailXNum, emailYNum)

        parentEmailToUnionEmails = {}
        for email, (name, num) in emailToNameAndNumber.items():
            parentEmail = numToEmails[unionFind.find(num)]
            unionEmails = parentEmailToUnionEmails.get(parentEmail, [])
            unionEmails.append(email)
            parentEmailToUnionEmails[parentEmail] = unionEmails
        print(parentEmailToUnionEmails)

        res = []
        for parent, unionEmails in parentEmailToUnionEmails.items():
            name = emailToNameAndNumber[parent][0]
            res.append([name] + sorted(unionEmails))

        return res
