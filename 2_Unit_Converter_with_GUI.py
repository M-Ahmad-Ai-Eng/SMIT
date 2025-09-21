import tkinter as tk
from tkinter import ttk, messagebox
import random

# Funny messages per category
jokes = {
    "length": [
        "Bro, you just stretched those units farther than my patience.",
        "Converted length? Now go stretch your legs, you’ve been sitting too long.",
        "Bro’s measuring game is stronger than my WiFi signal.",
        "That’s longer than the line at Taco Bell on a Friday night.",
        "You just made meters jealous of centimeters, bro.",
    ],
    "mass": [
        "You converted mass like you’re bench-pressing math problems.",
        "Bro, that conversion’s heavier than my Sunday regrets.",
        "Mass to mega mass? You just leveled up to ‘Hulk Mode.’",
        "You just turned grams into gains, bro. Flex those numbers!",
        "Bro’s so heavy on conversions, he’s practically a black hole.",
    ],
    "time": [
        "You just converted time faster than my excuses for skipping gym.",
        "Bro, time’s ticking and so is your conversion skill.",
        "That took less time than me deciding what to eat.",
        "You just made seconds jealous of minutes, bro.",
        "You converted time better than I convert bad vibes to good.",
    ],
    "temperature": [
        "You just turned up the heat and froze the haters.",
        "Bro, your conversions are fire — literally and figuratively.",
        "That temperature conversion? Cooler than my ex’s heart.",
        "Bro’s Celsius to Fahrenheit skills are hotter than summer.",
        "You just made Kelvin look basic, bro.",
    ],
    "current": [
        "Bro, you just powered up like an electric superhero.",
        "Your conversion is so lit, even Tesla’s texting you.",
        "You’ve got more amps than my party playlist.",
        "Bro just shocked the system — no outlet needed.",
        "That conversion’s got more juice than my morning coffee.",
    ],
    "currency": [
        "Bro just made it rain… numbers, that is.",
        "You converted cash like you’re the CEO of the digital bank.",
        "Bro’s currency game is so strong, even Scrooge McDuck is jealous.",
        "That conversion’s more profitable than my fantasy football team.",
        "You just leveled up to ‘Currency Conqueror.’",
    ]
}

# Conversion functions
def convert_length(choice, value):
    if choice == 1:  # cm to m
        return value / 100, "m"
    elif choice == 2:  # m to km
        return value / 1000, "km"
    elif choice == 3:  # km to Mm
        return value / 1000, "Mm"
    elif choice == 4:  # Mm to Gm
        return value / 1000, "Gm"

def convert_mass(choice, value):
    if choice == 1:  # mg to g
        return value / 1000, "g"
    elif choice == 2:  # g to kg
        return value / 1000, "kg"
    elif choice == 3:  # kg to t
        return value / 1000, "t"
    elif choice == 4:  # t to Mt
        return value / 1000000, "Mt"

def convert_time(choice, value):
    if choice == 1:  # ms to s
        return value / 1000, "s"
    elif choice == 2:  # s to min
        return value / 60, "min"
    elif choice == 3:  # min to h
        return value / 60, "h"
    elif choice == 4:  # h to d
        return value / 24, "d"

def convert_temperature(choice, value):
    if choice == 1:  # C to F
        return (value * 9/5) + 32, "°F"
    elif choice == 2:  # F to K
        return (value - 32) * 5/9 + 273.15, "K"
    elif choice == 3:  # K to C
        return value - 273.15, "°C"
    elif choice == 4:  # F to C
        return (value - 32) * 5/9, "°C"

def convert_current(choice, value):
    if choice == 1:  # mA to A
        return value / 1000, "A"
    elif choice == 2:  # A to kA
        return value / 1000, "kA"
    elif choice == 3:  # kA to MA
        return value / 1000, "MA"
    elif choice == 4:  # MA to GA
        return value / 1000, "GA"

def convert_currency(choice, value):
    if choice == 1:  # USD to PKR
        return value * 281.55, "Rs"
    elif choice == 2:  # SAR to PKR
        return value * 75.05, "Rs"
    elif choice == 3:  # INR to PKR
        return value * 3.19, "Rs"
    elif choice == 4:  # KWD to PKR
        return value * 922.12, "Rs"
    elif choice == 5:  # AFN to PKR
        return value * 4.08, "Rs"

# GUI Setup
root = tk.Tk()
root.title("Professional Unit Converter")
root.geometry("700x550")
root.minsize(600, 500)

# Fonts and colors
FONT_LARGE = ("Arial", 18, "bold")
FONT_MEDIUM = ("Arial", 14)
FONT_SMALL = ("Arial", 12)
BTN_BG = "#1e90ff"
BTN_ACTIVE_BG = "#104e8b"
BTN_FG = "white"

# Main Frame
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Title Label
title_lbl = ttk.Label(main_frame, text="Unit Converter", font=("Arial", 26, "bold"))
title_lbl.pack(pady=(0, 20))

# Variable to track selected main category
selected_category = tk.StringVar(value="")

# Dropdown for main categories
categories = [
    "Length",
    "Mass",
    "Time",
    "Temperature",
    "Current",
    "Currency"
]

