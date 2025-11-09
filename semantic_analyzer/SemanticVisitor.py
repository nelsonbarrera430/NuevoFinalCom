from TurismoLangVisitor import TurismoLangVisitor
from .SymbolTable import SymbolTable
from TurismoLangVisitor import TurismoLangVisitor

class SemanticVisitor(TurismoLangVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.current_scene = None

    def visitProgram(self, ctx):
        print("=== FASE SEMÁNTICA ===")
        for scene in ctx.scene():
            self.visit(scene)
        print("======================\n")
        return self.table

    def visitScene(self, ctx):
        name = ctx.ID().getText()
        print(f"[SEM] Escena detectada: {name}")
        self.current_scene = name
        self.table.add_scene(name)
        for d in ctx.dialogue():
            self.visit(d)
        self.current_scene = None

    def visitDecir(self, ctx):
        text = ctx.STRING().getText()
        print(f"[SEM] Diálogo en {self.current_scene}: {text}")
        self.table.add_dialogue(self.current_scene, ("decir", text))

    def visitOpcion(self, ctx):
        text = ctx.STRING().getText()
        target = ctx.ID().getText()
        print(f"[SEM] Opción en {self.current_scene}: '{text}' -> {target}")
        self.table.add_option(self.current_scene, text, target)
