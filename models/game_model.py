"""Estado global de la partida: vidas, puntuación, nivel y reglas del juego.

Es el corazón del Model. No dibuja, no suena y no lee el teclado:
recibe órdenes simples (dirección, salto) y deja avisos en una lista
de eventos que el Controller lee después.
"""

from enum import Enum, auto

import config
from levels import LEVELS
from models import events
from models.level import Level
from models.player import Player


class State(Enum):
    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    LEVEL_COMPLETE = auto()
    GAME_OVER = auto()
    VICTORY = auto()


class GameModel:
    def __init__(self):
        self.state = State.MENU
        self.lives = config.INITIAL_LIVES
        self.score = 0
        self.level_index = 0
        self.score_at_level_start = 0
        self.lives_at_level_start = config.INITIAL_LIVES
        self.level_points = self._empty_points()
        self.level_frames = 0
        self.player = Player(*config.PLAYER_START)
        self.level = None
        self._events = []
        self.load_level(0)
        self.state = State.MENU      # load_level deja el estado en PLAYING

    # ----- Propiedades de consulta (la View las lee) -----
    @property
    def level_number(self):
        """Número de nivel para mostrar al jugador (empieza en 1)."""
        return self.level_index + 1

    @property
    def total_levels(self):
        return len(LEVELS)

    @property
    def is_last_level(self):
        return self.level_index == len(LEVELS) - 1

    @property
    def time_left(self):
        """Segundos que quedan, o None si el nivel no tiene límite."""
        limit = self.level.time_limit
        if limit is None:
            return None
        return max(0.0, limit - self.level_frames / config.FPS)

    @property
    def level_total(self):
        """Puntos ganados en el nivel actual (suma del desglose)."""
        return sum(self.level_points.values())

    # ----- Eventos -----
    def pop_events(self):
        """Devuelve los eventos pendientes y vacía la lista."""
        pending = self._events
        self._events = []
        return pending

    def _emit(self, event):
        self._events.append(event)

    # ----- Puntuación -----
    @staticmethod
    def _empty_points():
        return {"balls": 0, "enemies": 0, "goal": 0, "lives": 0, "time": 0}

    def _add_points(self, kind, amount):
        """Suma puntos al total y al desglose del nivel."""
        self.score += amount
        self.level_points[kind] += amount

    # ----- Carga y reinicio -----
    def start_game(self):
        """Nueva partida desde el nivel 1."""
        self.lives = config.INITIAL_LIVES
        self.score = 0
        self.load_level(0)

    def load_level(self, index):
        self.level_index = index
        self.level = Level(LEVELS[index])
        self.player.reset(*self.level.start)
        self.score_at_level_start = self.score
        self.lives_at_level_start = self.lives
        self.level_points = self._empty_points()
        self.level_frames = 0
        self.state = State.PLAYING

    def _reload_level(self):
        """Reconstruye el nivel actual con la puntuación del inicio."""
        self.score = self.score_at_level_start
        self.load_level(self.level_index)

    def restart_level(self):
        """Reinicia el nivel sin perder vida (tecla R o pausa).
        Vidas y puntuación vuelven a los valores con que empezó el nivel,
        así que no se pueden ganar corazones reiniciando una y otra vez."""
        self.lives = self.lives_at_level_start
        self._reload_level()

    def retry_level(self):
        """Tras un Game Over: mismo nivel, vidas completas."""
        self.lives = config.INITIAL_LIVES
        self._reload_level()

    def pause(self):
        """Pausa la partida (solo si se está jugando)."""
        if self.state == State.PLAYING:
            self.state = State.PAUSED

    def resume(self):
        """Reanuda la partida pausada."""
        if self.state == State.PAUSED:
            self.state = State.PLAYING

    def go_to_menu(self):
        """Vuelve al menú principal. La partida se descarta."""
        self.state = State.MENU

    def next_level(self):
        """Pasa al siguiente nivel o, si era el último, a la victoria."""
        if self.is_last_level:
            self.state = State.VICTORY
            self._emit(events.VICTORY)
        else:
            self.load_level(self.level_index + 1)

    # ----- Actualización por frame -----
    def update(self, direction, want_jump):
        """Un frame de juego. Solo actúa si el estado es PLAYING."""
        if self.state != State.PLAYING:
            return

        level = self.level
        player = self.player
        self.level_frames += 1

        level.update_platforms(player)
        self._events.extend(
            player.update(direction, want_jump, level.solids, level.width)
        )
        level.update_enemies()

        for _ in range(level.collect_balls(player.rect)):
            self._add_points("balls", config.SCORE_BALL)
            self._emit(events.BALL_PICKED)
        level.carry_balls(player.rect)

        for heart in level.touching_hearts(player.rect):
            if self.lives < config.MAX_LIVES:
                heart.taken = True
                self.lives += 1
                self._emit(events.HEART_PICKED)

        if level.touches_spikes(player.rect):
            self._lose_life()
            return

        for enemy in level.enemies:
            if enemy.alive and player.rect.colliderect(enemy.rect):
                if enemy.is_stomped_by(player):
                    enemy.alive = False
                    player.bounce()
                    self._add_points("enemies", config.SCORE_ENEMY)
                    self._emit(events.ENEMY_DEFEATED)
                else:
                    self._lose_life()
                    return

        if level.reached_goal(player.rect):
            self._complete_level()
            return

        if self.time_left is not None and self.time_left <= 0:
            self._emit(events.TIME_UP)
            self._lose_life()

    # ----- Reglas -----
    def _lose_life(self):
        self.lives -= 1
        self._emit(events.HURT)
        if self.lives <= 0:
            self.state = State.GAME_OVER
            self._emit(events.GAME_OVER)
        else:
            self._reload_level()

    def _complete_level(self):
        self._add_points("goal", config.SCORE_GOAL)
        self._add_points("lives", self.lives * config.SCORE_PER_LIFE)
        if self.time_left is not None:
            self._add_points("time", int(self.time_left) * config.SCORE_PER_SECOND)
        self.state = State.LEVEL_COMPLETE
        self._emit(events.GOAL)