import sys
import pygame
import pygame.camera
from pygame.locals import *
from PIL import Image


pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()

print(camlist)

# images = map(Image.open, ['Test1.jpg', 'Test2.jpg', 'Test3.jpg'])
# widths, heights = zip(*(i.size for i in images))

# total_width = sum(widths)
# max_height = max(heights)

# new_im = Image.new('RGB', (total_width, max_height))

# x_offset = 0
# for im in images:
#   new_im.paste(im, (x_offset,0))
#   x_offset += im.size[0]

# new_im.save('test.jpg')