# Generated from TurismoLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,4,1,22,8,1,11,1,12,1,23,1,1,
        1,1,1,2,1,2,3,2,30,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,0,0,5,0,2,4,6,8,0,0,39,0,11,1,0,0,0,2,17,1,0,0,0,4,29,1,0,0,0,
        6,31,1,0,0,0,8,35,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,
        0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,
        1,0,0,0,17,18,5,4,0,0,18,19,5,8,0,0,19,21,5,1,0,0,20,22,3,4,2,0,
        21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,
        0,0,0,25,26,5,2,0,0,26,3,1,0,0,0,27,30,3,6,3,0,28,30,3,8,4,0,29,
        27,1,0,0,0,29,28,1,0,0,0,30,5,1,0,0,0,31,32,5,5,0,0,32,33,5,9,0,
        0,33,34,5,3,0,0,34,7,1,0,0,0,35,36,5,6,0,0,36,37,5,9,0,0,37,38,5,
        7,0,0,38,39,5,8,0,0,39,40,5,3,0,0,40,9,1,0,0,0,3,13,23,29
    ]

class TurismoLangParser ( Parser ):

    grammarFileName = "TurismoLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'escena'", "'decir'", 
                     "'opcion'", "'ir_a'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ESCENA", "DECIR", "OPCION", "IR_A", "ID", "STRING", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_scene = 1
    RULE_dialogue = 2
    RULE_decir = 3
    RULE_opcion = 4

    ruleNames =  [ "program", "scene", "dialogue", "decir", "opcion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ESCENA=4
    DECIR=5
    OPCION=6
    IR_A=7
    ID=8
    STRING=9
    WS=10
    COMMENT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TurismoLangParser.EOF, 0)

        def scene(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TurismoLangParser.SceneContext)
            else:
                return self.getTypedRuleContext(TurismoLangParser.SceneContext,i)


        def getRuleIndex(self):
            return TurismoLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TurismoLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.scene()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 15
            self.match(TurismoLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SceneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCENA(self):
            return self.getToken(TurismoLangParser.ESCENA, 0)

        def ID(self):
            return self.getToken(TurismoLangParser.ID, 0)

        def dialogue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TurismoLangParser.DialogueContext)
            else:
                return self.getTypedRuleContext(TurismoLangParser.DialogueContext,i)


        def getRuleIndex(self):
            return TurismoLangParser.RULE_scene

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScene" ):
                listener.enterScene(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScene" ):
                listener.exitScene(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScene" ):
                return visitor.visitScene(self)
            else:
                return visitor.visitChildren(self)




    def scene(self):

        localctx = TurismoLangParser.SceneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scene)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(TurismoLangParser.ESCENA)
            self.state = 18
            self.match(TurismoLangParser.ID)
            self.state = 19
            self.match(TurismoLangParser.T__0)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.dialogue()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==6):
                    break

            self.state = 25
            self.match(TurismoLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DialogueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decir(self):
            return self.getTypedRuleContext(TurismoLangParser.DecirContext,0)


        def opcion(self):
            return self.getTypedRuleContext(TurismoLangParser.OpcionContext,0)


        def getRuleIndex(self):
            return TurismoLangParser.RULE_dialogue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDialogue" ):
                listener.enterDialogue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDialogue" ):
                listener.exitDialogue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDialogue" ):
                return visitor.visitDialogue(self)
            else:
                return visitor.visitChildren(self)




    def dialogue(self):

        localctx = TurismoLangParser.DialogueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dialogue)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.decir()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.opcion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIR(self):
            return self.getToken(TurismoLangParser.DECIR, 0)

        def STRING(self):
            return self.getToken(TurismoLangParser.STRING, 0)

        def getRuleIndex(self):
            return TurismoLangParser.RULE_decir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecir" ):
                listener.enterDecir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecir" ):
                listener.exitDecir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecir" ):
                return visitor.visitDecir(self)
            else:
                return visitor.visitChildren(self)




    def decir(self):

        localctx = TurismoLangParser.DecirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(TurismoLangParser.DECIR)
            self.state = 32
            self.match(TurismoLangParser.STRING)
            self.state = 33
            self.match(TurismoLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPCION(self):
            return self.getToken(TurismoLangParser.OPCION, 0)

        def STRING(self):
            return self.getToken(TurismoLangParser.STRING, 0)

        def IR_A(self):
            return self.getToken(TurismoLangParser.IR_A, 0)

        def ID(self):
            return self.getToken(TurismoLangParser.ID, 0)

        def getRuleIndex(self):
            return TurismoLangParser.RULE_opcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcion" ):
                listener.enterOpcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcion" ):
                listener.exitOpcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcion" ):
                return visitor.visitOpcion(self)
            else:
                return visitor.visitChildren(self)




    def opcion(self):

        localctx = TurismoLangParser.OpcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_opcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(TurismoLangParser.OPCION)
            self.state = 36
            self.match(TurismoLangParser.STRING)
            self.state = 37
            self.match(TurismoLangParser.IR_A)
            self.state = 38
            self.match(TurismoLangParser.ID)
            self.state = 39
            self.match(TurismoLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





