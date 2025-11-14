# main.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "generated"))

from antlr4 import *
from TurismoLangLexer import TurismoLangLexer
from TurismoLangParser import TurismoLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.PythonCodeGenerator import PythonCodeGenerator
from antlr4.Token import Token
from io import StringIO

# ----------- Mostrar Tokens (Lexer) -----------
def debug_tokens(input_file, log):
    log.write("\n================= FASE LÉXICA (TOKENS) =================\n")
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = TurismoLangLexer(input_stream)

    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else str(token.type)
        log.write(f"{token.text} -> {token_name}\n")
        token = lexer.nextToken()
    log.write("========================================================\n\n")

# ----------- MAIN COMPILER PIPELINE -----------
def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"

    if not os.path.exists(input_file):
        print(f"❌ Archivo no encontrado: {input_file}")
        return

    # Abrir log para fases
    log_path = "output_fases.txt"
    with open(log_path, "w", encoding="utf-8") as log:

        # 1) Lexer
        debug_tokens(input_file, log)

        # 2) Parser
        input_stream = FileStream(input_file, encoding="utf-8")
        lexer = TurismoLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = TurismoLangParser(stream)
        tree = parser.program()

        log.write("=============== FASE SINTÁCTICA (Parse Tree) ===============\n")
        log.write(tree.toStringTree(recog=parser) + "\n")
        log.write("===========================================================\n\n")

        # 3) Visitor Semántico
        visitor = SemanticVisitor()
        try:
            table = visitor.visitProgram(tree)
        except Exception as e:
            log.write(f"❌ Error semántico: {e}\n")
            print(f"❌ Error semántico: {e}")
            return

        # 4) Tabla de símbolos
        log.write("=============== TABLA DE SÍMBOLOS ===============\n")
        for name, data in table.scenes.items():
            log.write(f"\nEscena: {name}\n")
            log.write(f"  Diálogos: {data['dialogues']}\n")
            log.write(f"  Opciones: {data['options']}\n")
        log.write("=================================================\n\n")

        # Validaciones semánticas
        try:
            warnings = table.check_all()
            for w in warnings:
                log.write(w + "\n")
        except Exception as e:
            log.write(f"❌ Error semántico: {e}\n")
            print(f"❌ Error semántico: {e}")
            return

        # 5) Generación de código
        generator = PythonCodeGenerator(table)
        code = generator.generate()

        with open("output_program.py", "w", encoding="utf-8") as f:
            f.write(code)

        log.write("✅ Código generado: output_program.py\n")
        log.write("🎮 Ejecuta tu juego con: python output_program.py\n")

    print(f"✅ Proceso completo guardado en {log_path}")
    print("🎮 Ejecuta tu juego con: python output_program.py")

if __name__ == "__main__":
    main()
