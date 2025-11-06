# Generated from TurismoLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TurismoLangParser import TurismoLangParser
else:
    from TurismoLangParser import TurismoLangParser

# This class defines a complete generic visitor for a parse tree produced by TurismoLangParser.

class TurismoLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TurismoLangParser#program.
    def visitProgram(self, ctx:TurismoLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TurismoLangParser#scene.
    def visitScene(self, ctx:TurismoLangParser.SceneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TurismoLangParser#dialogue.
    def visitDialogue(self, ctx:TurismoLangParser.DialogueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TurismoLangParser#decir.
    def visitDecir(self, ctx:TurismoLangParser.DecirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TurismoLangParser#opcion.
    def visitOpcion(self, ctx:TurismoLangParser.OpcionContext):
        return self.visitChildren(ctx)



del TurismoLangParser