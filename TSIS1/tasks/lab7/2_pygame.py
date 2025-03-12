
import pygame

RESOLUTION = (400, 200)
TICK = 60
DELTA = 1.0 / TICK
SONG_END = pygame.USEREVENT + 1

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
done = False
clock = pygame.time.Clock()   

font = pygame.font.SysFont("comicsansms", 68)
text = font.render("Music Player", True, (0, 128, 0))

_currently_playing_song = None
_songs = ['1.mp3', '2.mp3', '3.mp3']
import random

def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] 
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def play_previous_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

play_a_different_song()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == SONG_END:
                    play_next_song()
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pygame.mixer.music.play()
                        break
                    if event.key == pygame.K_DOWN:
                        pygame.mixer.music.stop()
                    if event.key == pygame.K_RIGHT:
                        play_next_song()
                    if event.key == pygame.K_LEFT:
                        play_previous_song()
            
                
        
        screen.fill((255, 255, 255))
        screen.blit(text,
        (0, text.get_height() // 2))
        
        pygame.display.flip()
        clock.tick(TICK)