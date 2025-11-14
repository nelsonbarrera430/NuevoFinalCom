# ---------------------------
# main.py – Pipeline del compilador TurismoLang
# ---------------------------

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "generated"))

from antlr4 import *
from antlr4.Token import Token
from TurismoLangLexer import TurismoLangLexer
from TurismoLangParser import TurismoLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.PythonCodeGenerator import PythonCodeGenerator


# ----- Árbol sintáctico formateado -----
def pretty_tree(node, rules, indent=0):
    from antlr4.tree.Tree import TerminalNodeImpl
    sp = "  " * indent
    if isinstance(node, TerminalNodeImpl):
        return sp + f"'{node.getText()}'\n"
    out = sp + rules[node.getRuleIndex()] + "\n"
    for c in node.children or []:
        out += pretty_tree(c, rules, indent + 1)
    return out


# ----- Fase léxica -----
def debug_tokens(file, log):
    log.write("\n--- TOKENS ---\n")
    lexer = TurismoLangLexer(FileStream(file, encoding="utf-8"))
    tok = lexer.nextToken()
    while tok.type != Token.EOF:
        name = lexer.symbolicNames[tok.type] if tok.type < len(lexer.symbolicNames) else tok.type
        log.write(f"{tok.text} → {name}\n")
        tok = lexer.nextToken()
    log.write("--------------\n\n")


# ----- Pipeline principal -----
def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    if not os.path.exists(input_file):
        print(f"❌ Archivo no encontrado: {input_file}")
        return

    with open("output_fases.txt", "w", encoding="utf-8") as log:

        # 1. Léxico
        debug_tokens(input_file, log)

        # 2. Sintaxis
        stream = CommonTokenStream(TurismoLangLexer(FileStream(input_file, encoding="utf-8")))
        parser = TurismoLangParser(stream)
        tree = parser.program()
        log.write("--- ÁRBOL SINTÁCTICO ---\n")
        log.write(pretty_tree(tree, parser.ruleNames))
        log.write("------------------------\n\n")

        # 3. Semántica
        visitor = SemanticVisitor()
        try:
            table = visitor.visitProgram(tree)
        except Exception as e:
            log.write(f"❌ Error semántico: {e}")
            print(f"❌ Error semántico: {e}")
            return

        # Tabla de símbolos
        log.write("--- TABLA DE SÍMBOLOS ---\n")
        for name, data in table.scenes.items():
            log.write(f"{name}:\n")
            log.write(f"  Diálogos: {data['dialogues']}\n")
            log.write(f"  Opciones: {data['options']}\n")
        log.write("-------------------------\n\n")

        # Validaciones globales
        try:
            for w in table.check_all():
                log.write(w + "\n")
        except Exception as e:
            log.write(f"❌ Error semántico: {e}")
            print(f"❌ Error semántico: {e}")
            return

        # 4. Generación de código
        code = PythonCodeGenerator(table).generate()
        open("output_program.py", "w", encoding="utf-8").write(code)

    print("✅ Fases guardadas en output_fases.txt")


if __name__ == "__main__":
    main()
