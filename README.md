# Siuu.Bross

Videojuego de plataformas en Python con pygame: lleva el balón hasta la portería, esquiva pinchos y enemigos, y supera 10 niveles de dificultad creciente.

## Descripción

Siuu.Bross es un juego de plataformas 2D en el que controlas a CR7 por escenarios cada vez más difíciles. En cada nivel debes recoger el balón (o los balones) y llevarlo a la portería sin caer sobre los pinchos ni chocar de lado con los enemigos. Puedes derrotar a los enemigos saltando sobre ellos.

El proyecto está construido siguiendo el patrón **MVC (Modelo - Vista - Controlador)**, lo que separa claramente las reglas del juego, el dibujo y el sonido, y la lectura de la entrada del jugador. Esto facilita su mantenimiento y la incorporación de nuevos niveles y mecánicas.

## Características

- 10 niveles con dificultad progresiva: 3 fáciles, 4 medios y 3 difíciles
- Mecánicas que se introducen poco a poco: enemigos patrulleros, plataformas móviles, ascensores, corazones, varios balones por nivel y límite de tiempo
- Cámara horizontal que sigue al jugador en los niveles largos
- Puntuación con desglose por nivel (balones, enemigos, gol, vidas restantes y tiempo sobrante)
- Sistema de vidas con corazones recogibles (máximo 5)
- Menú principal, pausa, pantalla de nivel completado, Game Over y pantalla final
- Música de fondo y efectos de sonido
- Los niveles son datos puros (diccionarios), sin lógica, por lo que agregar uno nuevo no requiere tocar el código del juego
- Usa únicamente los recursos gráficos y de audio incluidos en el proyecto: el sprite de los enemigos se genera por código a partir del sprite del jugador
- El Model solo usa pygame para la geometría (`pygame.Rect`), por lo que su lógica puede probarse sin abrir una ventana
- Rutas de recursos independientes del directorio desde el que se ejecute

## Controles

| Acción | Teclas |
|---|---|
| Mover | Flechas `←` `→` o `A` / `D` |
| Saltar | `Espacio`, `↑` o `W` |
| Reiniciar el nivel (sin perder vida) | `R` |
| Pausa / continuar | `P` o `ESC` |
| Confirmar (menú, Game Over, final) | `ENTER` |
| Pasar de nivel | Cualquier tecla en la pantalla de nivel completado |
| Botones del menú | Clic izquierdo del ratón |

Para derrotar a un enemigo, cae sobre él desde arriba. Si lo tocas de lado, pierdes una vida.

## Reglas y puntuación

| Concepto | Efecto |
|---|---|
| Recoger un balón | +100 puntos |
| Derrotar a un enemigo | +200 puntos |
| Llegar a la portería con **todos** los balones | +500 puntos |
| Vidas restantes al completar el nivel | +100 por vida |
| Segundos sobrantes (niveles con tiempo) | +10 por segundo |
| Recoger un corazón | +1 vida (máximo 5) |
| Tocar pinchos, chocar con un enemigo o agotar el tiempo | −1 vida y reinicio del nivel |

Al reiniciar con `R` o desde la pausa, las vidas y la puntuación vuelven a las del inicio del nivel, por lo que no se pueden ganar vidas reiniciando repetidamente.

## Niveles

| Nivel | Nombre | Dificultad | Novedad principal |
|---|---|---|---|
| 1 | Calentamiento | Fácil | Movimiento básico y saltos |
| 2 | El primer rival | Fácil | Primer enemigo: pisarlo |
| 3 | Escalera al gol | Fácil | Plataformas, pinchos, enemigos y el primer corazón |
| 4 | El muro | Media | Muro, primera plataforma móvil y cámara |
| 5 | Foso de pinchos | Media | Suelo mortal y plataformas estrechas |
| 6 | El ascensor | Media | Plataformas móviles verticales y corazón escondido |
| 7 | Doble balón | Media | Dos balones: ida y vuelta |
| 8 | La trampa | Difícil | Aterrizajes precisos entre pinchos |
| 9 | Contrarreloj | Difícil | 3 balones y 60 segundos |
| 10 | La final | Difícil | 3 balones, 90 segundos y todo lo anterior |

