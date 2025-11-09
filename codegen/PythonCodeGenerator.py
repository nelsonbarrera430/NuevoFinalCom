# codegen/PythonCodeGenerator.py
import textwrap

class PythonCodeGenerator:
    def __init__(self, symbol_table):
        # symbol_table.scenes structure from SymbolTable
        self.scenes = symbol_table.scenes

    def _safe_name(self, n):
        # asegurar que el nombre sea un identificador válido en Python (básico)
        return n if n.isidentifier() else ("s_" + n)

    def generate(self):
        lines = []
        lines.append("# Código Python generado automáticamente por TurismoLang\n")
        lines.append("import sys\n")
        # generar funciones por cada escena
        for scene_name, data in self.scenes.items():
            fname = self._safe_name(scene_name)
            lines.append(f"def {fname}():")
            # imprimir diálogos
            if data["dialogues"]:
                for kind, content in data["dialogues"]:
                    if kind == "decir":
                        # content incluye las comillas; usamos eval seguro via repr
                        text = content[1:-1]  # quitar comillas exteriores
                        lines.append(f"    print({repr(text)})")
            else:
                lines.append("    pass")

            # opciones
            if data["options"]:
                option_texts = [opt["text"][1:-1] for opt in data["options"]]
                prompt = " / ".join(option_texts)
                lines.append(f"    opcion = input({repr(prompt + ' -> ')})")
                for opt in data["options"]:
                    opt_text = opt["text"][1:-1]
                    target = self._safe_name(opt["target"])
                    lines.append(f"    if opcion == {repr(opt_text)}:")
                    lines.append(f"        return {target}()")
                # si no coincide ninguna opción, repetir la misma escena
                lines.append("    print('Opción no reconocida, intenta de nuevo.')")
                lines.append(f"    return {fname}()")
            else:
                lines.append("    return None")
            lines.append("")  # linea en blanco

        # llamada inicial
        start = "inicio" if "inicio" in self.scenes else next(iter(self.scenes), None)
        if start:
            start_name = self._safe_name(start)
            lines.append("if __name__ == '__main__':")
            lines.append(f"    {start_name}()")
        else:
            lines.append("if __name__ == '__main__':")
            lines.append("    print('No hay escenas definidas.')")

        return "\n".join(lines)
