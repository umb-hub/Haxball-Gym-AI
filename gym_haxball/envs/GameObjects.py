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
            self.vertexes = None
            self.segments = None
            self.goals = None
            self.discs = None
            self.planes = None
            self.joints = None
            self.redSpawnPoints = []
            self.blueSpawnPoints = []
            self.playerPhysics = None
            self.ballPhysics = None

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
    def __init__(self, pos=Vector(), bCoef=1, cMask=[], cGroup=[]) -> None:
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
    def __init__(self, pos=Vector(), speed=Vector(), gravity=Vector(), radius=10, invMass=1, damping=0.99, color=0xFFFFFF, bCoef=0.5, cMask = [], cGroup = []) -> None:
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
    def __init__(self, gravity=Vector(), radius=15, invMass=0.5, bCoef=0.5, damping=0.96, cMask=[], cGroup=[], acceleration=0.1, kickingAcceleration=0.07, kickingDamping=0.96, kickStrength=5, kickback=0) -> None:
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
    def __init__(self, gravity=Vector(), radius=10, invMass=1, bCoef=0.5, damping=0.99, cMask=["all"], cGroup=["ball"], color=0xFFFFFF) -> None:
        self.gravity = gravity
        self.radius = radius
        self.invMass = invMass
        self.bCoef = bCoef
        self.damping = damping
        self.cMask = cMask
        self.cGroup = cGroup
        self.color = color