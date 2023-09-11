class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            self.parent[root_p] = root_q

if __name__ == "__main__":
    N = 6  # Set the value of N as per your requirement
    uf = UF(N)
    
    # Sample input
    input_data = [
        (1, 2),
        (2, 3),
        (4, 5),
        (3, 4),
        (0, 5)
    ]
    
    for p, q in input_data:
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f"{p} {q}")
