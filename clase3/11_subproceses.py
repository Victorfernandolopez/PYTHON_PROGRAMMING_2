import subprocess

p = subprocess.run(["python.exe", "-v"], capture_output=True, encoding="cp850")
print(f"La salida es {p.stderr}")