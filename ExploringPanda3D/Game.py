from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties


class Game(ShowBase):
    def __init__(self):
        super().__init__(self)

        self.disableMouse()

        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        self.environment = loader.loadModel("models/environment")
        self.environment.reparentTo(self.render)

        self.camera.setPos(0, 0, 200)
        self.camera.setP(-90)


game = Game()
game.run()
