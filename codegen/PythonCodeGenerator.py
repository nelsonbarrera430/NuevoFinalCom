# ============================================================
#  PythonCodeGenerator.py
#  Generador de código para el lenguaje TurismoLang
#
#  Convierte la tabla de símbolos en un programa Python
#  donde cada escena se transforma en una función, y las
#  opciones permiten navegar entre escenas mediante input().
# ============================================================

class PythonCodeGenerator:
    def __init__(self, symbol_table):
        # Estructura con todas las escenas procesadas por el analizador semántico
        self.scenes = symbol_table.scenes

    # Convierte nombres de escenas en identificadores válidos de Python
    def _safe_name(self, name):
        return name if name.isidentifier() else f"s_{name}"

    def generate(self):
        code = []

        # Encabezado del archivo generado
        code.append("# Código generado automáticamente por TurismoLang\n")
        code.append("import sys\n")

        # ------------------------------------------------------------
        # Generación de funciones para cada escena
        # ------------------------------------------------------------
        for scene, data in self.scenes.items():
            func_name = self._safe_name(scene)
            code.append(f"def {func_name}():")

            # Mostrar diálogos
            for kind, content in data["dialogues"]:
                if kind == "decir":
                    text = content[1:-1]   # quitar comillas
                    code.append(f"    print({repr(text)})")

            # Manejar opciones
            if data["options"]:
                options_list = [opt["text"][1:-1] for opt in data["options"]]
                prompt = " / ".join(options_list)

                code.append(f"    opcion = input({repr(prompt + ' -> ')})")

                # Generar condiciones
                for opt in data["options"]:
                    opt_text = opt["text"][1:-1]
                    target = self._safe_name(opt["target"])

                    code.append(f"    if opcion == {repr(opt_text)}:")
                    code.append(f"        return {target}()")

                code.append("    print('Opción no válida, intenta de nuevo.')")
                code.append(f"    return {func_name}()")
            else:
                code.append("    return None")

            code.append("")  # línea en blanco

        # ------------------------------------------------------------
        # Punto de entrada (escena "inicio")
        # ------------------------------------------------------------
        start = "inicio" if "inicio" in self.scenes else next(iter(self.scenes))
        start_fn = self._safe_name(start)

        code.append("if __name__ == '__main__':")
        code.append(f"    {start_fn}()")

        return "\n".join(code)
