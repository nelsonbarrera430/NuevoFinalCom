# codegen/PythonCodeGenerator.py
import textwrap

class PythonCodeGenerator:
    def __init__(self, symbol_table):
        # symbol_table.scenes structure from SymbolTable
        self.scenes = symbol_table.scenes

    def generate(self):
        lines = []
        # For each scene, create a Python function
        for scene_name, data in self.scenes.items():
            lines.append(f"def {scene_name}():")
            # dialogues
            if data["dialogues"]:
                for kind, content in data["dialogues"]:
                    if kind == "decir":
                        # content includes quotes, remove outer quotes for safe print
                        text = content[1:-1]
                        lines.append(f"    print({repr(text)})")
            else:
                lines.append(f"    pass  # escena sin instrucciones")

            # options: build prompt if there are options
            if data["options"]:
                # prompt: join option texts
                option_texts = [opt["text"][1:-1] for opt in data["options"]]
                prompt = " / ".join(option_texts)
                # create input and branches
                lines.append(f"    opcion = input({repr(prompt + ' -> ')})")
                for opt in data["options"]:
                    opt_text = opt["text"][1:-1]
                    target = opt["target"]
                    # call target if chosen
                    lines.append(f"    if opcion == {repr(opt_text)}:")
                    lines.append(f"        {target}()")
            lines.append("")  # blank line between functions

        # call inicio at the end
        lines.append("if __name__ == '__main__':")
        lines.append("    inicio()")
        return "\n".join(lines)
