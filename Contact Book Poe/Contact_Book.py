import tkinter as tk
from tkinter import messagebox
import json
import os
import re

# -----------------------------
# File Setup
# -----------------------------
FILE_NAME = "contacts.json"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)


# -----------------------------
# Helper Functions
# -----------------------------
def load_contacts():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def refresh_contact_list():
    contact_listbox.delete(0, tk.END)

    contacts = load_contacts()

    for contact in contacts:
        display_text = f"{contact['name']} | {contact['phone']} | {contact['email']}"
        contact_listbox.insert(tk.END, display_text)


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# -----------------------------
# CRUD Functions
# -----------------------------
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    address = address_entry.get().strip()
    email = email_entry.get().strip()

    # Validation
    if not name or not phone or not address or not email:
        messagebox.showerror("Error", "All fields are required.")
        return

    if not phone.isdigit() or len(phone) < 7:
        messagebox.showerror("Error", "Please enter a valid phone number.")
        return

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(email_pattern, email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    contacts = load_contacts()

    new_contact = {
        "name": name,
        "phone": phone,
        "address": address,
        "email": email
    }

    contacts.append(new_contact)

    save_contacts(contacts)

    refresh_contact_list()
    clear_fields()

    messagebox.showinfo("Success", "Contact added successfully!")


def delete_contact():
    selected = contact_listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Please select a contact to delete.")
        return

    index = selected[0]

    contacts = load_contacts()

    deleted_contact = contacts.pop(index)

    save_contacts(contacts)

    refresh_contact_list()

    messagebox.showinfo(
        "Deleted",
        f"{deleted_contact['name']} deleted successfully."
    )


def search_contact():
    search_name = name_entry.get().strip().lower()

    if not search_name:
        messagebox.showerror("Error", "Enter a name to search.")
        return

    contacts = load_contacts()

    contact_listbox.delete(0, tk.END)

    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            display_text = (
                f"{contact['name']} | "
                f"{contact['phone']} | "
                f"{contact['email']}"
            )
            contact_listbox.insert(tk.END, display_text)
            found = True

    if not found:
        messagebox.showinfo("Search", "No matching contact found.")


def update_contact():
    selected = contact_listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact to update.")
        return

    index = selected[0]

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    address = address_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not phone or not address or not email:
        messagebox.showerror("Error", "All fields are required.")
        return

    contacts = load_contacts()

    contacts[index] = {
        "name": name,
        "phone": phone,
        "address": address,
        "email": email
    }

    save_contacts(contacts)

    refresh_contact_list()

    messagebox.showinfo("Updated", "Contact updated successfully!")


def load_selected_contact(event):
    selected = contact_listbox.curselection()

    if not selected:
        return

    index = selected[0]

    contacts = load_contacts()

    contact = contacts[index]

    clear_fields()

    name_entry.insert(0, contact["name"])
    phone_entry.insert(0, contact["phone"])
    address_entry.insert(0, contact["address"])
    email_entry.insert(0, contact["email"])


# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Contact Manager")
root.geometry("700x500")
root.configure(bg="#f0f0f0")


# -----------------------------
# Labels and Entry Fields
# -----------------------------
tk.Label(root, text="Name:", bg="#f0f0f0").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Phone Number:", bg="#f0f0f0").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

tk.Label(root, text="Address:", bg="#f0f0f0").pack()
address_entry = tk.Entry(root, width=50)
address_entry.pack()

tk.Label(root, text="Email:", bg="#f0f0f0").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Contact",
    width=15,
    command=add_contact
)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(
    button_frame,
    text="Update Contact",
    width=15,
    command=update_contact
)
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Contact",
    width=15,
    command=delete_contact
)
delete_button.grid(row=0, column=2, padx=5)

search_button = tk.Button(
    button_frame,
    text="Search Contact",
    width=15,
    command=search_contact
)
search_button.grid(row=0, column=3, padx=5)

view_button = tk.Button(
    root,
    text="View All Contacts",
    width=25,
    command=refresh_contact_list
)
view_button.pack(pady=5)


# -----------------------------
# Contact List Display
# -----------------------------
contact_listbox = tk.Listbox(root, width=90, height=15)
contact_listbox.pack(pady=10)

contact_listbox.bind("<<ListboxSelect>>", load_selected_contact)


# -----------------------------
# Start Program
# -----------------------------
refresh_contact_list()

root.mainloop()