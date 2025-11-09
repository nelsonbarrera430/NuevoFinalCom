# run_tests.py
import subprocess, os, sys, shutil

tests_dir = os.path.join(os.path.dirname(__file__), "tests")
if not os.path.isdir(tests_dir):
    print("No hay carpeta tests/")
    sys.exit(1)

tests = sorted(os.listdir(tests_dir))
results = []

for t in tests:
    if not t.endswith(".txt"):
        continue
    path = os.path.join(tests_dir, t)
    print("----", t, "----")
    # borrar output_program.py previo
    if os.path.exists("output_program.py"):
        os.remove("output_program.py")

    proc = subprocess.Popen([sys.executable, "main.py", path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    out, _ = proc.communicate(timeout=10)
    print(out)
    success = os.path.exists("output_program.py")
    # heurística: si test filename contiene 'valid' esperamos success True
    expected_valid = "valid" in t.lower()
    ok = (expected_valid and success) or (not expected_valid and (not success))
    results.append((t, ok, expected_valid, success))
    print("Result:", "OK" if ok else "FAIL", "\n")

print("==== Summary ====")
for t, ok, expected_valid, success in results:
    print(f"{t}: {'PASS' if ok else 'FAIL'} (expected valid={expected_valid}, got output={success})")
