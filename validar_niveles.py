"""Herramienta de desarrollo: revisa los datos de todos los niveles.

Detecta errores típicos al copiar niveles: campos que faltan, objetos
fuera del nivel, balones o portería dentro de plataformas, enemigos mal
colocados, etc. No necesita ventana.

Uso:  python validar_niveles.py
"""

import pygame

import config
from levels import LEVELS
from models.level import Level

CAMPOS = ["name", "difficulty", "hint", "width", "start", "balls", "goal",
          "platforms", "spikes", "floor_spikes", "enemies", "hearts",
          "moving_platforms", "time_limit"]


def revisar(data):
    problemas = []

    for campo in CAMPOS:
        if campo not in data:
            problemas.append(f"falta el campo '{campo}'")
    if problemas:
        return problemas

    if data["difficulty"] not in config.ENEMY_SPEED:
        problemas.append(f"dificultad desconocida: {data['difficulty']}")
        return problemas

    ancho = data["width"]
    if ancho < config.WIDTH:
        problemas.append(f"el ancho ({ancho}) es menor que la pantalla ({config.WIDTH})")

    try:
        nivel = Level(data)
    except Exception as error:
        return [f"no se pudo construir el nivel: {error!r}"]

    def dentro(rect):
        return rect.left >= 0 and rect.right <= ancho and rect.top >= 0 and rect.bottom <= config.HEIGHT

    def choca_plataforma(rect):
        return any(rect.colliderect(s) for s in nivel.solids)

    for i, ball in enumerate(nivel.balls, 1):
        if not dentro(ball.rect):
            problemas.append(f"balón {i} fuera del nivel {ball.rect.topleft}")
        if choca_plataforma(ball.rect):
            problemas.append(f"balón {i} dentro de una plataforma {ball.rect.topleft}")

    if not dentro(nivel.goal):
        problemas.append(f"la portería está fuera del nivel {nivel.goal.topleft}")
    if choca_plataforma(nivel.goal):
        problemas.append(f"la portería está dentro de una plataforma {nivel.goal.topleft}")

    for i, heart in enumerate(nivel.hearts, 1):
        if not dentro(heart.rect):
            problemas.append(f"corazón {i} fuera del nivel {heart.rect.topleft}")
        if choca_plataforma(heart.rect):
            problemas.append(f"corazón {i} dentro de una plataforma {heart.rect.topleft}")

    for i, platform in enumerate(nivel.platforms, 1):
        if not dentro(platform):
            problemas.append(f"plataforma {i} fuera del nivel {platform.topleft}")

    for i, enemy in enumerate(nivel.enemies, 1):
        if choca_plataforma(enemy.rect):
            problemas.append(f"enemigo {i} nace dentro de una plataforma {enemy.rect.topleft}")
        if enemy.right_limit - enemy.left_limit < enemy.rect.width:
            problemas.append(f"enemigo {i}: el tramo de patrulla es más corto que su cuerpo")
        if not (enemy.left_limit <= enemy.rect.left and enemy.rect.right <= enemy.right_limit):
            problemas.append(f"enemigo {i} nace fuera de su tramo de patrulla")
        if enemy.right_limit > ancho or enemy.left_limit < 0:
            problemas.append(f"enemigo {i}: patrulla fuera del nivel")

    for i, moving in enumerate(nivel.moving_platforms, 1):
        r = moving.rect
        if moving.axis not in ("x", "y"):
            problemas.append(f"plataforma móvil {i}: eje inválido '{moving.axis}'")
            continue
        largo = r.width if moving.axis == "x" else r.height
        if moving.end_limit - moving.start_limit <= largo:
            problemas.append(f"plataforma móvil {i}: el recorrido no es mayor que su tamaño")
        if moving.axis == "x" and not (moving.start_limit <= r.left and r.right <= moving.end_limit):
            problemas.append(f"plataforma móvil {i} nace fuera de su recorrido")
        if moving.axis == "y" and not (moving.start_limit <= r.top and r.bottom <= moving.end_limit):
            problemas.append(f"plataforma móvil {i} nace fuera de su recorrido")

    jugador = pygame.Rect(*nivel.start, *config.PLAYER_SIZE)
    if not dentro(jugador):
        problemas.append(f"la salida del jugador está fuera del nivel {nivel.start}")
    if choca_plataforma(jugador):
        problemas.append(f"el jugador nace dentro de una plataforma {nivel.start}")
    if nivel.touches_spikes(jugador):
        problemas.append(f"el jugador nace sobre pinchos {nivel.start}")

    for x_from, x_to in data["floor_spikes"]:
        if x_from >= x_to or x_from < 0 or x_to > ancho:
            problemas.append(f"tramo de pinchos inválido ({x_from}, {x_to})")

    if not nivel.balls:
        problemas.append("el nivel no tiene ningún balón")

    return problemas


def main():
    total = 0
    for numero, data in enumerate(LEVELS, 1):
        problemas = revisar(data)
        nombre = data.get("name", "?") if isinstance(data, dict) else "?"
        if problemas:
            total += len(problemas)
            print(f"[REVISAR] Nivel {numero}: {nombre}")
            for problema in problemas:
                print("          -", problema)
        else:
            print(f"[OK]      Nivel {numero}: {nombre}")
    print("\nTodos los niveles son válidos." if total == 0
          else f"\n{total} problema(s) encontrado(s).")


if __name__ == "__main__":
    main()