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

# Label for Pokémon Name input
lbl_name = ttk.Label(frm_input, text="Pokémon Name:")
lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

# Entry field for user input
ent_name = ttk.Entry(frm_input, width=20)
ent_name.grid(row=0, column=1, padx=(5, 10), pady=10)

# Button to fetch Pokémon info
btn_get_info = ttk.Button(frm_input, text="Get Info", command=handle_btn_get_info)
btn_get_info.grid(row=0, column=2, padx=(5, 10), pady=10)

# Info frame
lblfrm_info = ttk.LabelFrame(root, text="Info")
lblfrm_info.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="n")

# Height Label
lbl_height = ttk.Label(lblfrm_info, text="Height:")
lbl_height.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="e")

lbl_height_val = ttk.Label(lblfrm_info, width=20)
lbl_height_val.grid(row=0, column=1, padx=(0, 10), pady=(10, 5), sticky="w")

# Weight Label
lbl_weight = ttk.Label(lblfrm_info, text="Weight:")
lbl_weight.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="e")

lbl_weight_val = ttk.Label(lblfrm_info)
lbl_weight_val.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="w")

# Types Label (Added based on the instruction)
lbl_types = ttk.Label(lblfrm_info, text="Types:")
lbl_types.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="e")

lbl_types_val = ttk.Label(lblfrm_info, width=20)
lbl_types_val.grid(row=2, column=1, padx=(0, 10), pady=5, sticky="w")

# Stats frame
lblfrm_stats = ttk.LabelFrame(root, text="Stats")
lblfrm_stats.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky="n")

# HP Label and Progress Bar
lbl_hp = ttk.Label(lblfrm_stats, text="HP:")
lbl_hp.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="e")

bar_hp = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_hp.grid(row=0, column=1, padx=(0, 10), pady=(10, 5))

# Attack Label and Progress Bar
lbl_attack = ttk.Label(lblfrm_stats, text="Attack:")
lbl_attack.grid(row=1, column=0, padx=(10, 5), pady=5, sticky="e")

bar_attack = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_attack.grid(row=1, column=1, padx=(0, 10), pady=5)

# Defense Label and Progress Bar
lbl_defense = ttk.Label(lblfrm_stats, text="Defense:")
lbl_defense.grid(row=2, column=0, padx=(10, 5), pady=5, sticky="e")

bar_defense = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_defense.grid(row=2, column=1, padx=(0, 10), pady=5)

# Special Attack Label and Progress Bar
lbl_special_attack = ttk.Label(lblfrm_stats, text="Special Attack:")
lbl_special_attack.grid(row=3, column=0, padx=(10, 5), pady=5, sticky="e")

bar_special_attack = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_special_attack.grid(row=3, column=1, padx=(0, 10), pady=5)

# Special Defense Label and Progress Bar
lbl_special_defense = ttk.Label(lblfrm_stats, text="Special Defense:")
lbl_special_defense.grid(row=4, column=0, padx=(10, 5), pady=5, sticky="e")

bar_special_defense = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_special_defense.grid(row=4, column=1, padx=(0, 10), pady=5)

# Speed Label and Progress Bar
lbl_speed = ttk.Label(lblfrm_stats, text="Speed:")
lbl_speed.grid(row=5, column=0, padx=(10, 5), pady=5, sticky="e")

bar_speed = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_speed.grid(row=5, column=1, padx=(0, 10), pady=5)

# Run the main event loop
root.mainloop()
