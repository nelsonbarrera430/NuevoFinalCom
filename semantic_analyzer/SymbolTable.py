# ============================================================
#  SymbolTable.py - Tabla de Símbolos de TurismoLang
#  Almacena todas las escenas, sus diálogos y sus opciones.
#  Es usada por el analizador semántico y el generador de código.
# ============================================================

class SymbolTable:

    # ------------------------------------------------------------
    # Constructor: crea la estructura base de la tabla de símbolos.
    # self.scenes es un diccionario donde cada clave es el nombre
    # de una escena, y su valor contiene diálogos y opciones.
    # ------------------------------------------------------------
    def __init__(self):
        self.scenes = {}  # tabla vacía al inicio


    # ------------------------------------------------------------
    # add_scene(name)
    # Registra una nueva escena en la tabla.
    # Lanza error si ya existe una escena con el mismo nombre.
    # ------------------------------------------------------------
    def add_scene(self, name):
        if name in self.scenes:
            # Escenas duplicadas están prohibidas → error obligatorio
            raise Exception(f"escena '{name}' duplicada.")

        # Crear estructura vacía para la escena
        self.scenes[name] = {
            "dialogues": [],   # lista de ("decir", "texto")
            "options": []      # lista de {"text": "...", "target": "..."}
        }


    # ------------------------------------------------------------
    # add_dialogue(scene_name, dialogue)
    # Guarda un diálogo dentro de la escena indicada.
    # dialogue tiene forma ("decir", "Texto")
    # ------------------------------------------------------------
    def add_dialogue(self, scene_name, dialogue):
        self.scenes[scene_name]["dialogues"].append(dialogue)


    # ------------------------------------------------------------
    # add_option(scene_name, option_text, target)
    # Registra una opción interactiva dentro de una escena.
    #
    #   option_text → texto visible al usuario
    #   target      → escena a la que saltará cuando elija esa opción
    # ------------------------------------------------------------
    def add_option(self, scene_name, option_text, target):
        self.scenes[scene_name]["options"].append({
            "text": option_text,
            "target": target
        })


    # ------------------------------------------------------------
    # check_all()
    # Validaciones globales del programa antes de generar código:
    #
    #   - Debe existir la escena "inicio"
    #   - Las escenas no deberían quedar sin diálogos
    #   - Tampoco deberían quedar sin opciones
    #
    # Devuelve *advertencias* (no errores).
    # ------------------------------------------------------------
    def check_all(self):
        # La escena inicial es obligatoria
        if "inicio" not in self.scenes:
            raise Exception("falta escena inicial 'inicio'.")

        warnings = []

        # Verificar cada escena
        for name, data in self.scenes.items():

            # Si no tiene diálogos → warning
            if not data["dialogues"]:
                warnings.append(f"⚠️ escena '{name}' sin texto.")

            # Si no tiene opciones → warning
            if not data["options"]:
                warnings.append(f"⚠️ escena '{name}' sin opciones.")

        return warnings
