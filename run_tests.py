import os
import subprocess

TEST_DIR = "tests"

valid_passed = 0
valid_total = 0
invalid_passed = 0
invalid_total = 0

for filename in os.listdir(TEST_DIR):
    if not filename.endswith(".txt"):
        continue

    path = os.path.join(TEST_DIR, filename)

    # Copiar el archivo como input.txt
    os.system(f"cp {path} input.txt")

    print(f"\n🔎 Probando: {filename}")

    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    output = result.stdout + result.stderr

    if "Error" in output or "error" in output.lower():
        # debe ser inválido
        if filename.startswith("invalid"):
            invalid_passed += 1
            print(f"✅ INVALIDO detectado correctamente")
        else:
            print(f"❌ ERROR: archivo válido marcado como inválido")
        invalid_total += filename.startswith("invalid")
        valid_total += filename.startswith("valid")

    else:
        # debe ser válido
        if filename.startswith("valid"):
            valid_passed += 1
            print(f"✅ VÁLIDO compiló correctamente")
        else:
            print(f"❌ ERROR: archivo inválido pasó como válido")
        valid_total += filename.startswith("valid")
        invalid_total += filename.startswith("invalid")

print("\n📊 RESULTADOS FINALES:")
print(f"✔️ Válidos correctos: {valid_passed}/{valid_total}")
print(f"❌ Inválidos detectados correctamente: {invalid_passed}/{invalid_total}")
print("\n🏁 Testeo completado")
