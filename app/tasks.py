from app.app import celery
from subprocess import Popen, PIPE

@celery.task(name="report", acks_late=True)
def report():
    script_path = "<ruta_del_script>/nombre_del_script.py"  # Reemplaza "<ruta_del_script>" con la ruta real del script

    process = Popen(["python", script_path], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print("Error al ejecutar el script:")
        print(stderr.decode())
        return {"state": "error"}

    return {"state": "completed"}
