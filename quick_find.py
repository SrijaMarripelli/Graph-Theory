class QuickFindUF:
    def __init__(self, N):
        self.id = [i for i in range(N)]

    def connected(self, p, q):
        return self.id[p] == self.id[q]
    
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

# Create an instance of QuickFindUF with 10 elements (0 to 9)
uf = QuickFindUF(10)

# Perform union operations
uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)
uf.union(8, 9)

# Check for connectivity
print(uf.connected(0, 1))
print(uf.connected(1, 2))
print(uf.connected(4, 5))
print(uf.connected(7, 8))