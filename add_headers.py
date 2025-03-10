#!/usr/bin/env python3
import os
import re
import sys
from datetime import datetime

# Dossiers et fichiers à exclure par défaut
EXCLUDED_DIRS = {'node_modules', '.git', 'dist', 'build'}
EXCLUDED_FILES = {'.DS_Store', 'Thumbs.db', '*.pyc', '*.pyo', '*.pyd', '*.so'}

def should_process_path(path):
    """Vérifie si le chemin doit être traité ou ignoré."""
    # Vérifie si le chemin contient un dossier exclu
    for excluded_dir in EXCLUDED_DIRS:
        if excluded_dir in path.split(os.sep):
            return False
            
    # Vérifie si le fichier correspond à un pattern exclu
    filename = os.path.basename(path)
    for excluded_pattern in EXCLUDED_FILES:
        if re.match(excluded_pattern.replace('*', '.*'), filename):
            return False
            
    return True

def get_file_header(file_ext, filename):
    """Génère l'en-tête de commentaire court sur une ligne."""
    date = datetime.now().strftime("%d/%m/%Y")
    
    # Pour les fichiers HTML
    if file_ext == '.html':
        return f'<!-- {filename} | E-commerce Team | {date} -->\n\n'
    
    # Pour tous les autres types de fichiers
    return f'/* {filename} | E-commerce Team | {date} */\n\n'

def has_header(content, file_ext):
    """Vérifie si le fichier a déjà un en-tête de commentaire."""
    if file_ext == '.html':
        return bool(re.match(r'<!--.*?-->', content))
    return bool(re.match(r'/\*.*?\*/', content))

def remove_header(content, file_ext):
    """Supprime l'en-tête de commentaire du fichier."""
    if file_ext == '.html':
        return re.sub(r'<!--.*?-->\s*', '', content, count=1)
    return re.sub(r'/\*.*?\*/\s*', '', content, count=1)

def process_file(filepath, remove=False):
    """Traite un fichier en ajoutant ou supprimant l'en-tête selon le mode."""
    if not should_process_path(filepath):
        return

    _, ext = os.path.splitext(filepath)
    filename = os.path.basename(filepath)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if remove:
            if has_header(content, ext):
                new_content = remove_header(content, ext)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"En-tête supprimé de {filename}")
            else:
                print(f"Pas d'en-tête trouvé dans {filename}")
        else:
            if has_header(content, ext):
                print(f"Le fichier {filename} a déjà un en-tête")
                return
                
            header = get_file_header(ext, filename)
            new_content = header + content
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"En-tête ajouté à {filename}")
            
    except Exception as e:
        print(f"Erreur lors du traitement de {filename}: {str(e)}")

def process_path(path, remove=False):
    """Traite un chemin qui peut être un fichier ou un dossier."""
    if os.path.isfile(path):
        process_file(path, remove)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                filepath = os.path.join(root, file)
                process_file(filepath, remove)

def print_usage():
    print("Usage:")
    print("  Pour ajouter des en-têtes:")
    print("    python add_headers.py chemin1 [chemin2 ...]")
    print("    Exemple: python add_headers.py store/src store-storefront/src store/package.json")
    print("\n  Pour supprimer les en-têtes:")
    print("    python add_headers.py remove chemin1 [chemin2 ...]")
    print("\nNote: Les dossiers node_modules, .git, dist, build sont exclus automatiquement")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "help":
        print_usage()
        sys.exit(0)
        
    # Détermine si nous sommes en mode suppression
    remove_mode = False
    paths = []
    
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "remove":
            remove_mode = True
            paths = sys.argv[2:]
        else:
            paths = sys.argv[1:]
    
    if not paths:
        print("Erreur: Aucun chemin spécifié!")
        print_usage()
        sys.exit(1)
    
    # Vérifie si les chemins existent
    invalid_paths = [p for p in paths if not os.path.exists(p)]
    if invalid_paths:
        print("Erreur: Les chemins suivants n'existent pas:")
        for p in invalid_paths:
            print(f"  - {p}")
        sys.exit(1)
        
    action = "Suppression" if remove_mode else "Ajout"
    print(f"{action} des en-têtes...")
    
    for path in paths:
        print(f"\nTraitement de {path}...")
        process_path(path, remove_mode)
    
    print("\nTerminé!")

        # Utilisation du script :

# Ajouter des en-têtes dans un dossier spécifique :
# python python .\add_headers.py store\src
# Supprimer les en-têtes :
# python add_headers.py remove store\src store-storefront\src
# Utiliser le dossier courant :
# python add_headers.py


# python .\add_headers.py store\src store-storefront\src store\.medusa store\prisma\schema.prisma store\src store\static store\instrumentation.ts store\medusa-config.ts store\package.json store\tsconfig.json store-storefront\.prettierrc store-storefront\.eslintrc.js store-storefront\check-env-variables.js store-storefront\next-env.d.ts store-storefront\next-sitemap.js store-storefront\next.config.js store-storefront\package.json store-storefront\postcss.config.js store-storefront\tailwind.config.js store-storefront\tsconfig.json





# python .\add_headers.py remove store\src store-storefront\src store\.medusa store\prisma\schema.prisma store\src store\static store\instrumentation.ts store\medusa-config.ts store\package.json store\tsconfig.json store-storefront\.prettierrc store-storefront\.eslintrc.js store-storefront\check-env-variables.js store-storefront\next-env.d.ts store-storefront\next-sitemap.js store-storefront\next.config.js store-storefront\package.json store-storefront\postcss.config.js store-storefront\tailwind.config.js store-storefront\tsconfig.json
