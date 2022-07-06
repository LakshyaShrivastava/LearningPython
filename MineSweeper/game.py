import pygame
import os


class Game:
    def __init__(self, board, screenSize):
        self.images = None
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.images = {}
        self.loadImages()


    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    isRightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, isRightClick)
                self.draw()
                pygame.display.flip()
                if (self.board.getWon()):
                    running = False

        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in range (self.board.getSize()[0]):
            for col in range (self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def loadImages(self):
        for fileName in os.listdir("data"):
            if not fileName.endswith(".png"):
                continue
            image = pygame.image.load(r"data/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        string = ""
        if piece.getClicked():
            string = "bomb-at-clicked" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block"
        return self.images[string]

    def handleClick(self, position, isRightClick):
        """
         Start the click handeling process. This is implemented (y, x) or  (row, col)
        :param position: where the click happened
        :param isRightClick: whether or not the click was a right click
        :return: None
        """
        if self.board.getLost():
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, isRightClick)
