
# Starting the app
from core.controller import Controller

print('Go to tiles!')

c = Controller()
c.set_corner(66.6, 25.5)
c.set_corner(66.3, 25.9)
c.download_tiles()
