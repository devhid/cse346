from graph import Graph

def main(matrix, src, dst):
    graph = Graph(matrix)

    # Outputs the 3 - link disjoint shortest paths. 
    for i in range(3):
        path = list(graph.djikstra(src, dst))

        print("\n{index}) Shortest path from node {src} to node {dst}: {path}".format(index=i+1, src=src, dst=dst, path=path))
        print("Total Distance: {distance}".format(distance=graph.get_total_distance(path)))

        graph.remove_links(path)

if __name__ == "__main__":
    matrix = [
         #1   #2   #3   #4   #5   #6   #7
        [0,   2,   4,   0,   0,   0,   1],
        [2,   0,   5,   2,   2,   0,   0],
        [4,   5,   0,   8,   0,   2,   0],
        [0,   2,   8,   0,   2,   2,   4],
        [0,   2,   0,   2,   0,   0,   1],
        [0,   0,   2,   2,   0,   0,   1],
        [1,   0,   0,   4,   1,   1,   0]
    ]

    main(matrix=matrix, src=1, dst=4)