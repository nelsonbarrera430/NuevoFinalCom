# Generated from TurismoLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TurismoLangParser import TurismoLangParser
else:
    from TurismoLangParser import TurismoLangParser

# This class defines a complete listener for a parse tree produced by TurismoLangParser.
class TurismoLangListener(ParseTreeListener):

    # Enter a parse tree produced by TurismoLangParser#program.
    def enterProgram(self, ctx:TurismoLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by TurismoLangParser#program.
    def exitProgram(self, ctx:TurismoLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by TurismoLangParser#scene.
    def enterScene(self, ctx:TurismoLangParser.SceneContext):
        pass

    # Exit a parse tree produced by TurismoLangParser#scene.
    def exitScene(self, ctx:TurismoLangParser.SceneContext):
        pass


    # Enter a parse tree produced by TurismoLangParser#dialogue.
    def enterDialogue(self, ctx:TurismoLangParser.DialogueContext):
        pass

    # Exit a parse tree produced by TurismoLangParser#dialogue.
    def exitDialogue(self, ctx:TurismoLangParser.DialogueContext):
        pass


    # Enter a parse tree produced by TurismoLangParser#decir.
    def enterDecir(self, ctx:TurismoLangParser.DecirContext):
        pass

    # Exit a parse tree produced by TurismoLangParser#decir.
    def exitDecir(self, ctx:TurismoLangParser.DecirContext):
        pass


    # Enter a parse tree produced by TurismoLangParser#opcion.
    def enterOpcion(self, ctx:TurismoLangParser.OpcionContext):
        pass

    # Exit a parse tree produced by TurismoLangParser#opcion.
    def exitOpcion(self, ctx:TurismoLangParser.OpcionContext):
        pass



del TurismoLangParser