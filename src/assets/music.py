import pygame

def load_music(f_path, volume):
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(f_path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
    except FileNotFoundError:
        raise FileNotFoundError("The File cannot be found in the 'resources/music' folder!")