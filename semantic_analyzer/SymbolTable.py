import csv, os

class SymbolTable:
    def __init__(self):
        self.scenes = {}
        self.valid_tokens = self.load_tokens()

    def load_tokens(self):
        path = os.path.join(os.path.dirname(__file__), "..", "datos_propiedades_turismo.csv")
        tokens = set()
        try:
            with open(path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                for row in reader:
                    tokens.add(row[0])
        except Exception as e:
            print(f"⚠️ Advertencia: No se pudo cargar el CSV de tokens: {e}")
        return tokens

    def validate_keyword(self, word):
        if word not in self.valid_tokens:
            raise Exception(f"Error léxico/semántico: '{word}' no es un token válido según el CSV")

    def add_scene(self, name, defined_line=None):
        self.validate_keyword("escena")  # ensure token exists
        if name in self.scenes:
            raise Exception(f"Error semántico: escena '{name}' duplicada.")
        self.scenes[name] = {"dialogues": [], "options": [], "defined_line": defined_line}

    def add_dialogue(self, scene_name, dialogue):
        self.validate_keyword("decir")
        self.scenes[scene_name]["dialogues"].append(dialogue)

    def add_option(self, scene_name, option_text, target_scene):
        self.validate_keyword("opcion")
        self.validate_keyword("ir_a")
        self.scenes[scene_name]["options"].append({"text": option_text, "target": target_scene})

    def check_all(self):
        # Must have 'inicio'
        if "inicio" not in self.scenes:
            raise Exception("Error semántico: falta escena inicial 'inicio'.")

        warnings = []
        for name, data in self.scenes.items():
            if not data["dialogues"]:
                warnings.append(f"⚠️ Escena '{name}' sin narración.")
            if not data["options"]:
                warnings.append(f"⚠️ Escena '{name}' sin opciones (posible final).")

        return warnings
