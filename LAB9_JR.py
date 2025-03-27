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
    # Print the entered Pokémon name
    pokemon_name = ent_name.get()
    print(f"Entered Pokémon Name: {pokemon_name}")

    # Example values for Pokémon (you should replace these with real data from PokeAPI)
    height = "6.5 m"
    weight = "80 kg"
    types = "Fire, Flying"  # Example with two types

    # Update the Info labels with the Pokémon data
    lbl_height_val.config(text=height)
    lbl_weight_val.config(text=weight)
    lbl_types_val.config(text=types)

    # Example stats (replace with data from PokeAPI)
    hp = 150
    attack = 180
    defense = 150
    special_attack = 160
    special_defense = 140
    speed = 120

    # Update the progress bars with stats
    bar_hp["value"] = hp
    bar_attack["value"] = attack
    bar_defense["value"] = defense
    bar_special_attack["value"] = special_attack
    bar_special_defense["value"] = special_defense
    bar_speed["value"] = speed


# Create the main window
root = Tk()
root.title("Pokémon Information Viewer")
root.geometry("600x400")  # Set a default window size

# Create the User Input Frame
frm_input = ttk.Frame(root)
frm_input.grid(row=0, column=0, columnspan=3, pady=(20, 10))
