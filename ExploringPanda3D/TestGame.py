from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import WindowProperties
from panda3d.core import AmbientLight
from panda3d.core import Vec3, Vec4
from panda3d.core import DirectionalLight
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerPusher
from panda3d.core import CollisionNode, CollisionSphere, CollisionTube
from GameObject import *

import random

DEBUGGING = False


class Game(ShowBase):
    def __init__(self):
        super().__init__(self)

        self.disableMouse()

        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        self.environment = loader.loadModel("PandaSampleModels-master/Environment/environment")
        self.environment.reparentTo(self.render)

        self.camera.setPos(0, 0, 34)
        self.camera.setP(-90)

        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(self.ambientLightNodePath)

        mainLight = DirectionalLight("main light")
        self.mainLightNodePath = self.render.attachNewNode(mainLight)
        self.mainLightNodePath.setHpr(45, -45, 0)
        self.render.setLight(self.mainLightNodePath)
        self.render.setShaderAuto()

        self.keyMap = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "shoot": False
        }

        self.accept("w", self.updateKeyMap, ["up", True])
        self.accept("w-up", self.updateKeyMap, ["up", False])
        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])
        self.accept("mouse1", self.updateKeyMap, ["shoot", True])
        self.accept("mouse1-up", self.updateKeyMap, ["shoot", False])

        self.updateTask = taskMgr.add(self.update, "update")

        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()
        self.pusher.setHorizontal(True)

        wallSolid = CollisionTube(-8, 0, 0, 8, 0, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = self.render.attachNewNode(wallNode)
        wall.setY(8.0)
        if DEBUGGING:
            wall.show()

        wallSolid = CollisionTube(-8, 0, 0, 8, 0, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = self.render.attachNewNode(wallNode)
        wall.setY(-8.0)
        if DEBUGGING:
            wall.show()

        wallSolid = CollisionTube(0, -8, 0, 0, 8, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = self.render.attachNewNode(wallNode)
        wall.setX(8.0)
        if DEBUGGING:
            wall.show()

        wallSolid = CollisionTube(0, -8, 0, 0, 8, 0, 0.2)
        wallNode = CollisionNode("wall")
        wallNode.addSolid(wallSolid)
        wall = self.render.attachNewNode(wallNode)
        wall.setX(-8.0)
        if DEBUGGING:
            wall.show()

        self.player = None
        self.enemies = []
        self.trapEnemies = []
        self.deadEnemies = []

        self.spawnPoints = []
        numPointsPerWall = 5
        for i in range(numPointsPerWall):
            coord = 7.0/numPointsPerWall+0.5
            self.spawnPoints.append(Vec3(-7.0, coord, 0))
            self.spawnPoints.append(Vec3(7.0, coord, 0))
            self.spawnPoints.append(Vec3(coord, -7.0, 0))
            self.spawnPoints.append(Vec3(coord, 7.0, 0))

        self.initialSpawnInterval = 1.0
        self.minimumSpawnInterval = 0.2
        self.spawnInterval = self.initialSpawnInterval
        self.maxEnemies = 2
        self.maximumMaxEnemies = 20

        self.numTrapsPerSide = 2

        self.difficultyInterval = 5.0
        self.difficultyTimer = self.difficultyInterval

        self.startGame()

        # self.tempEnemy = WalkingEnemy(Vec3(5, 0, 0))

        # self.tempTrap = TrapEnemy(Vec3(-2, 7, 0))

        self.pusher.add_in_pattern("%fn-into-%in")

        self.accept("trapEnemy-into-wall", self.stopTrap)
        self.accept("trapEnemy-into_trapEnemy", self.stopTrap)
        self.accept("trapEnemy-into-player", self.trapHitsSomething)
        self.accept("trapEnemy-into-walkingEnemy", self.trapHitsSomething)

    def startGame(self):
        self.cleanup()
        self.player = Player()
        self.maxEnemies = 2
        self.spawnInterval = self.initialSpawnInterval
        self.difficultyTimer = self.difficultyInterval

        sideTrapSlots = [
            [],
            [],
            [],
            []
        ]

        trapSlotDistance = 0.4
        slotPos = -8 + trapSlotDistance
        while slotPos < 8:
            if abs(slotPos) > 1.0:
                sideTrapSlots[0].append(slotPos)
                sideTrapSlots[1].append(slotPos)
                sideTrapSlots[2].append(slotPos)
                sideTrapSlots[3].append(slotPos)
            slotPos += trapSlotDistance

        for i in range(self.numTrapsPerSide):
            slot = sideTrapSlots[0].pop(random.randint(0, len(sideTrapSlots[0])-1))
            trap = TrapEnemy(Vec3(slot, 7.0, 0))


    def updateKeyMap(self, controlName, controlState):
        self.keyMap[controlName] = controlState
        if DEBUGGING:
            print(controlName, "set to", controlState)

    def update(self, task):

        # Get the amount of time since the last update
        dt = globalClock.getDt()

        self.player.update(self.keyMap, dt)

        # self.tempEnemy.update(self.player, dt)
        # self.tempTrap.update(self.player, dt)

        return task.cont

    def stopTrap(self, entry):
        collider = entry.getFromNodePath()
        if collider.hasPythonTag("owner"):
            trap = collider.getPythonTag("owner")
            trap.moveDirection = 0
            trap.ignorePlayer = False

    def trapHitsSomething(self, entry):
        collider = entry.getFromNodePath()
        if collider.hasPythonTag("owner"):
            trap = collider.getPythonTag("owner")

            if trap.moveDirection == 0:
                return

            collider = entry.getIntoNodePath()
            if collider.hasPythonTag("owner"):
                obj = collider.getPythonTag("owner")
                if isinstance(obj, Player):
                    if not trap.ignorePlayer:
                        obj.alterHealth(-1)
                        trap.ignorePlayer = True
                else:
                    obj.alterHealth(-10)


game = Game()
game.run()
