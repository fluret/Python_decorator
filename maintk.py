import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk


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


def run_app(file_path):
    """Lance l'application Python spécifiée."""
    try:
        subprocess.Popen(
            ["uv", "run", str(file_path)],
            cwd=str(file_path.parent)
        )
        return True
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du lancement: {e}")
        return False


class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lanceur d'Applications Python")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        self.folders = find_folders()
        self.selected_folder = None
        
        # Frame principal
        main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titre
        title = tk.Label(
            main_frame, 
            text="🚀 Lanceur d'Applications Python",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title.pack(pady=(0, 20))
        
        # Frame pour les dossiers
        folder_frame = tk.LabelFrame(
            main_frame, 
            text="Dossiers disponibles",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            padx=10,
            pady=10
        )
        folder_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Listbox pour les dossiers
        self.folder_listbox = tk.Listbox(
            folder_frame,
            font=("Arial", 10),
            bg="white",
            selectmode=tk.SINGLE,
            height=8
        )
        self.folder_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.folder_listbox.bind("<<ListboxSelect>>", self.on_folder_select)
        
        # Scrollbar pour les dossiers
        folder_scrollbar = tk.Scrollbar(folder_frame, orient=tk.VERTICAL)
        folder_scrollbar.config(command=self.folder_listbox.yview)
        folder_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.folder_listbox.config(yscrollcommand=folder_scrollbar.set)
        
        # Remplir la liste des dossiers
        for folder in self.folders:
            self.folder_listbox.insert(tk.END, folder.name)
        
        # Frame pour les fichiers
        file_frame = tk.LabelFrame(
            main_frame,
            text="Scripts Python",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            padx=10,
            pady=10
        )
        file_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Listbox pour les fichiers
        self.file_listbox = tk.Listbox(
            file_frame,
            font=("Arial", 10),
            bg="white",
            selectmode=tk.SINGLE,
            height=8
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.file_listbox.bind("<Double-Button-1>", self.on_file_double_click)
        
        # Scrollbar pour les fichiers
        file_scrollbar = tk.Scrollbar(file_frame, orient=tk.VERTICAL)
        file_scrollbar.config(command=self.file_listbox.yview)
        file_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=file_scrollbar.set)
        
        # Frame pour les boutons
        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(fill=tk.X)
        
        # Bouton Lancer
        launch_btn = tk.Button(
            button_frame,
            text="▶ Lancer",
            command=self.launch_selected,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        launch_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Bouton Quitter
        quit_btn = tk.Button(
            button_frame,
            text="✕ Quitter",
            command=root.quit,
            font=("Arial", 11),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        quit_btn.pack(side=tk.RIGHT)
        
        # Message si aucun dossier
        if not self.folders:
            messagebox.showwarning(
                "Aucun dossier",
                "Aucun dossier avec des fichiers Python trouvé."
            )
    
    def on_folder_select(self, event):
        """Appelé quand un dossier est sélectionné."""
        selection = self.folder_listbox.curselection()
        if selection:
            folder_idx = selection[0]
            self.selected_folder = self.folders[folder_idx]
            self.update_file_list()
    
    def update_file_list(self):
        """Met à jour la liste des fichiers."""
        self.file_listbox.delete(0, tk.END)
        
        if self.selected_folder:
            files = find_python_files_in_folder(self.selected_folder)
            for file in files:
                self.file_listbox.insert(tk.END, file.name)
    
    def on_file_double_click(self, event):
        """Appelé quand un fichier est double-cliqué."""
        self.launch_selected()
    
    def launch_selected(self):
        """Lance le script sélectionné."""
        file_selection = self.file_listbox.curselection()
        
        if not self.selected_folder:
            messagebox.showwarning(
                "Aucune sélection",
                "Veuillez d'abord sélectionner un dossier."
            )
            return
        
        if not file_selection:
            messagebox.showwarning(
                "Aucune sélection",
                "Veuillez sélectionner un script à lancer."
            )
            return
        
        file_idx = file_selection[0]
        files = find_python_files_in_folder(self.selected_folder)
        selected_file = files[file_idx]
        
        if run_app(selected_file):
            messagebox.showinfo(
                "Lancement réussi",
                f"Le script '{selected_file.name}' a été lancé."
            )
            self.root.quit()


def main():
    """Fonction principale du lanceur."""
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
