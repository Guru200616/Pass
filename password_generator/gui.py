import tkinter as tk
from tkinter import messagebox

from .logic import generate_password, PasswordConfigError


def run_app() -> None:
    """Create and run the Tkinter GUI application."""
    root = tk.Tk()
    root.title("🔐 Password Generator")
    root.geometry("420x340")
    root.resizable(False, False)
    root.config(bg="lightgray")

    # ---------- Inner Functions (Event Handlers) ---------- #

    def on_generate():
        """Handle click on 'Generate Password' button."""
        try:
            length_str = length_entry.get().strip()
            length = int(length_str)

            password = generate_password(
                length=length,
                use_upper=use_upper.get(),
                use_lower=use_lower.get(),
                use_digits=use_digits.get(),
                use_symbols=use_symbols.get(),
            )

            password_var.set(password)

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter a valid number for password length (>= 4)."
            )
        except PasswordConfigError:
            messagebox.showwarning(
                "Selection Error",
                "Please select at least one character set."
            )

    def on_copy():
        """Handle click on 'Copy to Clipboard' button."""
        password = password_var.get()

        if not password:
            messagebox.showwarning(
                "No Password",
                "Generate a password before copying."
            )
            return

        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    # ---------- UI Layout ---------- #

    # Title Label
    title_label = tk.Label(
        root,
        text="Password Generator",
        font=("Helvetica", 18, "bold"),
        bg="lightgray"
    )
    title_label.pack(pady=10)

    # Frame for length input
    input_frame = tk.Frame(root, bg="lightgray")
    input_frame.pack(pady=5)

    length_label = tk.Label(
        input_frame,
        text="Enter Password Length:",
        bg="lightgray"
    )
    length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    length_entry = tk.Entry(input_frame, width=10)
    length_entry.grid(row=0, column=1, padx=5, pady=5)
    length_entry.insert(0, "12")  # Default length

    # Frame for checkbox options
    options_frame = tk.LabelFrame(
        root,
        text="Character Options",
        bg="lightgray",
        padx=10,
        pady=10
    )
    options_frame.pack(pady=10, padx=10, fill="x")

    use_upper = tk.BooleanVar(value=True)
    use_lower = tk.BooleanVar(value=True)
    use_digits = tk.BooleanVar(value=True)
    use_symbols = tk.BooleanVar(value=True)

    upper_cb = tk.Checkbutton(
        options_frame,
        text="Include Uppercase (A-Z)",
        variable=use_upper,
        bg="lightgray",
        anchor="w"
    )
    upper_cb.grid(row=0, column=0, sticky="w")

    lower_cb = tk.Checkbutton(
        options_frame,
        text="Include Lowercase (a-z)",
        variable=use_lower,
        bg="lightgray",
        anchor="w"
    )
    lower_cb.grid(row=1, column=0, sticky="w")

    digits_cb = tk.Checkbutton(
        options_frame,
        text="Include Digits (0-9)",
        variable=use_digits,
        bg="lightgray",
        anchor="w"
    )
    digits_cb.grid(row=2, column=0, sticky="w")

    symbols_cb = tk.Checkbutton(
        options_frame,
        text="Include Symbols (!@#$...)",
        variable=use_symbols,
        bg="lightgray",
        anchor="w"
    )
    symbols_cb.grid(row=3, column=0, sticky="w")

    # Output password display
    password_var = tk.StringVar()

    output_entry = tk.Entry(
        root,
        textvariable=password_var,
        font=("Courier", 12),
        justify="center",
        width=32
    )
    output_entry.pack(pady=10)

    # Buttons frame
    buttons_frame = tk.Frame(root, bg="lightgray")
    buttons_frame.pack(pady=5)

    generate_button = tk.Button(
        buttons_frame,
        text="Generate Password",
        command=on_generate,
        bg="green",
        fg="white",
        width=18
    )
    generate_button.grid(row=0, column=0, padx=5, pady=5)

    copy_button = tk.Button(
        buttons_frame,
        text="Copy to Clipboard",
        command=on_copy,
        bg="blue",
        fg="white",
        width=18
    )
    copy_button.grid(row=0, column=1, padx=5, pady=5)

    # Start the Tkinter main loop
    root.mainloop()
