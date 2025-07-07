# importing Tkinter
import tkinter as tk
# importing Themed Tkinter
from tkinter import ttk
# importing pandas
import pandas as pd

all_teams = pd.read_csv("Opponents.csv")

# function for when user clicks the button on the pop-up window
def on_button_click():
    # message in the original pop-up window once the button is game_info_clicked
    label.config(text="Data Loaded!")

    # Upload the DataFrame
    df = pd.read_csv("Opponents.csv")

    # Create a new window to display the DataFrame
    df_window = tk.Toplevel(run_it)
    # give the new window a title to display
    df_window.title("Test")

    # Create a Treeview widget to display the DataFrame
    tree = ttk.Treeview(df_window, columns=list(df.columns), show='headings')

    # Add columns to the Treeview
    for col in df.columns:
        # set the column heading text for the specified column
        tree.heading(col, text=col)
        # centering the text in each column
        tree.column(col, anchor='center')

    # Insert data into the Treeview
    for i, row in df.iterrows():
        # insert a new row at the end of values of list 'row'
        tree.insert("", "end", values=list(row))

    # create a vertical scrollbar widget
    vsb = ttk.Scrollbar(df_window, orient="vertical", command=tree.yview)
    # Enable the scrollbar, positioned above the data here to ensure the
    # scrollbar will be at the side of the data shown
    tree.configure(yscrollcommand=vsb.set)

    # display the scrollbar
    vsb.pack(side="right", fill="y")
    # display the Treeview
    tree.pack(fill='y', expand=True, padx=10, pady=10)


def game_info_clicked(value):
    if value:
        label.config(text=f"Entering {value} Data")
        opp_info_label.config(text="Enter Opponent ID\neg. SEA", pady=5)
        opp_info_label.pack(pady=10)
        chi_input.forget()
        sea_input.forget()
        opponent_entry.pack(pady=15)
        back_button.pack()
        entry = opponent_entry.get()
        if entry.isalpha():
            label.config(text="Found!")


def data_input():
    label.config(text="Which team are you inputting data for?")
    chi_input.pack(pady=10)
    sea_input.pack(pady=10)
    show_button.forget()
    data_input_button.forget()
    back_button.forget()
    opponent_entry.forget()
    opp_info_label.forget()


# Create the main window
run_it = tk.Tk()
# Title for main window
run_it.title("Files")

# Create a label
label = tk.Label(run_it, text="Enter")
opp_info_label = tk.Label(run_it, text="Enter")
# display the label with 10 pixels of padding
label.pack(pady=10)


# Create a button to open the stored data
show_button = tk.Button(run_it, text="Click to Show DataFrame", command=on_button_click)
data_input_button = tk.Button(run_it, text="Add Game Info", command=data_input)
# display the button with 10 pixels of padding
show_button.pack(pady=10)
data_input_button.pack(pady=10)

# Buttons for entering each teams data
chi_input = tk.Button(run_it, text="Chicago", command=lambda: game_info_clicked("Chicago"))
sea_input = tk.Button(run_it, text="Seattle", command=lambda: game_info_clicked("Seattle"))
opponent_entry = tk.Entry(run_it, validate="key", validatecommand=(run_it.register(lambda text: len(text) <= 4), "%P"))
back_button = tk.Button(run_it, text="Cancel Entry", command=data_input)
back_button.forget()

# Start the Tkinter event loop
run_it.mainloop()
