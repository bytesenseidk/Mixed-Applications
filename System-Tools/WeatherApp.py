import requests  # For making API requests to get weather data
import tkinter as tk  # For creating the GUI (Graphical User Interface)
from PIL import Image, ImageTk  # For handling and displaying images/icons in the GUI

# Function to get weather data from the OpenWeatherMap API
def get_weather():
    city = city_entry.get()  # Get the city entered by the user
    if not city:
        label_temp.config(text="Enter a city name!")
        return
    
    api_key = "<API_KEY>"  # Replace with your own OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # API request URL
    
    response = requests.get(url).json()  # Make the API request and parse the JSON response
    
    # Print the full response for debugging
    print("API Response:", response)  # Print the response to see what data is returned
    
    # Check if the "main" key exists in the response
    if "main" in response:
        temp = response["main"]["temp"]
        weather = response["weather"][0]["description"]
        icon_code = response["weather"][0]["icon"]

        # Update the temperature label with a pulsing animation
        animate_pulse(label_temp, f"{temp}°C")
        
        # Update the weather description label with a fade-in animation
        animate_fade_in(label_weather, weather.capitalize())
        
        # Fetch the weather icon from OpenWeatherMap and update the icon label
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"  # URL for the weather icon
        icon_image = Image.open(requests.get(icon_url, stream=True).raw)  # Load the icon image using PIL.Image
        label_icon.image = ImageTk.PhotoImage(icon_image)  # Convert PIL image to PhotoImage for tkinter
        label_icon.config(image=label_icon.image)  # Set the icon in the label
    else:
        # Handle the error if "main" key is missing
        error_message = response.get("message", "Unknown error")
        print(f"Error: {error_message}")
        label_temp.config(text="N/A")
        label_weather.config(text="City not found or invalid API key")
        label_icon.config(image='')  # Clear the icon

# Animation: Pulse effect on temperature label
def animate_pulse(label, new_text, scale=1.0, step=0.05, max_scale=1.2):
    label.config(text=new_text)  # Set the new text
    scale += step  # Increase the scale by the step
    label.config(font=("Arial", int(48 * scale), "bold"))  # Adjust the font size to create a pulse effect
    
    # Reverse direction if max scale is reached
    if scale > max_scale or scale < 1.0:
        step = -step
    
    # Continue animating until scale returns to normal
    if round(scale, 2) != 1.0:
        root.after(50, lambda: animate_pulse(label, new_text, scale, step))  # Re-run the function after 50 ms

# Animation: Fade-in effect on weather description label
def animate_fade_in(label, new_text, alpha=0):
    # Define a list of intermediate colors to simulate fading
    colors = ['#333333', '#555555', '#777777', '#999999', '#bbbbbb', '#dddddd', '#ffffff']
    label.config(text=new_text, fg=colors[int(alpha * len(colors))])  # Update the color to simulate fading
    
    alpha += 0.1  # Increment the alpha level
    
    if alpha <= 1.0:
        root.after(100, lambda: animate_fade_in(label, new_text, alpha))  # Continue fading in

# Set up the main application window
root = tk.Tk()  # Initialize the main window
root.title("Weather Dashboard")  # Set the window title
root.geometry("400x500")  # Set the window size
root.configure(bg="#1e1e2f")  # Set the background color for the dashboard

# Create and configure the label for entering the city name
city_entry_label = tk.Label(root, text="Enter city:", font=("Arial", 14), fg="white", bg="#1e1e2f")
city_entry_label.pack(pady=10)

# Create the input field for the city
city_entry = tk.Entry(root, font=("Arial", 14), width=20, bg="white")
city_entry.pack(pady=5)

# Create and configure the label for displaying the temperature
label_temp = tk.Label(root, font=("Arial", 48, "bold"), fg="#ffffff", bg="#1e1e2f")  # Large font for temperature
label_temp.pack(pady=20)  # Add padding around the label for spacing

# Create and configure the label for displaying the weather description
label_weather = tk.Label(root, font=("Arial", 24), fg="#ffffff", bg="#1e1e2f")  # Medium font for weather description
label_weather.pack()  # Pack the label into the window

# Create and configure the label for displaying the weather icon
label_icon = tk.Label(root, bg="#1e1e2f")  # Icon label with the same background color
label_icon.pack(pady=10)  # Add padding around the icon for spacing

# Create and configure the refresh button to update the weather data
refresh_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather, bg="#4caf50", fg="white", relief="flat")  # Styled button
refresh_button.pack(pady=20)  # Add padding around the button for spacing

root.mainloop()  # Run the main loop to keep the GUI window open
