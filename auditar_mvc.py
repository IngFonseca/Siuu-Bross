"""Auditoría del MVC: revisa el código fuente buscando violaciones de las
reglas de dependencia entre Model, View y Controller.

Uso:  python auditar_mvc.py
"""

import glob
import re

# (descripción, patrón prohibido)
MODEL = [
    ("el Model no debe importar la View ni el Controller",
     r"^\s*(from|import)\s+(views|controllers)\b"),
    ("el Model no debe tocar pantalla, audio, imágenes, fuentes ni entrada",
     r"pygame\.(display|mixer|image|font|draw|key|mouse|event|transform|Surface|time)\b"),
]
VIEW = [
    ("la View no debe importar el Controller",
     r"^\s*(from|import)\s+controllers\b"),
    ("la View no debe leer el teclado ni los eventos",
     r"pygame\.(key|event)\b"),
    ("la View no debe modificar el Model (asignaciones a model.*)",
     r"\bmodel\.[A-Za-z_][\w\.]*\s*(=|\+=|-=)(?!=)"),
]
CONTROLLER = [
    ("el Controller no debe dibujar",
     r"pygame\.(draw|font|transform)\b|\.blit\(|\.render\("),
    ("el Controller no debe calcular física ni reglas (acceso a rects)",
     r"\.rect\b"),
]

REGLAS = {"models": MODEL, "views": VIEW, "controllers": CONTROLLER}

problemas = 0
for carpeta, reglas in REGLAS.items():
    for ruta in sorted(glob.glob(f"{carpeta}/*.py")):
        with open(ruta, encoding="utf-8") as f:
            lineas = f.read().splitlines()
        for num, linea in enumerate(lineas, 1):
            codigo = linea.split("#")[0]
            for descripcion, patron in reglas:
                if re.search(patron, codigo):
                    problemas += 1
                    print(f"[VIOLACIÓN] {ruta}:{num}: {descripcion}\n            {linea.strip()}")

# El Model solo puede usar pygame como geometría (pygame.Rect)
for ruta in sorted(glob.glob("models/*.py")):
    with open(ruta, encoding="utf-8") as f:
        usados = set(re.findall(r"pygame\.(\w+)", f.read()))
    extra = usados - {"Rect"}
    if extra:
        problemas += 1
        print(f"[VIOLACIÓN] {ruta}: usa pygame.{', pygame.'.join(sorted(extra))} (solo se permite Rect)")

if problemas == 0:
    print("MVC limpio: no se encontraron violaciones de las reglas de dependencia.")
else:
    print(f"\n{problemas} violación(es) encontrada(s).")