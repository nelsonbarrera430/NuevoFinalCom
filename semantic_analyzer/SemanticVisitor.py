# semantic_analyzer/SemanticVisitor.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "generated"))

from TurismoLangParser import TurismoLangParser
from TurismoLangVisitor import TurismoLangVisitor
from .SymbolTable import SymbolTable

class SemanticVisitor(TurismoLangVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self._current_scene = None

    def visitProgram(self, ctx:TurismoLangParser.ProgramContext):
        for sc in ctx.scene():
            self.visit(sc)
        return self.table

    def visitScene(self, ctx:TurismoLangParser.SceneContext):
        name = ctx.ID().getText()
        self._current_scene = name
        self.table.add_scene(name, defined_line=ctx.start.line)
        for d in ctx.dialogue():
            self.visit(d)
        self._current_scene = None
        return None

    def visitDecir(self, ctx:TurismoLangParser.DecirContext):
        text = ctx.STRING().getText()
        self.table.add_dialogue(self._current_scene, ("decir", text))
        return None

    def visitOpcion(self, ctx:TurismoLangParser.OpcionContext):
        text = ctx.STRING().getText()
        target = ctx.ID().getText()
        self.table.add_option(self._current_scene, text, target)
        return None
