class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return

            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        ansChars = []
        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            ansChars.append(chr(root + ord('a')))

        return "".join(ansChars)         