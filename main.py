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


# ----- Imprimir árbol sintáctico con indentación -----
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



# ---------------------------
#       MAIN PIPELINE
# ---------------------------
def main():

    # archivo de entrada
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    if not os.path.exists(input_file):
        print(f"❌ Archivo no encontrado: {input_file}")
        return

    print(f"📄 Ejecutando test: {input_file}")

    # ---------------------------
    # Crear carpeta FasesTests si no existe
    # ---------------------------
    output_dir = "FasesTests"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Carpeta creada: {output_dir}")

    # nombre automático del archivo de fases
    base = os.path.splitext(os.path.basename(input_file))[0]
    log_path = os.path.join(output_dir, f"{base}_fases.txt")

    passed = True
    error_msg = None

    with open(log_path, "w", encoding="utf-8") as log:

        # ------- 1. Fase Léxica -------
        debug_tokens(input_file, log)

        # ------- 2. Fase Sintáctica -------
        try:
            stream = CommonTokenStream(TurismoLangLexer(FileStream(input_file, encoding="utf-8")))
            parser = TurismoLangParser(stream)
            tree = parser.program()
        except Exception as e:
            passed = False
            error_msg = f"Error sintáctico: {e}"
            log.write("❌ " + error_msg + "\n")

        if not passed:
            print(f"❌ TEST FALLÓ: {error_msg}")
            return

        log.write("--- ÁRBOL SINTÁCTICO ---\n")
        log.write(pretty_tree(tree, parser.ruleNames))
        log.write("------------------------\n\n")

        # ------- 3. Fase Semántica -------
        visitor = SemanticVisitor(log)
        try:
            table = visitor.visitProgram(tree)
        except Exception as e:
            passed = False
            error_msg = f"Error semántico: {e}"
            log.write("❌ " + error_msg + "\n")

        if not passed:
            print(f"❌ TEST FALLÓ: {error_msg}")
            return

        # ------- Tabla de símbolos -------
        log.write("--- TABLA DE SÍMBOLOS ---\n")
        for name, data in table.scenes.items():
            log.write(f"{name}:\n")
            log.write(f"  Diálogos: {data['dialogues']}\n")
            log.write(f"  Opciones: {data['options']}\n")
        log.write("-------------------------\n\n")

        # ------- Validaciones globales -------
        try:
            for w in table.check_all():
                log.write(w + "\n")
        except Exception as e:
            passed = False
            error_msg = f"Error semántico: {e}"
            log.write("❌ " + error_msg + "\n")

        if not passed:
            print(f"❌ TEST FALLÓ: {error_msg}")
            return

        # ------- 4. Generación de código -------
        code = PythonCodeGenerator(table).generate()
        with open("output_program.py", "w", encoding="utf-8") as f:
            f.write(code)

    # RESULTADO FINAL
    if passed:
        print(f"✅ TEST PASÓ: {input_file}")
        print(f"📦 Archivo generado en: {log_path}")
    else:
        print(f"❌ TEST FALLÓ: {error_msg}")


if __name__ == "__main__":
    main()
