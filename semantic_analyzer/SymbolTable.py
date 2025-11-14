# ============================================================
#  SymbolTable.py - Tabla de Símbolos de TurismoLang
#  Guarda escenas, diálogos y opciones del programa.
# ============================================================

class SymbolTable:

    # ---------------- Constructor ----------------
    # Crea una tabla vacía donde cada escena tendrá:
    #   - dialogues: lista de textos "decir"
    #   - options: lista de opciones con destino
    def __init__(self):
        self.scenes = {}


    # ---------------- Añadir escena ----------------
    # Registra una nueva escena. No permite duplicadas.
    def add_scene(self, name):
        if name in self.scenes:
            raise Exception(f"escena '{name}' duplicada.")

        self.scenes[name] = {
            "dialogues": [],
            "options": []
        }


    # ---------------- Añadir diálogo ----------------
    # Guarda un texto tipo ("decir", "Mensaje") dentro de una escena.
    def add_dialogue(self, scene_name, dialogue):
        self.scenes[scene_name]["dialogues"].append(dialogue)


    # ---------------- Añadir opción ----------------
    # Registra una opción interactiva con su texto y escena destino.
    def add_option(self, scene_name, option_text, target):
        self.scenes[scene_name]["options"].append({
            "text": option_text,
            "target": target
        })


    # ---------------- Validaciones finales ----------------
    # Comprueba:
    #   - que exista la escena "inicio"
    #   - que no haya escenas sin texto
    #   - que no haya escenas sin opciones
    # Retorna advertencias (no errores)
    def check_all(self):
        if "inicio" not in self.scenes:
            raise Exception("falta escena inicial 'inicio'.")

        warnings = []

        for name, data in self.scenes.items():
            if not data["dialogues"]:
                warnings.append(f"⚠️ escena '{name}' sin texto.")
            if not data["options"]:
                warnings.append(f"⚠️ escena '{name}' sin opciones.")

        return warnings
