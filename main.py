
import subprocess

from pathlib import Path


def find_folders():
    """Scanne tous les dossiers contenant des fichiers .py."""
    root_path = Path(__file__).parent
    folders = []
    
    for folder in sorted(root_path.iterdir()):
        if folder.is_dir() and not folder.name.startswith('.'):
            folder_files = list(folder.glob("*.py"))
            if folder_files:
                folders.append(folder)
    
    return folders


def find_python_files_in_folder(folder_path):
    """Retourne la liste des fichiers .py dans un dossier."""
    return sorted(folder_path.glob("*.py"))


def display_folder_menu(folders):
    """Affiche le menu des dossiers disponibles."""
    print("\n" + "="*50)
    print("LANCEUR D'APPLICATIONS DASH")
    print("="*50)
    print("\nSélectionnez un dossier :\n")
    
    for idx, folder in enumerate(folders, 1):
        print(f"[{idx}] {folder.name}")
    
    print(f"\n[0] Quitter")
    print("="*50)


def display_file_menu(folder_name, files):
    """Affiche le menu des fichiers dans un dossier."""
    print("\n" + "="*50)
    print(f"DOSSIER: {folder_name}")
    print("="*50)
    print("\n[0] ← Retour aux dossiers\n")
    
    for idx, file in enumerate(files, 1):
        print(f"[{idx}] {file.name}")
    
    print("="*50)


def run_app(file_path):
    """Lance l'application Python spécifiée."""
    print(f"\n🚀 Lancement de {file_path.name}...\n")
    
    try:
        # Lance le processus sans bloquer
        process = subprocess.Popen(
            ["uv", "run", str(file_path)],
            cwd=str(file_path.parent)
        )
        
    except KeyboardInterrupt:
        print("\n⏸️  Application arrêtée par l'utilisateur")
        process.terminate()
    except Exception as e:
        print(f"\n❌ Erreur lors du lancement: {e}")


def main():
    """Fonction principale du lanceur."""
    while True:
        folders = find_folders()
        
        if not folders:
            print("❌ Aucun dossier avec des fichiers Python trouvé.")
            break
        
        display_folder_menu(folders)
        
        try:
            choice = input("\nSélectionnez un dossier (numéro): ").strip()
            
            if choice == "0":
                print("Au revoir!")
                break
            
            folder_idx = int(choice) - 1
            
            if 0 <= folder_idx < len(folders):
                selected_folder = folders[folder_idx]
                
                # Sous-menu des fichiers
                while True:
                    files = find_python_files_in_folder(selected_folder)
                    
                    if not files:
                        print("❌ Aucun fichier Python dans ce dossier.")
                        break
                    
                    display_file_menu(selected_folder.name, files)
                    
                    file_choice = input("\nSélectionnez un fichier (numéro): ").strip()
                    
                    if file_choice == "0":
                        break  # Retour au menu des dossiers
                    
                    file_idx = int(file_choice) - 1
                    
                    if 0 <= file_idx < len(files):
                        run_app(files[file_idx])
                        return  # Arrête le programme après le lancement
                        
                    else:
                        print("❌ Choix invalide. Veuillez réessayer.")
            else:
                print("❌ Choix invalide. Veuillez réessayer.")
        
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")
        except KeyboardInterrupt:
            print("\n\nAu revoir!")
            break


if __name__ == "__main__":
    main()
