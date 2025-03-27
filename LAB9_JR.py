from tkinter import *
from tkinter import ttk
from tkinter import Tk, ttk

def handle_btn_get_info():
    print(f"Entered Pokémon Name: {ent_name.get()}")

def main():
    # Create the main window
    root = Tk()
    root.title("Pokémon Information Viewer")
    root.geometry("400x300")  # Set a default window size
    

    # Create the User Input Frame
    frm_input = ttk.Frame(root)
    frm_input.grid(row=0, column=0, columnspan=2, pady=(20, 10))
    

    # Label for Pokémon Name input
    lbl_name = ttk.Label(frm_input, text="Pokémon Name:")
    lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)
    

    # Entry field for user input
    global ent_name
    ent_name = ttk.Entry(frm_input, width=20)
    ent_name.grid(row=0, column=1, padx=(5, 10), pady=10)
    

    # Button to fetch Pokémon info
    btn_get_info = ttk.Button(frm_input, text="Get Info")
    btn_get_info = ttk.Button(frm_input, text="Get Info", command=handle_btn_get_info)
    btn_get_info.grid(row=0, column=2, padx=(5, 10), pady=10)
    

    # Run the main event loop
    root.mainloop()

# Run the application
main()
if __name__ == "__main__":
    main()
