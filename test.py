import pygame
pygame.init()

# Setup layar
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Pixel Perfect Collision Demo")

# Load gambar dan ubah ke surface dengan alpha (transparansi)
player_img = pygame.image.load("imgs/green-car.png").convert_alpha()
enemy_img = pygame.image.load("imgs/track-border.png").convert_alpha()

# Buat rect untuk posisi gambar
player_rect = player_img.get_rect(topleft=(100, 200))
enemy_rect = enemy_img.get_rect(topleft=(350, 200))

# Buat mask (peta piksel) dari gambar
player_mask = pygame.mask.from_surface(player_img)
enemy_mask = pygame.mask.from_surface(enemy_img)

# Warna background
BG_COLOR = (30, 30, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrol gerakan player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_rect.x += 3
    if keys[pygame.K_LEFT]:
        player_rect.x -= 3
    if keys[pygame.K_UP]:
        player_rect.y -= 3
    if keys[pygame.K_DOWN]:
        player_rect.y += 3

    # Hitung jarak posisi (offset) antara dua gambar
    offset = (enemy_rect.x - player_rect.x, enemy_rect.y - player_rect.y)

    # Cek apakah piksel antar dua gambar bersentuhan
    collision_point = player_mask.overlap(enemy_mask, offset)

    # Gambar ke layar
    screen.fill(BG_COLOR)
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)

    # Kalau tabrakan, tampilkan indikator
    if collision_point:
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (player_rect.x + collision_point[0], player_rect.y + collision_point[1]),
            5
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
