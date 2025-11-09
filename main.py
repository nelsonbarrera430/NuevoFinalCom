# main.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "generated"))

from antlr4 import *
from TurismoLangLexer import TurismoLangLexer
from TurismoLangParser import TurismoLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.PythonCodeGenerator import PythonCodeGenerator
from antlr4.Token import Token

def debug_tokens(input_file):
    print("\n================= FASE LÉXICA (TOKENS) =================")
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = TurismoLangLexer(input_stream)

    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else str(token.type)
        print(f"{token.text} -> {token_name}")
        token = lexer.nextToken()
    print("========================================================\n")

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"

    if not os.path.exists(input_file):
        print(f"❌ Archivo no encontrado: {input_file}")
        return

    # 1) Lexer debug
    debug_tokens(input_file)

    # 2) Parser
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = TurismoLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TurismoLangParser(stream)
    tree = parser.program()

    print("=============== FASE SINTÁCTICA (Parse Tree) ===============")
    print(tree.toStringTree(recog=parser))
    print("===========================================================\n")

    # 3) Semantic visitor
    visitor = SemanticVisitor()
    try:
        table = visitor.visitProgram(tree)
    except Exception as e:
        print(f"❌ Error semántico: {e}")
        return

    # 4) Tabla de símbolos
    print("=============== TABLA DE SÍMBOLOS ===============")
    for name, data in table.scenes.items():
        print(f"\nEscena: {name}")
        print(f"  Diálogos: {data['dialogues']}")
        print(f"  Opciones: {data['options']}")
    print("=================================================\n")

    # 5) Validaciones semánticas
    try:
        warnings = table.check_all()
        for w in warnings:
            print(w)
    except Exception as e:
        print(f"❌ Error semántico: {e}")
        return

    # 6) Code generation
    generator = PythonCodeGenerator(table)
    code = generator.generate()

    with open("output_program.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("✅ Código generado: output_program.py")
    print("🎮 Ejecuta tu juego con:  python output_program.py")

if __name__ == "__main__":
    main()
