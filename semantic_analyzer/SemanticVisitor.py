# ============================================================
#  SemanticVisitor.py
#  Analizador semántico del lenguaje TurismoLang
#
#  Se encarga de:
#    - Registrar cada escena del programa
#    - Guardar diálogos y opciones dentro de la tabla de símbolos
#    - Validar que las escenas y saltos existan
#    - Detectar errores semánticos (escenas repetidas, sin inicio, etc.)
# ============================================================

from TurismoLangVisitor import TurismoLangVisitor
from .SymbolTable import SymbolTable


class SemanticVisitor(TurismoLangVisitor):

    def __init__(self):
        # Tabla de símbolos donde se almacenan escenas, diálogos y opciones
        self.table = SymbolTable()
        self.current_scene = None  # Escena que se está procesando

    # ------------------------------------------------------------
    # visitProgram
    # Recorre todas las escenas del archivo fuente
    # ------------------------------------------------------------
    def visitProgram(self, ctx):
        print("=== FASE SEMÁNTICA ===")

        for scene in ctx.scene():
            self.visit(scene)

        print("======================\n")
        return self.table

    # ------------------------------------------------------------
    # visitScene
    # Procesa una escena: la registra y recorre su contenido
    # ------------------------------------------------------------
    def visitScene(self, ctx):
        name = ctx.ID().getText()
        print(f"[SEM] Escena detectada: {name}")

        self.current_scene = name
        self.table.add_scene(name)  # Guardar en la tabla de símbolos

        # Procesar los elementos internos (decir, opcion)
        for d in ctx.dialogue():
            self.visit(d)

        self.current_scene = None

    # ------------------------------------------------------------
    # visitDecir
    # Registra un diálogo dentro de la escena actual
    # ------------------------------------------------------------
    def visitDecir(self, ctx):
        text = ctx.STRING().getText()
        print(f"[SEM] Diálogo en {self.current_scene}: {text}")

        self.table.add_dialogue(self.current_scene, ("decir", text))

    # ------------------------------------------------------------
    # visitOpcion
    # Registra una opción y su destino
    # ------------------------------------------------------------
    def visitOpcion(self, ctx):
        text = ctx.STRING().getText()
        target = ctx.ID().getText()

        print(f"[SEM] Opción en {self.current_scene}: '{text}' -> {target}")

        self.table.add_option(self.current_scene, text, target)
