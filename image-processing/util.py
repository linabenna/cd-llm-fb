class Color:
    def __init__(self, hsv):
        self.hsv = [[hsv]]

# Yellow
y1 = Color((20, 100, 100))
y2 = Color((30, 255, 255))

# Blue
b1 = Color((100, 150, 0))
b2 = Color((140, 255, 255))

# Brown
br1 = Color((10, 100, 20))
br2 = Color((20, 255, 200))

# Purple
p1 = Color((130, 50, 50))
p2 = Color((160, 255, 255))

# Grey
g1 = Color((0, 0, 50))
g2 = Color((180, 50, 200))

# Green
gr1 = Color((40, 40, 40))
gr2 = Color((80, 255, 255))

# Red – note: split in two HSV ranges due to wraparound
r1l = Color((0, 120, 70))
r2l = Color((10, 255, 255))
r1h = Color((170, 120, 70))
r2h = Color((180, 255, 255))

# Optional Gold
# gl1 = Color((22, 180, 130))
# gl2 = Color((30, 255, 255))
