class Piece:
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        self.neighbors = None
        self.numAround = 0

    def getHasBomb(self):
        return self.hasBomb

    def getClicked(self):
        return self.clicked

    def getFlagged(self):
        return self.flagged

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    def setNumAround(self):
        for piece in self.neighbors:
            if piece.getHasBomb():
                self.numAround += 1

    def toggleFlag(self):
        self.flagged = not self.flagged

    def getNumAround(self):
        return self.numAround

    def click(self):
        self.clicked = True

    def getNeighbors(self):
        return self.neighbors
