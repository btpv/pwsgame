import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Home Screen")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
LIGHT_BLUE = (100, 180, 240)
GRAY = (200, 200, 200)

# Fonts
TITLE_FONT = pygame.font.SysFont("Arial", 48)
BUTTON_FONT = pygame.font.SysFont("Arial", 32)

# Button class
class Button:
    def __init__(self, text, x, y, w, h, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.callback = callback
        self.hovered = False

    def draw(self, surface):
        color = LIGHT_BLUE if self.hovered else BLUE
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=8)
        text_surf = BUTTON_FONT.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

# Button callbacks
def start_game():
    # Start game.py in a new process
    subprocess.Popen([sys.executable, "Untitled-1.py"])
    pygame.QUIT()

def show_credits():
    print("Credits button pressed.")

def show_settings():
    print("Settings button pressed.")

# Button positions and sizes
button_width = 220
button_height = 60
button_spacing = 30
start_y = HEIGHT // 2 - (button_height * 3 + button_spacing * 2) // 2
buttons = [
    Button("Start Game", WIDTH//2 - button_width//2, start_y, button_width, button_height, start_game),
    Button("Credits", WIDTH//2 - button_width//2, start_y + button_height + button_spacing, button_width, button_height, show_credits),
    Button("Settings", WIDTH//2 - button_width//2, start_y + 2*(button_height + button_spacing), button_width, button_height, show_settings)
]

def draw_screen():
    SCREEN.fill(WHITE)
    # Draw title
    title_surf = TITLE_FONT.render("Welcome to the Game", True, BLACK)
    title_rect = title_surf.get_rect(center=(WIDTH//2, HEIGHT//4))
    SCREEN.blit(title_surf, title_rect)
    # Draw buttons
    for btn in buttons:
        btn.draw(SCREEN)
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for btn in buttons:
                btn.handle_event(event)
        draw_screen()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()