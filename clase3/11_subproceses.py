import subprocess

p = subprocess.run(["python.exe", "-v"], capture_output=True, encoding="cp850") #windows = cp8550
print(f"La salida es {p.stderr}")#imprime el error que devuelve python al ejecutar el script
print(f"retorno: {p.returncode}")#retorna 0 si todo salio bien, si no retorna el codigo de error