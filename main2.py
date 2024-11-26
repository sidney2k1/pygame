import pygame
pygame.init()
white=(255,255,255)
clock=pygame.time.Clock()
displaysurface=pygame.display.set_mode((500,500))
pygame.display.set_caption("Image")
image=pygame.image.load("download (3).jpeg")
defaultsizeimage=(500,500)
image=pygame.transform.scale(image,defaultsizeimage)
defaultimageposition=(1,1)
while True:
    displaysurface.fill(white)
    displaysurface.blit(image,defaultimageposition)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
    clock.tick(30)