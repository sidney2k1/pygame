import pygame
pygame.init()
grey=(170,170,170)
clock=pygame.time.Clock()
displaysurface=pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game display")
image=pygame.image.load("download.jpeg")
defaultsizeimage=(200,200)
image=pygame.transform.scale(image,defaultsizeimage)
defaultposition=(1,1)
image2=pygame.image.load("download (3).jpeg")
defaultsizeimage2=(200,300)
image2=pygame.transform.scale(image2,defaultsizeimage2)
defaultposition2=(1,200)

while True:
    displaysurface.fill(grey)
    displaysurface.blit(image,defaultposition)
    displaysurface.blit(image2,defaultposition2)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
    clock.tick(30)

            