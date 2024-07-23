from books.models import Genre
import os
import django

# Configura el entorno de Django
# Reemplaza con el nombre de tu módulo de configuración
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookcrud.settings')
django.setup()

# Importa los modelos y realiza la operación deseada


def run_script():
    # Crear e insertar un nuevo género
    b = Genre(genre='Fantasy')
    b.save()
    print("Genre 'Fantasy' created successfully!")


if __name__ == "__main__":
    run_script()
