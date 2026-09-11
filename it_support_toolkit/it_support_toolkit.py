# Libraries
import tkinter as tk
import subprocess

# Function used by the "Ping Host" button
def start_ping():
        host = host_input.get()
        if host == "":
            result_label.config(text="Please enter a host")
        else:
              result = subprocess.run(["ping", "-n", "1", host], capture_output=True, text=True)
              output.delete("1.0", "end")
              output.insert("1.0", result.stdout)
              result_label.config(text="Ping completed")





# Main window
window = tk.Tk()
window.title("IT Support Toolkit")

# Title
message = tk.Label(window, text ="IT Support Toolkit", bg="#1D1D1D", fg="#377A7A", font=("Arial", 18, "bold"))
message.pack(pady=10)

# Entry field for host
host_input = tk.Entry(window, bg="#1d1d1d", fg = "#0c9eb1", width=50)
host_input.pack()

# Ping button
button = tk.Button(window, text="Ping Host", font=("Arial", 10, "bold"), bg=("#1dddb3"), command=start_ping)
button.pack()

# Output area
result_label = tk.Label(window, text="Waiting for ping...", bg="#1D1D1D", fg="white", justify="left")
result_label.pack()

output = tk.Text(window, height=10, width=60, bg="#474747", fg="#0bdbae")
output.pack()

# Author
author = tk.Label(window, text="github.com/simonzagradisnik", fg="#5e5e5e", bg="#1d1d1d")
author.place(relx=0.725, rely=0.95)

# Version
version = tk.Label(window, text="v0.1", fg="#5e5e5e", bg="#1d1d1d")
version.place(relx=0, rely=0.95)

# Window settings
window.deiconify()
window.geometry("600x400")
window.configure(bg="#1D1D1D")
window.resizable(False, False)

window.mainloop()