Al completar el nivel 10 aparece la pantalla final.

## Tecnologías

- Lenguaje: Python 3
- Biblioteca de juego: pygame 2.6.1
- Gráficos y audio: imágenes PNG y sonidos MP3/WAV incluidos en `assets/`
- Persistencia: ninguna (no se guarda la puntuación)
- Empaquetado (opcional): PyInstaller

## Requisitos

- Python 3 (probado con 3.13.2)
- pip
- Pantalla y dispositivo de audio

## Descarga

Si solo quieres jugar, descarga el ejecutable desde la sección **Releases** (Windows, no requiere Python).

## Instalación

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd Siuu.Bross
```

2. (Recomendado) Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta el juego desde la raíz del proyecto:

```bash
python main.py
```

Ejemplo de partida:

```text
Menú principal  →  Jugar
Nivel 1: Calentamiento  →  recoge el balón y llega a la portería
¡GOOOOOOOOL!  →  desglose de puntos  →  cualquier tecla
Nivel 2: El primer rival  →  ...
P  →  Pausa (Continuar / Reiniciar nivel / Menú principal)
...
Nivel 10 completado  →  pantalla final
```

## Estructura del Proyecto

```text
Siuu.Bross/
├── main.py                      # Punto de entrada: crea y conecta las piezas
├── config.py                    # Constantes del juego, física, puntuación y rutas
├── requirements.txt
├── README.md
├── assets/                      # Recursos (solo se usan los existentes)
│   ├── images/                  # balon, corazon, cr7, fondo, porteria, terror (.png)
│   └── sounds/                  # musica_fondo, grito (.mp3) · sonido_balon, sonido_gol (.wav)
├── models/                      # MODELO
│   ├── __init__.py
│   ├── events.py                # Nombres de los eventos que el Modelo emite
│   ├── player.py                # Jugador: movimiento, salto y colisiones
│   ├── enemy.py                 # Enemigo patrullero
│   ├── moving_platform.py       # Plataforma móvil (horizontal o vertical)
│   ├── level.py                 # Construye un nivel a partir de sus datos
│   └── game_model.py            # Estado del juego: vidas, puntos, nivel y reglas
├── views/                       # VISTA
│   ├── __init__.py
│   ├── assets.py                # Carga de imágenes, fuentes y sonidos
│   ├── ui.py                    # Texto centrado y botones
│   ├── game_view.py             # Dibuja el mundo, el HUD y la cámara
│   ├── screens_view.py          # Menú, pausa, nivel completado, Game Over y final
│   └── audio_view.py            # Música y efectos de sonido
├── controllers/                 # CONTROLADOR
│   ├── __init__.py
│   ├── input_controller.py      # Lee teclado y ratón
│   └── game_controller.py       # Bucle principal y transiciones entre estados
└── levels/                      # Datos de los niveles (sin lógica)
    ├── __init__.py              # Lista ordenada de niveles
    └── level_01.py ... level_10.py
