import sys

import pygame

def check_events(ship):
  '''respond to keypress and mouse events'''
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        ship.moving_right= True
    
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        ship.moving_right= False
      
def update_screen(ai_settings, screen, ship):
  '''update images on the screen and flip to to the new screen.'''
  #screen.fill(bg_color)
  screen.fill(ai_settings.bg_color)
  ship.blitme()
  
  # make the most recently drawn screen visible
  pygame.display.flip()
