import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os
import cleanData as cd

class DataCleaningAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Cleaning Assistant")
        self.root.geometry("700x700")
        self.root.configure(bg="white")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header section
        header_frame = tk.Frame(self.root, bg="white", pady=30)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(header_frame, text="Data Cleaning\nAssistant", 
                               font=("Arial", 24, "bold"), bg="white")
        title_label.pack()
        
        subtitle_label = tk.Label(header_frame, text="Clean with ease", 
                                 font=("Arial", 12), fg="gray", bg="white")
        subtitle_label.pack(pady=(5, 20))
        
        # Upload file button
        upload_button = tk.Button(header_frame, text="Upload file", 
                                 bg="#2D2D2D", fg="white", 
                                 font=("Arial", 10),
                                 width=20, height=2,
                                 command=self.upload_file)
        upload_button.pack(pady=10)
        
        # Settings section
        settings_frame = tk.Frame(self.root, bg="white", pady=20, padx=50)
        settings_frame.pack(fill="x", anchor="w")
        
        # Dropdown
        label1 = tk.Label(settings_frame, text="Label", bg="white", anchor="w")
        label1.grid(row=0, column=0, sticky="w", pady=(10, 5))
        
        self.dropdown = ttk.Combobox(settings_frame, values=["Value"], width=25)
        self.dropdown.current(0)
        self.dropdown.grid(row=1, column=0, sticky="w", pady=(0, 15))
        
        # Toggle switches
        # Switch 1
        label2 = tk.Label(settings_frame, text="Label", bg="white", anchor="w")
        label2.grid(row=2, column=0, sticky="w")
        
        desc2 = tk.Label(settings_frame, text="Description", fg="gray", bg="white", anchor="w")
        desc2.grid(row=3, column=0, sticky="w", pady=(0, 15))
        
        self.switch_var1 = tk.BooleanVar()
        switch1 = self.create_switch(settings_frame, self.switch_var1)
        switch1.grid(row=2, column=1, rowspan=2, padx=(50, 0), sticky="e")
        
        # Switch 2
        label3 = tk.Label(settings_frame, text="Label", bg="white", anchor="w")
        label3.grid(row=4, column=0, sticky="w")
        
        desc3 = tk.Label(settings_frame, text="Description", fg="gray", bg="white", anchor="w")
        desc3.grid(row=5, column=0, sticky="w", pady=(0, 15))
        
        self.switch_var2 = tk.BooleanVar()
        switch2 = self.create_switch(settings_frame, self.switch_var2)
        switch2.grid(row=4, column=1, rowspan=2, padx=(50, 0), sticky="e")
        
        # Switch 3
        label4 = tk.Label(settings_frame, text="Label", bg="white", anchor="w")
        label4.grid(row=6, column=0, sticky="w")
        
        desc4 = tk.Label(settings_frame, text="Description", fg="gray", bg="white", anchor="w")
        desc4.grid(row=7, column=0, sticky="w")
        
        self.switch_var3 = tk.BooleanVar()
        switch3 = self.create_switch(settings_frame, self.switch_var3)
        switch3.grid(row=6, column=1, rowspan=2, padx=(50, 0), sticky="e")
        
        # Preview area (gray box)
        self.preview_frame = tk.Frame(self.root, bg="#ECECEC", height=250)
        self.preview_frame.pack(fill="x", padx=50, pady=30)
        
        self.preview_label = tk.Label(self.preview_frame, text="No file selected", 
                                    fg="#AAAAAA", bg="#ECECEC",
                                    font=("Arial", 10))
        self.preview_label.pack(expand=True, fill="both", pady=115)
        
        # Action button
        action_frame = tk.Frame(self.root, bg="white", pady=20)
        action_frame.pack(fill="x")
        
        action_button = tk.Button(action_frame, text="Button", 
                                 bg="#2D2D2D", fg="white", 
                                 font=("Arial", 10),
                                 width=30, height=3)
        action_button.pack(pady=10)
        
    def create_switch(self, parent, variable):
        """Create a custom toggle switch using a Canvas"""
        switch_frame = tk.Frame(parent, bg="white")
        
        # Create a custom toggle switch with Canvas
        switch = tk.Canvas(switch_frame, width=40, height=20, bg="white", 
                          highlightthickness=0)
        switch.pack()
        
        # Draw the switch background
        switch.create_oval(0, 0, 20, 20, fill="#333333", outline="")
        switch.create_oval(20, 0, 40, 20, fill="#333333", outline="")
        switch.create_rectangle(10, 0, 30, 20, fill="#333333", outline="")
        
        # Create the switch knob
        knob = switch.create_oval(2, 2, 18, 18, fill="white", outline="")
        
        def toggle():
            if variable.get():
                # ON state - move knob to right
                switch.coords(knob, 22, 2, 38, 18)
            else:
                # OFF state - move knob to left
                switch.coords(knob, 2, 2, 18, 18)
                
        # Configure the switch to toggle when clicked
        switch.bind("<Button-1>", lambda e: [variable.set(not variable.get()), toggle()])
        
        # Initialize the switch state
        toggle()
        
        return switch_frame
    
    def upload_file(self):
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("CSV files", "*.csv"),
                       ("JSON files", "*.json"),
                       ("SQL files", "*.sql"), 
                      ("Excel files", "*.xlsx"), 
                      ("All files", "*.*"))
        )
        if filename:
            df = cd.DataFrame(filename)
            self.preview_label = ImageTk.PhotoImage(Image.open(df.head_image()))
            print(f"File selected: {filename}")
            # Here you would add code to process the uploaded file
            

if __name__ == "__main__":
    root = tk.Tk()
    app = DataCleaningAssistant(root)
    root.mainloop()