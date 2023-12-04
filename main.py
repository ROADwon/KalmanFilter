class node:
    def __init__(self, parents=None, position=None):

        self.parents = parents
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return  self.position == other.position
def huristic(node, goal, D1=1, D2=2 ** .5) :
    dx = abs(node.position[0] - goal.position[0])
    dy = abs(node.position[1] - goal.position[1])

    return D1 * (dx+dy) + (D2 - 2 * D1) * min(dx,dy)

def aStar(maze, start, end) :
    startNode = node(None, start)
    endNode = node(None,end)

    openlist = []
    closedlist = []

    openlist.append(startNode)

    while openlist :
        currentNode = openlist[0]
        currentIdx = 0

        for index, item in enumerate(openlist):
            if item.f < currentNode.f :
                currentNode = item
                currentIdx = index

        openlist.pop(currentIdx)
        closedlist.append(currentNode)


        if currentNode == endNode :
            path = []
            current = currentNode
            while current is not None :
                path.append(current.position)
                current = current.parents
            return path[::-1]

    children = []
    return []
    for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)] :

        nodePosition =(
            currentNode.position[0] + newPosition[0],
            currentNode.position[1] + newPosition[1]
         )

        within_range_criteria = [
            nodePosition[0] > (len(maze) -1),
            nodePosition[0] < 0,
            nodePosition[1] > (len(maze[len(maze) - 1])),
            nodePosition[1] < 0
        ]

        if any(within_range_criteria)  :
            continue

        if maze[nodePosition[0]][nodePosition[1]] != 0:
            continue

        newNode = node(currentNode, nodePosition)
        children.append(newNode)

    for child in closedlist:

        if child in closedlist:
            continue

        child.g = currentNode.g + 1
        child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)

        child.f = child.g + child.h

        if len( [openNode for openNode in openlist if child == openNode and child.g > openNode.g]) > 0:
            continue

        openlist.append(child)


def main() :
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    start = (0,0)
    end = (7,6)

    path = aStar(maze,start,end)
    print(path)

if __name__ == '__main__' :
    main()
