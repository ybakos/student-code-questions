# A tree node.
# FIXME: Make this a real tree node.

class Node:

    def __init__(self, x, y, value):
        self.color = color(random(255), random(255), random(255), 150)
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.theta = 0.0
        self.value = value
        self.inOrder = []
        self.preOrder = []
        self.postOrder = []
    
    def draw(self):
        noStroke()
        fill(self.color)
        ellipse(self.x, self.y, 100, 100)
        ellipse(self.x, self.y, 10, 10)
        textAlign(CENTER, CENTER)
        textSize(32)
        fill(33)
        #text((' '.join(map(str, self.inOrder))), 40, 40)
        text(self.value, self.x, self.y)
        if (self.left != None):
            self.left.draw()
            stroke(50)
            strokeWeight(1)
            line(self.x, self.y, self.left.x, self.left.y)
        if (self.right != None):
            self.right.draw()
            stroke(50)
            strokeWeight(1)
            line(self.x, self.y, self.right.x, self.right.y)
        
    def move(self):
        self.y += 0.5 * cos(self.theta)
        self.theta += 0.1
        if (self.left != None):
            self.left.move()
        if (self.right != None):
            self.right.move()


    def add(self, node):
        if (self.value <= node.value):
            if (self.left == None):
                node.x = self.x + 150
                node.y = self.y + 150
                self.left = node
                self.inOrder.append(node.value)
            else:
                self.left.add( Node(0, 0, node.value) )

        else:
            if (self.right == None):
                node.x = self.x - 150
                node.y = self.y + 150
                self.right = node
            else:
                self.right.add( Node(0, 0, node.value) )