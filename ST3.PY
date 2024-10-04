import tkinter as tk
from tkinter import messagebox
import time
import threading

class Sabertooth:
    def __init__(self, output_area):
        self.output_area = output_area
        self.output_area.insert(tk.END, "Sabertooth 2x60 initialized for virtual demo.\n")
        self.output_area.see(tk.END)  # Scroll to the end

    def send_command(self, command, data):
        """Simulates sending a command to the Sabertooth with specified data as a byte."""
        direction = ""
        movement = ""
        byte_data = data.to_bytes(1, byteorder='big')  # Convert data to byte format

        # Determine the action based on the command
        if command == 0:  # Drive forward motor 1
            direction = "Motor 1 moving forward"
            movement = f"at speed {data} (byte: {byte_data})"
        elif command == 1:  # Drive backward motor 1
            direction = "Motor 1 moving backward"
            movement = f"at speed {data} (byte: {byte_data})"
        elif command == 4:  # Drive forward motor 2
            direction = "Motor 2 moving forward"
            movement = f"at speed {data} (byte: {byte_data})"
        elif command == 5:  # Drive backward motor 2
            direction = "Motor 2 moving backward"
            movement = f"at speed {data} (byte: {byte_data})"
        elif command == 2:  # Set min voltage
            direction = "Setting minimum voltage"
            movement = f"to {data * 0.2 + 6} volts (byte: {byte_data})"
        elif command == 3:  # Set max voltage
            direction = "Setting maximum voltage"
            movement = f"to {data / 5.12} volts (byte: {byte_data})"
        elif command == 14:  # Set serial timeout
            direction = "Setting serial timeout"
            movement = f"to {data * 100} ms (byte: {byte_data})"
        elif command == 15:  # Set baud rate
            baud_rates = {1: 2400, 2: 9600, 3: 19200, 4: 38400, 5: 115200}
            direction = "Setting baud rate"
            movement = f"to {baud_rates.get(data, 'Invalid rate')} bps (byte: {byte_data})"
        elif command == 16:  # Set ramping
            direction = "Setting ramping"
            movement = f"to {'fast' if data == 1 else 'medium' if data <= 10 else 'slow' if data <= 20 else 'off'} (byte: {byte_data})"
        elif command == 17:  # Set deadband
            direction = "Setting deadband"
            movement = f"to {data} (byte: {byte_data})"

        # Append the result to the output area
        self.output_area.insert(tk.END, f"Sending Command: {command}, Data: {data} => {direction} {movement}\n")
        self.output_area.see(tk.END)  # Scroll to the end
        time.sleep(2)  # Delay of 2 seconds

    def run_command(self, command, data):
        """Run the command in a separate thread to avoid freezing the UI."""
        self.send_command(command, data)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sabertooth 2x60 Simulator")
        self.geometry("600x400")

        self.output_area = tk.Text(self, wrap=tk.WORD, height=15)
        self.output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.command_label = tk.Label(self, text="Command (in binary):")
        self.command_label.pack(padx=10, pady=5)

        self.command_entry = tk.Entry(self)
        self.command_entry.pack(padx=10, pady=5)

        self.data_label = tk.Label(self, text="Data (in binary):")
        self.data_label.pack(padx=10, pady=5)

        self.data_entry = tk.Entry(self)
        self.data_entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(self, text="Send Command", command=self.send_command)
        self.send_button.pack(pady=20)

        self.sabertooth = Sabertooth(self.output_area)

    def send_command(self):
        """Retrieve command and data, and send to the Sabertooth."""
        command_binary = self.command_entry.get()
        data_binary = self.data_entry.get()

        try:
            command = int(command_binary, 2)  # Convert binary string to integer
            data = int(data_binary, 2)  # Convert binary string to integer
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid binary values.")
            return

        # Validate inputs
        if command < 0 or command > 17:
            messagebox.showerror("Invalid Command", "Command must be between 0 and 17.")
            return
        if data < 0 or data > 127:
            messagebox.showerror("Invalid Data", "Data must be between 0 and 127.")
            return

        # Run the command in a separate thread
        threading.Thread(target=self.sabertooth.run_command, args=(command, data)).start()

# Run the application
if __name__ == "__main__":
    app = Application()
    app.mainloop()

