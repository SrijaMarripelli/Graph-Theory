# The following code is used to represent a graph
# Time Complexity : O(n)

def main():
    n, m = map(int, input().split())
    # Adjacency matrix for undirected graph
    adj = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(m):
        u,v = map(int, input().split())
        adj[u][v] = 1
        adj[v][u] = 1 # This statement will be removed in case of directed graph


    # print the adjacency matrix
    for i in range(n):
        for j in range(n):
            print(adj[i][j], end=" ")
        print()


if __name__=="__main__":
   main()