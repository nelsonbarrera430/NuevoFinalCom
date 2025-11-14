from TurismoLangVisitor import TurismoLangVisitor
from .SymbolTable import SymbolTable

class SemanticVisitor(TurismoLangVisitor):

    # ----------------------------------------------------------
    # Constructor: inicializa tabla y archivo de log
    # ----------------------------------------------------------
    def __init__(self, log=None):
        self.table = SymbolTable()      # Tabla de símbolos
        self.current_scene = None       # Escena actual procesándose
        self.log = log                  # Archivo output_fases.txt

    # ----------------------------------------------------------
    # Función auxiliar: escribir en el archivo de log
    # ----------------------------------------------------------
    def _log(self, msg):
        if self.log:
            self.log.write(msg + "\n")

    # ----------------------------------------------------------
    # Fase Semántica: inicio del recorrido del programa
    # ----------------------------------------------------------
    def visitProgram(self, ctx):--
        self._log("=== FASE SEMÁNTICA ===")

        for scene in ctx.scene():
            self.visit(scene)

        self._log("======================")
        return self.table

    # ----------------------------------------------------------
    # Visitador de cada escena del lenguaje
    # ----------------------------------------------------------
    def visitScene(self, ctx):
        name = ctx.ID().getText()
        self.current_scene = name

        self._log(f"[SEM] Escena detectada: {name}")

        # Registrar escena en la tabla
        self.table.add_scene(name)

        # Procesar diálogos y opciones dentro de la escena
        for d in ctx.dialogue():
            self.visit(d)

        self.current_scene = None

    # ----------------------------------------------------------
    # Visitador de una instrucción "decir"
    # ----------------------------------------------------------
    def visitDecir(self, ctx):
        text = ctx.STRING().getText()

        self._log(f"[SEM] Diálogo en {self.current_scene}: {text}")

        # Guardar diálogo en la tabla
        self.table.add_dialogue(self.current_scene, ("decir", text))

    # ----------------------------------------------------------
    # Visitador de una instrucción "opcion"
    # ----------------------------------------------------------
    def visitOpcion(self, ctx):
        text = ctx.STRING().getText()
        target = ctx.ID().getText()

        self._log(f"[SEM] Opción en {self.current_scene}: '{text}' -> {target}")

        # Registrar la opción en la tabla
        self.table.add_option(self.current_scene, text, target)