```

| Capa | Responsabilidad |
|---|---|
| Modelo | Contiene las reglas y los datos del juego. No dibuja, no reproduce sonidos y no lee el teclado. Solo usa pygame para `pygame.Rect`. |
| Vista | Dibuja el juego y reproduce los sonidos. Solo lee el Modelo; nunca lo modifica. |
| Controlador | Lee la entrada, decide qué hacer según el estado (menú, jugando, pausa...) y coordina Modelo y Vista. No dibuja ni calcula física. |

**Comunicación entre capas:** cuando ocurre algo importante (recoger un balón, marcar gol, perder una vida), el Modelo deja un aviso en una lista de eventos. El Controlador la lee y se la entrega a la Vista de audio, que decide qué sonido reproducir.

**Estados del juego:** `MENU`, `PLAYING`, `PAUSED`, `LEVEL_COMPLETE`, `GAME_OVER` y `VICTORY`.

## Cómo agregar un nivel nuevo

1. Crea `levels/level_11.py` con un diccionario `LEVEL` (copia uno existente como plantilla).
2. Impórtalo y añádelo, en orden, a la lista `LEVELS` de `levels/__init__.py`.
3. Juégalo desde el menú. La pantalla final (`terror.png` + grito) aparece tras el **último** nivel de la lista.

Formato de un nivel:

| Campo | Descripción |
|---|---|
| `name` | Nombre mostrado al empezar el nivel |
| `difficulty` | `"easy"`, `"medium"` o `"hard"` (define la velocidad de enemigos y plataformas móviles) |
| `hint` | Mensaje que se muestra los primeros 3 segundos |
| `width` | Ancho del nivel en píxeles (la pantalla mide 800) |
| `start` | Posición inicial del jugador `(x, y)` |
| `balls` | Lista de balones `(x, y)` |
| `goal` | Portería `(x, y)` |
| `platforms` | Plataformas fijas `(x, y, ancho, alto)` |
| `spikes` | Pinchos sueltos de 20×20 `(x, y)` |
| `floor_spikes` | Tramos de pinchos en el suelo `(x_inicio, x_fin)` |
| `enemies` | Lista de `{"x", "y", "patrol": (izq, der)}`; opcional `"speed"` |
| `hearts` | Corazones `(x, y)` |
| `moving_platforms` | Lista de `{"x", "y", "w", "h", "axis": "x" o "y", "range": (inicio, fin)}`; opcional `"speed"` |
| `time_limit` | Segundos disponibles, o `None` si no hay límite |

El suelo está en `y = 400`. El jugador mide 40×60 y su salto sube unos 84 px. Como referencia para que un salto sea posible, el hueco horizontal máximo entre plataformas depende de lo que se suba:

| Subida | Hueco máximo teórico |
|---|---|
| 0 px | ~147 px |
| 30 px | ~133 px |
| 50 px | ~121 px |
| 70 px | ~105 px |

Se recomienda quedarse alrededor del 80 % de esos valores. Si la plataforma de destino tiene pinchos en los extremos, recuerda que la zona segura es más corta de lo que parece.

## Cómo agregar una mecánica nueva

1. Agrega la lógica y los datos en `models/` (y un evento en `models/events.py` si debe sonar o avisar).
2. Agrega su dibujo en `views/game_view.py` y, si tiene sonido, asígnalo en `views/audio_view.py`.
3. Si requiere una acción del jugador, léela en `controllers/input_controller.py` y atiéndela en `controllers/game_controller.py`.

## Generar el Ejecutable (Windows)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name SiuuBross --add-data "assets;assets" main.py
```

El archivo queda en `dist/SiuuBross.exe`. Es un juego gráfico, por lo que se usa la opción `--windowed`. `config.py` detecta cuando se ejecuta empaquetado y busca `assets/` dentro del ejecutable. No se versiona en el repositorio; se distribuye desde la sección Releases de GitHub.

## Notas sobre Seguridad y Credenciales

- El proyecto no usa credenciales, API keys, variables de entorno ni servicios externos, no accede a la red y no guarda datos en disco.
- Solo se usan los recursos gráficos y de audio ya incluidos en `assets/`; no se descargan recursos adicionales.
- Los eventos `jump`, `hurt`, `time_up` y `game_over` no tienen sonido asignado porque no existen archivos de audio para ellos.
- Si se publica el repositorio, se recomienda un `.gitignore` que excluya `__pycache__/`, entornos virtuales y los archivos de PyInstaller (`build/`, `dist/`, `*.spec`).

## Roadmap

- [ ] Pruebas unitarias con pytest para el Modelo
- [ ] Sonidos de salto, daño y Game Over (requieren nuevos archivos de audio)
- [ ] Más niveles y nuevas mecánicas
- [ ] Selector de nivel y guardado del progreso
- [ ] Mejor puntuación guardada en disco
- [ ] Soporte para mando (gamepad)
- [ ] Fondo con desplazamiento (parallax)

## Autor

Juan Fernando Fonseca Martínez

## Licencia

Este proyecto no especifica una licencia por el momento.

## Soporte

Para reportar problemas o sugerir mejoras:

- Abre un Issue en GitHub.
- Describe claramente el problema encontrado.
- Incluye los pasos necesarios para reproducirlo.
- Si es posible, proporciona mensajes de error o capturas de pantalla.