class QuickUnionUF:
    def __init__(self, N):
        self.id = [i for i in range(N)]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

# Create an instance of QuickUnionUF with 10 elements (0 to 9)
uf = QuickUnionUF(10)

# Perform union operations
uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)
uf.union(8, 9)

# Check for connectivity
print(uf.connected(0, 1))  # Should print True
print(uf.connected(1, 2))  # Should print False
print(uf.connected(4, 5))  # Should print True
print(uf.connected(7, 8))  # Should print False