# Sub-unit options dictionary
sub_units_options = {
    "Length": ["CentiMeter(cm) to Meter(m)", "Meter(m) to KiloMeter(km)", "KiloMeter(km) to MegaMeter(Mm)", "MegaMeter(Mm) to GigaMeter(Gm)"],
    "Mass": ["MilliGram(mg) to Gram(g)", "Gram(g) to KiloGram(kg)", "KiloGram(kg) to Tonne(t)", "Tonne(t) to MegaTonne(Mt)"],
    "Time": ["MilliSecond(ms) to Second(s)", "Second(s) to Minutes(min)", "Minutes(min) to Hour(h)", "Hour(h) to Day(d)"],
    "Temperature": ["Celsius(°C) to Fahrenheit(°F)", "Fahrenheit(°F) to Kelvin(K)", "Kelvin(K) to Celsius(°C)", "Fahrenheit(°F) to Celsius(°C)"],
    "Current": ["Milliampere(mA) to Ampere(A)", "Ampere(A) to KiloAmpere(kA)", "KiloAmpere(kA) to MegaAmpere(MA)", "MegaAmpere(MA) to GigaAmpere(GA)"],
    "Currency": ["USD to PKR", "SAR to PKR", "INR to PKR", "KWD to PKR", "AFN to PKR"]
}

# Category dropdown UI
category_label = ttk.Label(main_frame, text="Select Unit Category:", font=FONT_MEDIUM)
category_label.pack(anchor="w")

category_combo = ttk.Combobox(main_frame, values=categories, state="readonly", font=FONT_MEDIUM)
category_combo.pack(fill="x", pady=10)

# Sub-unit dropdown (will update based on category)
subunit_label = ttk.Label(main_frame, text="Select Conversion Type:", font=FONT_MEDIUM)
subunit_label.pack(anchor="w", pady=(10, 0))

subunit_combo = ttk.Combobox(main_frame, values=[], state="readonly", font=FONT_MEDIUM)
subunit_combo.pack(fill="x", pady=10)

# Input frame for value
input_label = ttk.Label(main_frame, text="Enter Value to Convert:", font=FONT_MEDIUM)
input_label.pack(anchor="w", pady=(20, 0))

value_entry = tk.Text(main_frame, height=2, font=FONT_MEDIUM, wrap="word")
value_entry.pack(fill="x", pady=5)

# Result display
result_label = ttk.Label(main_frame, text="Result:", font=FONT_MEDIUM)
result_label.pack(anchor="w", pady=(20, 0))

result_display = tk.Text(main_frame, height=4, font=FONT_MEDIUM, bg="#f0f0f0", state="disabled")
result_display.pack(fill="both", pady=5)

# Function to update subunits when category changes
def on_category_change(event):
    category = category_combo.get()
    subunit_combo['values'] = sub_units_options.get(category, [])
    subunit_combo.set('')
    result_display.config(state="normal")
    result_display.delete("1.0", tk.END)
    result_display.config(state="disabled")
    value_entry.delete("1.0", tk.END)

category_combo.bind("<<ComboboxSelected>>", on_category_change)

# Conversion button action
def on_convert():
    category = category_combo.get()
    subunit_index = subunit_combo.current()
    raw_value = value_entry.get("1.0", tk.END).strip()

    if not category:
        messagebox.showerror("Error", "Please select a unit category.")
        return
    if subunit_index == -1:
        messagebox.showerror("Error", "Please select a conversion type.")
        return
    if not raw_value:
        messagebox.showerror("Error", "Please enter a value to convert.")
        return

    try:
        value = float(raw_value)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value.")
        return

    # Perform conversion based on category and subunit index
    try:
        if category == "Length":
            result, unit = convert_length(subunit_index+1, value)
            joke = random.choice(jokes["length"])
        elif category == "Mass":
            result, unit = convert_mass(subunit_index+1, value)
            joke = random.choice(jokes["mass"])
        elif category == "Time":
            result, unit = convert_time(subunit_index+1, value)
            joke = random.choice(jokes["time"])
        elif category == "Temperature":
            result, unit = convert_temperature(subunit_index+1, value)
            joke = random.choice(jokes["temperature"])
        elif category == "Current":
            result, unit = convert_current(subunit_index+1, value)
            joke = random.choice(jokes["current"])
        elif category == "Currency":
            # Currency has 5 options, so just pass index+1
            result, unit = convert_currency(subunit_index+1, value)
            joke = random.choice(jokes["currency"])
        else:
            messagebox.showerror("Error", "Invalid category selected.")
            return
    except Exception as e:
        messagebox.showerror("Error", f"Conversion error: {e}")
        return

    # Show result & joke
    result_text = f"Converted Result: {result:.5f} {unit}\n\n💬 Joke: {joke}"
    result_display.config(state="normal")
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, result_text)
    result_display.config(state="disabled")

# Exit button
def on_exit():
    messagebox.showinfo("Goodbye", "Unit Converter signing off... May your measurements always be accurate! جزاک اللہ")
    root.destroy()

# Buttons frame
btn_frame = ttk.Frame(main_frame)
btn_frame.pack(fill="x", pady=20)

# Convert button
convert_btn = tk.Button(
    btn_frame,
    text="Convert",
    font=FONT_LARGE,
    bg=BTN_BG,
    fg=BTN_FG,
    activebackground=BTN_ACTIVE_BG,
    activeforeground=BTN_FG,
    relief="flat",
    padx=20,
    pady=10,
    command=on_convert
)
convert_btn.pack(side="left", expand=True, fill="x", padx=10)

# Exit button
exit_btn = tk.Button(
    btn_frame,
    text="Exit",
    font=FONT_LARGE,
    bg="#d9534f",
    fg=BTN_FG,
    activebackground="#b52b27",
    activeforeground=BTN_FG,
    relief="flat",
    padx=20,
    pady=10,
    command=on_exit
)
exit_btn.pack(side="left", expand=True, fill="x", padx=10)

# Run the app
root.mainloop()
