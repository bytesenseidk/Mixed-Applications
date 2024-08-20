import geocoder
import reverse_geocoder as rg
import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser

class IpLocator:
    def __init__(self, target_ip="me"):
        self.target = geocoder.ip(target_ip)
        self.data = self.locate(self.target)
    
    def __str__(self):
        if self.data:
            return (f"IP Address:   {self.data[0]}\n"
                    f"City:         {self.data[1]}\n"
                    f"Country:      {self.data[2]}\n"
                    f"Coordinates:  {self.data[3][0]}, {self.data[3][1]}")
        else:
            return "Location could not be determined."
        
    def locate(self, target):
        if target.latlng:  # Check if latlng is not None
            latitude, longitude = target.latlng
            city = rg.search((latitude, longitude), verbose=False)
            return [target.ip, city[0]["name"], target.country, [latitude, longitude]]
        else:
            return None  # Return None if latlng is not available

class GeoLocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geo Locator Tool")
        self.root.geometry("600x400")
        self.root.configure(bg="#2b2b2b")
        
        # Title label
        self.title_label = tk.Label(root, text="IP Geographical Locator", font=("Arial", 24, "bold"), fg="white", bg="#2b2b2b")
        self.title_label.pack(pady=20)
        
        # IP input field
        self.ip_frame = tk.Frame(root, bg="#2b2b2b")
        self.ip_frame.pack(pady=10)
        
        self.ip_label = tk.Label(self.ip_frame, text="Enter IP Address:", font=("Arial", 14), fg="white", bg="#2b2b2b")
        self.ip_label.pack(side=tk.LEFT, padx=10)
        
        self.ip_entry = tk.Entry(self.ip_frame, font=("Arial", 14), width=20)
        self.ip_entry.pack(side=tk.LEFT, padx=10)
        
        # Locate button
        self.locate_button = tk.Button(root, text="Locate IP", font=("Arial", 14, "bold"), bg="#212121", fg="white", relief="flat", command=self.locate_ip)
        self.locate_button.pack(pady=20)
        
        # Display area
        self.result_frame = tk.Frame(root, bg="#2b2b2b")
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(self.result_frame, text="", font=("Courier", 14), fg="white", bg="#2b2b2b", justify="left", anchor="w")
        self.result_label.pack(pady=10)

        # Buttons frame
        self.button_frame = tk.Frame(root, bg="#2b2b2b")
        self.button_frame.pack(pady=10)

        # Show on map button (Initially hidden)
        self.show_map_button = self.create_rounded_button(self.button_frame, text="Show on Map", command=self.open_map_in_browser)
        self.show_map_button.pack(side=tk.LEFT, padx=10)
        self.show_map_button.pack_forget()  # Hide button initially

        # Copy to clipboard button (Initially hidden)
        self.copy_button = self.create_rounded_button(self.button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(side=tk.LEFT, padx=10)
        self.copy_button.pack_forget()  # Hide button initially

        # Save to file button (Initially hidden)
        self.save_button = self.create_rounded_button(self.button_frame, text="Save to File", command=self.save_to_file)
        self.save_button.pack(side=tk.LEFT, padx=10)
        self.save_button.pack_forget()  # Hide button initially

    def create_rounded_button(self, parent, text, command):
        return tk.Button(parent, text=text, font=("Arial", 14, "bold"), bg="#212121", fg="white", relief="flat",
                         command=command, bd=0, highlightthickness=0, padx=20, pady=5, overrelief="flat", 
                         activebackground="#333333", activeforeground="white", 
                         highlightbackground="white", highlightcolor="white")

    def locate_ip(self):
        ip_address = self.ip_entry.get()
        if not ip_address:
            messagebox.showerror("Input Error", "Please enter an IP address.")
            return
        
        try:
            locator = IpLocator(ip_address)
            if locator.data:
                self.result_label.config(text=str(locator))
                self.latitude, self.longitude = locator.data[3][0], locator.data[3][1]
                
                # Show all buttons after successful location
                self.show_map_button.pack(side=tk.LEFT, padx=10)
                self.copy_button.pack(side=tk.LEFT, padx=10)
                self.save_button.pack(side=tk.LEFT, padx=10)
            else:
                messagebox.showerror("Location Error", "Location could not be determined for this IP address.")
                self.hide_buttons()
        except Exception as e:
            messagebox.showerror("Location Error", f"An error occurred: {str(e)}")
            self.hide_buttons()

    def open_map_in_browser(self):
        if hasattr(self, 'latitude') and hasattr(self, 'longitude'):
            map_url = f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
            webbrowser.open(map_url)
        else:
            messagebox.showerror("Map Error", "No valid location data to display on map.")

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.result_label.cget("text"))
        messagebox.showinfo("Copied", "Geolocation data copied to clipboard!")

    def save_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.result_label.cget("text"))
            messagebox.showinfo("Saved", "Geolocation data saved to file!")

    def hide_buttons(self):
        self.show_map_button.pack_forget()
        self.copy_button.pack_forget()
        self.save_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = GeoLocatorApp(root)
    root.mainloop()
