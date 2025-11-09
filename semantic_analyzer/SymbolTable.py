class SymbolTable:
    def __init__(self):
        self.scenes = {}

    def add_scene(self, name):
        if name in self.scenes:
            raise Exception(f"escena '{name}' duplicada.")
        self.scenes[name] = {"dialogues": [], "options": []}

    def add_dialogue(self, scene_name, dialogue):
        self.scenes[scene_name]["dialogues"].append(dialogue)

    def add_option(self, scene_name, option_text, target):
        self.scenes[scene_name]["options"].append({
            "text": option_text,
            "target": target
        })

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
