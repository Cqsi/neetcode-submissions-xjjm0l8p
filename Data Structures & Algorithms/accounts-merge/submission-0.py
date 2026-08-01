class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        g = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name
                g[first_email].append(email)
                g[email].append(first_email)
        
        res = []
        visited = set()

        def dfs(email, component):
            visited.add(email)
            component.append(email)

            for nei in g[email]:
                if nei not in visited:
                    dfs(nei, component)

        for email in email_to_name:
            if email not in visited:
                comp = []
                dfs(email, comp)

                res.append([email_to_name[email]] + sorted(comp))
        
        return res