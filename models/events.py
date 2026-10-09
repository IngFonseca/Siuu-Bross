"""Eventos que el Model emite y que el Controller traduce en sonidos
o cambios de pantalla.

El Model nunca reproduce sonidos ni dibuja: solo avisa de lo que pasó.
"""

# Eventos durante la partida
BALL_PICKED = "ball_picked"          # el jugador recogió un balón
HEART_PICKED = "heart_picked"        # el jugador recogió un corazón
ENEMY_DEFEATED = "enemy_defeated"    # el jugador pisó a un enemigo
HURT = "hurt"                        # el jugador perdió una vida
JUMP = "jump"                        # el jugador saltó (no hay sonido para él)

# Eventos de fin de nivel y de juego
GOAL = "goal"                        # llegó a la portería con los balones necesarios
TIME_UP = "time_up"                  # se acabó el tiempo del nivel
GAME_OVER = "game_over"              # se acabaron las vidas
VICTORY = "victory"                  # completó el último nivel