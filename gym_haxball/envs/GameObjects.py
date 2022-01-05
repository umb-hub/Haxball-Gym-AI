class Vector:
    """
    Define vector in game space
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return '(x=%s, y=%s)' % (self.x, self.y)

    def __copy__(self):
        return Vector(self.x, self.y)

    def __eq__(self, other: 'Vector'):
        return self.x == other.x and self.y == other.y

class StadiumObject:
    """
    StadiumObjects are the root object of a game stadium

    See reference to https://github.com/haxball/haxball-issues/wiki/Stadium-(.hbs)-File
    """
    def __init__(self, stadium) -> None:
        """Default stadium"""
        if stadium == "classic":
            self.name = "Classic"
            self.cameraWidth = 420
            self.cameraHeight = 240
            self.maxViewWidth = 0 #0 for disable feature
            self.cameraFollow = "ball"
            self.spawnDistance = 170
            self.canBeStored = True
            self.kickOffReset = "partial"
            self.bg = BackgroundObject("classic")
            self.traits = None
            self.vertexes = [
                            Vertex(Vector(-370,170),cMask=["ball"]),
                            Vertex(Vector(-370,64),cMask=["ball"]),
                            Vertex(Vector(-370,-64),cMask=["ball"]),
                            Vertex(Vector(-370,-170),cMask=["ball"]),

                            Vertex(Vector(370,170),cMask=["ball"]),
                            Vertex(Vector(370,64),cMask=["ball"]),
                            Vertex(Vector(370,-64),cMask=["ball"]),
                            Vertex(Vector(370,-170),cMask=["ball"]),

                            Vertex(Vector(0,200), 0.1, ["red", "blue"], ["redKO", "blueKO"]),
                            Vertex(Vector(0,75), 0.1, ["red", "blue"], ["redKO", "blueKO"]),
                            Vertex(Vector(0,-75), 0.1, ["red", "blue"], ["redKO", "blueKO"]),
                            Vertex(Vector(0,-200), 0.1, ["red", "blue"], ["redKO", "blueKO"]),

                            Vertex(Vector(-380, -64), 0.1, cMask=["ball"]),
                            Vertex(Vector(-400, -44), 0.1, cMask=["ball"]),
                            Vertex(Vector(-400,  44), 0.1, cMask=["ball"]),
                            Vertex(Vector(-380,  64), 0.1, cMask=["ball"]),

                            Vertex(Vector(380, -64), 0.1, cMask=["ball"]),
                            Vertex(Vector(400, -44), 0.1, cMask=["ball"]),
                            Vertex(Vector(400,  44), 0.1, cMask=["ball"]),
                            Vertex(Vector(380,  64), 0.1, cMask=["ball"]),
                            ]
            self.segments = [
                            Segment(self.vertexes[0], self.vertexes[1], bCoef=1, vis=False, cMask=["ball"]),
                            Segment(self.vertexes[2], self.vertexes[3], bCoef=1, vis=False, cMask=["ball"]),
                            Segment(self.vertexes[4], self.vertexes[5], bCoef=1, vis=False, cMask=["ball"]),
                            Segment(self.vertexes[6], self.vertexes[7], bCoef=1, vis=False, cMask=["ball"]),

                            Segment(self.vertexes[12], self.vertexes[13], bCoef=0.1, vis=True, cMask=["ball"], curve=-90),
                            Segment(self.vertexes[13], self.vertexes[14], bCoef=0.1, vis=True, cMask=["ball"]),
                            Segment(self.vertexes[14], self.vertexes[15], bCoef=0.1, vis=True, cMask=["ball"], curve=-90),

                            Segment(self.vertexes[16], self.vertexes[17], bCoef=0.1, vis=True, cMask=["ball"], curve=90),
                            Segment(self.vertexes[17], self.vertexes[18], bCoef=0.1, vis=True, cMask=["ball"]),
                            Segment(self.vertexes[18], self.vertexes[19], bCoef=0.1, vis=True, cMask=["ball"], curve=90),

                            Segment(self.vertexes[8],  self.vertexes[9],  bCoef=1, vis=False, cMask=["red", "blue"], cGroup=["redKO", "blueKO"]),
                            Segment(self.vertexes[9],  self.vertexes[10], bCoef=1, vis=False, cMask=["red", "blue"], cGroup=["redKO", "blueKO"]),
                            Segment(self.vertexes[9],  self.vertexes[10], bCoef=1, vis=False, cMask=["red", "blue"], cGroup=["redKO", "blueKO"]),
                            Segment(self.vertexes[10], self.vertexes[11], bCoef=1, vis=False, cMask=["red", "blue"], cGroup=["redKO", "blueKO"]),
                            ]
            self.goals = [
                        Goal(Vector(-370,64), Vector(-370,-64), "red"),
                        Goal(Vector(370,64), Vector(370,-64), "blue"),
                        ]
            self.discs = [
                        Disc(Vector(-370,64), radius=8, invMass=0, color=0xFFCCCC),
                        Disc(Vector(-370,-64), radius=8, invMass=0, color=0xFFCCCC),

                        Disc(Vector(370,64), radius=8, invMass=0, color=0xCCCCFF),
                        Disc(Vector(370,-64), radius=8, invMass=0, color=0xCCCCFF),
                        ]
            self.planes = [
                            Plane(Vector(0, 1), -170, cMask=["ball"]),
                            Plane(Vector(0, -1), -170, cMask=["ball"]),

                            Plane(Vector(0, 1), -200, 0.1),
                            Plane(Vector(0, -1), -200, 0.1),

                            Plane(Vector(1, 0), -420, 0.1),
                            Plane(Vector(-1, 0), -420, 0.1),

                            ]
            self.joints = None
            self.redSpawnPoints = []
            self.blueSpawnPoints = []
            self.playerPhysics = PlayerPhysics()
            self.ballPhysics = BallPhysics()

class BackgroundObject:
    """
    BackgroundObject define background pattern of game stadium
    """
    def __init__(self, stadium) -> None:
        if stadium == "classic":
            self.type = "grass"
            self.width = 370
            self.height = 170
            self.kickOffRadius =  75
            self.cornerRadius = 0
            self.goalLine = 0
            self.color = 0x718C5A

class Vertex:
    """
    A vertex is a point which can collide with discs but cannot move and is not visible.
    """
    def __init__(self, pos=Vector(0, 0), bCoef=1, cMask=[], cGroup=[]) -> None:
        self.pos = pos
        self.bCoef = bCoef
        self.cMask = cMask
        self.cGroup = cMask

class Segment:
    """
    A segment is a line (curved or straight) that connects two vertexes. Discs can collide with segments and they can also be used as decoration.
    """
    def __init__(self, v1, v2, bCoef=1, curve=0, bias=0, cMask=[], cGroup=[], vis=True, color=0x0) -> None:
        self.v1 = v1
        self.v2 = v2
        self.bCoef = bCoef
        self.curve = curve
        self.bias = bias
        self.cMask = cMask
        self.cGroup = cMask
        self.vis = vis
        self.color = color

class Plane:
    """
    A segment is a line (curved or straight) that connects two vertexes. Discs can collide with segments and they can also be used as decoration.
    """
    def __init__(self, normal, dist, bCoef=1, cMask=[], cGroup=[]) -> None:
        self.normal = normal
        self.dist = dist
        self.bCoef = bCoef
        self.cMask = cMask
        self.cGroup = cMask
   

class Goal:
    """
    Goals are lines belonging to a team, when the ball crosses this line the opossite team scores a goal.
    """
    def __init__(self, p1, p2, team) -> None:
        self.p1 = p1
        self.p2 = p2
        self.team = team

class Disc:
    """
    Discs are circular physical objects that are placed in the stadium, they can move and collide with other discs.
    """
    def __init__(self, pos=Vector(0, 0), speed=Vector(0, 0), gravity=Vector(0, 0), radius=10, invMass=1, damping=0.99, color=0xFFFFFF, bCoef=0.5, cMask = [], cGroup = []) -> None:
        self.pos = pos
        self.speed = speed
        self.gravity = gravity
        self.radius = radius
        self.invMass = invMass
        self.damping = damping
        self.color = color
        self.bCoef = bCoef
        self.cMask = cMask
        self.cGroup = cGroup

class PlayerPhysics:
    """
    PlayerPhysics describes physical constants affecting the players.
    """
    def __init__(self, gravity=Vector(0, 0), radius=15, invMass=0.5, bCoef=0.5, damping=0.96, cMask=[], cGroup=[], acceleration=0.1, kickingAcceleration=0.07, kickingDamping=0.96, kickStrength=5, kickback=0) -> None:
        self.gravity = gravity
        self.radius = radius
        self.invMass = invMass
        self.bCoef = bCoef
        self.damping = damping
        self.cMask = cMask
        self.cGroup = cGroup
        self.acceleration = acceleration
        self.kickingAcceleration = kickingAcceleration
        self.kickingDamping = kickingDamping
        self.kickStrength = kickStrength
        self.kickback = kickback

class BallPhysics:
    """
    BallPhysics describes physical constants affecting the ball.
    """
    def __init__(self, gravity=Vector(0, 0), radius=10, invMass=1, bCoef=0.5, damping=0.99, cMask=["all"], cGroup=["ball"], color=0xFFFFFF) -> None:
        self.gravity = gravity
        self.radius = radius
        self.invMass = invMass
        self.bCoef = bCoef
        self.damping = damping
        self.cMask = cMask
        self.cGroup = cGroup
        self.color = color