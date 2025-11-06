# main.py
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "generated"))

from antlr4 import *
from TurismoLangLexer import TurismoLangLexer
from TurismoLangParser import TurismoLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.PythonCodeGenerator import PythonCodeGenerator

def main():
    # ✅ Usar archivo pasado como parámetro o default input.txt
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"

    try:
        input_stream = FileStream(input_file, encoding="utf-8")
    except Exception:
        print(f"❌ No se encontró el archivo '{input_file}'.")
        return

    lexer = TurismoLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TurismoLangParser(stream)
    tree = parser.program()

    # Semantic analysis
    visitor = SemanticVisitor()
    try:
        table = visitor.visitProgram(tree)  # returns SymbolTable
    except Exception as e:
        print(f"❌ Error semántico: {e}")
        return

    # Verify referenced scenes
    missing = []
    for name, data in table.scenes.items():
        for opt in data["options"]:
            target = opt["target"]
            if target not in table.scenes:
                missing.append((name, target))

    if missing:
        for sc, tgt in missing:
            print(f"❌ Error semántico: la escena '{sc}' tiene una opción que referencia a '{tgt}' que no existe.")
        return

    # Semantic table checks
    try:
        warnings = table.check_all()
    except Exception as e:
        print(f"❌ Error semántico: {e}")
        return

    for w in warnings:
        print(w)

    # Code generation
    generator = PythonCodeGenerator(table)
    code = generator.generate()

    with open("output_program.py", "w", encoding="utf-8") as f:
        f.write("# Código Python generado automáticamente\n")
        f.write(code)

    print("✅ Compilación finalizada. Archivo generado: output_program.py")

if __name__ == "__main__":
    main()

