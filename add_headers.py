#!/usr/bin/env python3
import os
import re
import sys
from datetime import datetime

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

def process_directory(directory, remove=False):
    """Parcourt récursivement le répertoire pour traiter les fichiers."""
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            process_file(filepath, remove)

def print_usage():
    print("Usage:")
    print("  Pour ajouter des en-têtes:    python add_headers.py [chemin_dossier]")
    print("  Pour supprimer les en-têtes:  python add_headers.py remove [chemin_dossier]")
    print("\nSi le chemin du dossier n'est pas spécifié, le dossier courant sera utilisé.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "help":
        print_usage()
        sys.exit(0)
        
    # Détermine si nous sommes en mode suppression
    remove_mode = False
    target_dir = "."
    
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "remove":
            remove_mode = True
            if len(sys.argv) > 2:
                target_dir = sys.argv[2]
        else:
            target_dir = sys.argv[1]
    
    # Vérifie si le dossier existe
    if not os.path.exists(target_dir):
        print(f"Le répertoire {target_dir} n'existe pas!")
        sys.exit(1)
        
    action = "Suppression" if remove_mode else "Ajout"
    print(f"{action} des en-têtes dans {target_dir}...")
    process_directory(target_dir, remove_mode)
    print("Terminé!")