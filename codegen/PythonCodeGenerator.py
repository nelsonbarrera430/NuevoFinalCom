# ============================================================
#  PythonCodeGenerator.py
#  Generador de código para el lenguaje TurismoLang
#
#  Convierte la tabla de símbolos en un programa Python.
#  Cada escena del lenguaje se transforma en una función.
#  Las opciones permiten navegar entre escenas con input().
# ============================================================

class PythonCodeGenerator:
    def __init__(self, symbol_table):
        # Guarda las escenas procesadas por la fase semántica
        self.scenes = symbol_table.scenes

    # ------------------------------------------------------------
    # Normaliza un nombre de escena para que sea un identificador
    # válido en Python (sin espacios, empieza por letra, etc.)
    # ------------------------------------------------------------
    def _safe_name(self, name):
        return name if name.isidentifier() else f"s_{name}"

    # ------------------------------------------------------------
    # generate() — Genera el código Python final como un string
    # ------------------------------------------------------------
    def generate(self):
        code = []  # lista de líneas que luego uniremos

        # -------------------------
        # Encabezado del archivo
        # -------------------------
        code.append("# Código generado automáticamente por TurismoLang\n")
        code.append("import sys\n")  # por si el usuario lo requiere

        # ============================================================
        #   GENERAR UNA FUNCIÓN POR CADA ESCENA
        # ============================================================
        for scene, data in self.scenes.items():

            # Convertir nombre de escena en función válida
            func_name = self._safe_name(scene)

            # Iniciar definición de función
            code.append(f"def {func_name}():")

            # --------------------------------------------------------
            # Agregar líneas para los diálogos de la escena
            # --------------------------------------------------------
            for kind, content in data["dialogues"]:
                if kind == "decir":
                    text = content[1:-1]   # quitamos las comillas del STRING
                    code.append(f"    print({repr(text)})")  # imprime diálogo

            # --------------------------------------------------------
            # Agregar manejo de opciones
            # --------------------------------------------------------
            if data["options"]:
                # Lista con textos de opciones (sin comillas internas)
                options_list = [opt['text'][1:-1] for opt in data["options"]]

                # Construir mensaje de input: "Ir al parque / Volver -> "
                prompt = " / ".join(options_list)

                # Pedir al usuario elegir opción
                code.append(f"    opcion = input({repr(prompt + ' -> ')})")

                # ---- Crear IF por cada opción ----
                for opt in data["options"]:
                    opt_text = opt["text"][1:-1]       # texto sin comillas
                    target = self._safe_name(opt["target"])  # función destino

                    # Si coincide con la opción escrita → llamar escena destino
                    code.append(f"    if opcion == {repr(opt_text)}:")
                    code.append(f"        return {target}()")

                # Si ninguna coincidió → error + repetir escena
                code.append("    print('Opción no válida, intenta de nuevo.')")
                code.append(f"    return {func_name}()")

            else:
                # Si una escena no tiene opciones, simplemente termina
                code.append("    return None")

            code.append("")  # línea en blanco para separar funciones

        # ============================================================
        #       PUNTO DE ENTRADA DEL PROGRAMA (escena 'inicio')
        # ============================================================
        start = "inicio" if "inicio" in self.scenes else next(iter(self.scenes))
        start_fn = self._safe_name(start)

        # Código que ejecuta la primera escena
        code.append("if __name__ == '__main__':")
        code.append(f"    {start_fn}()")

        # Convertir lista de líneas en un solo string
        return "\n".join(code)
