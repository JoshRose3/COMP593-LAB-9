from tkinter import Tk, ttk, messagebox
import requests

# Function to fetch Pokémon data from the PokeAPI
def get_pokemon_info(poke_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_name.lower()}/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for non-2xx responses
        return response.json()
    except requests.exceptions.RequestException:
        return None  # Return None if there is an error

# Function to handle button click event
def handle_btn_get_info():
    poke_name = ent_name.get()
    poke_info = get_pokemon_info(poke_name)

    if poke_info:
        # Info Section
        lbl_height_val['text'] = str(poke_info['height']) + ' dm'
        lbl_weight_val['text'] = str(poke_info['weight']) + ' hg'

        # Display Pokémon types (handling 1 or 2 types)
        types = [type_info['type']['name'] for type_info in poke_info['types']]
        lbl_types_val['text'] = ', '.join(types)

        # Stats Section
        bar_hp['value'] = poke_info['stats'][0]['base_stat']  # HP
        bar_attack['value'] = poke_info['stats'][1]['base_stat']  # Attack
        bar_defense['value'] = poke_info['stats'][2]['base_stat']  # Defense
        bar_special_attack['value'] = poke_info['stats'][3]['base_stat']  # Special Attack
        bar_special_defense['value'] = poke_info['stats'][4]['base_stat']  # Special Defense
        bar_speed['value'] = poke_info['stats'][5]['base_stat']  # Speed
    else:
        # Show error message dialog if Pokémon not found
        messagebox.showerror("Error", f"Pokémon '{poke_name}' not found. Please try again.")

# Create the main window
root = Tk()
root.title("Pokémon Information Viewer")
root.geometry("600x400")  # Set a default window size

# Create the User Input Frame
frm_input = ttk.Frame(root)
frm_input.grid(row=0, column=0, columnspan=2, pady=(20, 10))

# Label for Pokémon Name input
lbl_name = ttk.Label(frm_input, text="Pokémon Name:")
lbl_name.grid(row=0, column=0, padx=(10, 5), pady=10)

# Entry field for user input
ent_name = ttk.Entry(frm_input, width=20)
ent_name.grid(row=0, column=1, padx=(5, 10), pady=10)

# Button to fetch Pokémon info
btn_get_info = ttk.Button(frm_input, text="Get Info", command=handle_btn_get_info)
btn_get_info.grid(row=0, column=2, padx=(5, 10), pady=10)

# Info Frame
lblfrm_info = ttk.LabelFrame(root, text="Info")
lblfrm_info.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky='N')
lbl_height = ttk.Label(lblfrm_info, text="Height:")
lbl_height.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky='E')
lbl_height_val = ttk.Label(lblfrm_info, width=20)
lbl_height_val.grid(row=0, column=1, padx=(0, 10), pady=(10, 5), sticky='W')
lbl_weight = ttk.Label(lblfrm_info, text="Weight:")
lbl_weight.grid(row=1, column=0, padx=(10, 5), pady=5, sticky='E')
lbl_weight_val = ttk.Label(lblfrm_info, width=20)
lbl_weight_val.grid(row=1, column=1, padx=(0, 10), pady=5, sticky='W')
lbl_types = ttk.Label(lblfrm_info, text="Types:")
lbl_types.grid(row=2, column=0, padx=(10, 5), pady=(10, 5), sticky='E')
lbl_types_val = ttk.Label(lblfrm_info, width=20)
lbl_types_val.grid(row=2, column=1, padx=(0, 10), pady=(10, 5), sticky='W')

# Stats Frame
lblfrm_stats = ttk.LabelFrame(root, text="Stats")
lblfrm_stats.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky='N')
lbl_hp = ttk.Label(lblfrm_stats, text="HP:")
lbl_hp.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky='E')
bar_hp = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_hp.grid(row=0, column=1, padx=(0, 10), pady=(10, 5))
lbl_attack = ttk.Label(lblfrm_stats, text="Attack:")
lbl_attack.grid(row=1, column=0, padx=(10, 5), pady=5, sticky='E')
bar_attack = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_attack.grid(row=1, column=1, padx=(0, 10), pady=5)
lbl_defense = ttk.Label(lblfrm_stats, text="Defense:")
lbl_defense.grid(row=2, column=0, padx=(10, 5), pady=5, sticky='E')
bar_defense = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_defense.grid(row=2, column=1, padx=(0, 10), pady=5)
lbl_special_attack = ttk.Label(lblfrm_stats, text="Special Attack:")
lbl_special_attack.grid(row=3, column=0, padx=(10, 5), pady=5, sticky='E')
bar_special_attack = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_special_attack.grid(row=3, column=1, padx=(0, 10), pady=5)
lbl_special_defense = ttk.Label(lblfrm_stats, text="Special Defense:")
lbl_special_defense.grid(row=4, column=0, padx=(10, 5), pady=5, sticky='E')
bar_special_defense = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_special_defense.grid(row=4, column=1, padx=(0, 10), pady=5)
lbl_speed = ttk.Label(lblfrm_stats, text="Speed:")
lbl_speed.grid(row=5, column=0, padx=(10, 5), pady=5, sticky='E')
bar_speed = ttk.Progressbar(lblfrm_stats, length=200, maximum=255.0)
bar_speed.grid(row=5, column=1, padx=(0, 10), pady=5)

# Run the main event loop
root.mainloop()
