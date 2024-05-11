import tkinter as tk
from tkinter import messagebox
from collections import Counter
import string
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def analyze_text():
    text = text_input.get("1.0", tk.END).upper()
    # Count letters only
    letters = [ch for ch in text if ch in string.ascii_uppercase]
    frequency = Counter(letters)
    total_letters = sum(frequency.values())

    # Sort the frequency dictionary by frequency count in descending order
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Prepare data for display
    top_five = sorted_freq[:5]
    results = []
    labels = ['E', 'T', 'A', 'I', 'O']
    data_labels = []
    data_values = []

    for i, (letter, count) in enumerate(top_five):
        if i < len(labels):
            percentage = (count / total_letters) * 100 if total_letters > 0 else 0
            results.append(f"{labels[i]} ({letter}): {percentage:.2f}%")
            data_labels.append(f"{labels[i]} ({letter})")
            data_values.append(percentage)

    # Update results display
    results_output.config(state=tk.NORMAL)
    results_output.delete("1.0", tk.END)
    results_output.insert("1.0", "\n".join(results))
    results_output.config(state=tk.DISABLED)
    
    # Display the bar chart with customizations
    show_bar_chart(data_labels, data_values)

def show_bar_chart(labels, values):
    fig, ax = plt.subplots(figsize=(8, 6))  # Adjust the figure size
    ax.bar(labels, values, color='skyblue', edgecolor='black', linewidth=1.5)  # Custom bar color and edge
    ax.set_xlabel('Letters', fontsize=12)  # Customize axis label font size
    ax.set_ylabel('Percentage', fontsize=12)
    ax.set_title('Top 5 Letter Frequencies', fontsize=14)  # Customize title font size

    # Customize background color and grid
    ax.set_facecolor('#f9f9f9')  # Light gray background
    ax.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines

    # Integrate matplotlib into tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title("Letter Frequency Analyzer")

# Create a text input area
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=10)

# Create a button to trigger analysis
analyze_button = tk.Button(root, text="Analyze Frequencies", command=analyze_text)
analyze_button.pack(pady=10)

# Create an output area for the results
results_output = tk.Text(root, height=7, width=50, state=tk.DISABLED)
results_output.pack(pady=10)

# Start the GUI event loop
root.mainloop()
