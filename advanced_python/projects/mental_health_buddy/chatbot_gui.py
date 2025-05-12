import tkinter as tk
from tkinter import scrolledtext, ttk
from mental_health_buddy import (get_sad_response, get_happy_response, 
                            get_stressed_response, get_default_response)
from datetime import datetime
import tkinter.font as tkFont
import win32gui # type: ignore
import win32con # type: ignore

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("HERALDEXX Assistant 🤖")
        self.window.geometry("600x700")
        self.window.configure(bg='#2C3E50')
        
        # Initialize drag variables
        self._drag_data = {"x": 0, "y": 0, "dragging": False}
        
        # Make window corners rounded (Windows only)
        self.window.update_idletasks()
        self.hwnd = win32gui.GetParent(self.window.winfo_id())
        style = win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE)
        style = style & ~win32con.WS_CAPTION & ~win32con.WS_THICKFRAME
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE, style)
        
        # Set rounded corners
        self.update_rounded_corners()
        
        # Bind configure event to handle window resizing
        self.window.bind('<Configure>', self.on_window_configure)
        
        # Custom styling with explicit colors and proper button/entry configuration
        style = ttk.Style()
        style.configure('Custom.TFrame', background='#2C3E50')
        style.configure('Custom.TButton',
                       padding=10,
                       background='#3498DB',
                       foreground='white',
                       relief='raised')
        style.map('Custom.TButton',
                 background=[('active', '#2980B9'), ('disabled', '#BDC3C7')],
                 foreground=[('disabled', '#7F8C8D')])
        
        style.configure('Custom.TEntry',
                       padding=5,
                       fieldbackground='white',
                       foreground='black')
        
        style.configure('Custom.TLabel',
                       background='#2C3E50',
                       foreground='white')
        
        # Override default button style for better visibility
        style.layout('Custom.TButton', [
            ('Button.padding', {'sticky': 'nswe', 'children': [
                ('Button.label', {'sticky': 'nswe'})
            ]})
        ])
        
        # Custom font
        self.chat_font = tkFont.Font(family="Helvetica", size=10)
        
        # Header frame for dragging - this is the only draggable part
        self.header_frame = ttk.Frame(self.window, style='Custom.TFrame', cursor="arrow")
        self.header_frame.pack(fill=tk.X, pady=10)
        self.header_label = tk.Label(self.header_frame, 
                              text="🤖 HERALDEXX Assistant",
                              font=("Helvetica", 16, "bold"),
                              bg='#2C3E50',
                              fg='white',
                              cursor="arrow")
        self.header_label.pack(expand=True, fill=tk.X)
        
        # Make only header draggable with updated bindings
        self.header_frame.bind('<Button-1>', self.start_drag)
        self.header_frame.bind('<B1-Motion>', self.drag_window)
        self.header_frame.bind('<ButtonRelease-1>', self.stop_drag)
        self.header_label.bind('<Button-1>', self.start_drag)
        self.header_label.bind('<B1-Motion>', self.drag_window)
        self.header_label.bind('<ButtonRelease-1>', self.stop_drag)
        
        # Name entry and start button with tk widgets
        self.name_frame = tk.Frame(self.window, bg='#2C3E50')
        self.name_frame.pack(pady=10)
        
        tk.Label(self.name_frame, 
                text="Enter your name:",
                font=("Helvetica", 11),
                bg='#2C3E50',
                fg='white').pack(side=tk.LEFT)
                
        self.name_entry = tk.Entry(self.name_frame,
                                  width=20,
                                  bg='white',
                                  fg='black',
                                  font=("Helvetica", 10))
        self.name_entry.pack(side=tk.LEFT, padx=5)
        
        # Create start button
        self.start_button = tk.Button(
            self.name_frame, 
            text="Start Chat",
            font=("Helvetica", 10),
            bg='#3498DB',
            fg='white',
            activebackground='#2980B9',
            activeforeground='white',
            command=self.start_chat)
        self.start_button.pack(side=tk.LEFT)

        # Chat display with custom background
        self.chat_area = scrolledtext.ScrolledText(
            self.window,
            wrap=tk.WORD,
            width=50,
            height=20,
            font=self.chat_font,
            bg='#E8F4F9',
            fg='#2C3E50'
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Input area with tk widgets
        self.input_frame = tk.Frame(self.window, bg='#2C3E50')
        self.input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.msg_entry = tk.Entry(self.input_frame, 
                                 bg='white',
                                 fg='black',
                                 font=("Helvetica", 10))
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Create send button with tk
        self.send_button = tk.Button(
            self.input_frame,
            text="Send",
            font=("Helvetica", 10),
            bg='#3498DB',
            fg='white',
            activebackground='#2980B9',
            activeforeground='white',
            command=self.process_input
        )
        self.send_button.pack(side=tk.RIGHT)
        
        # Add clear chat and exit buttons with tk
        button_frame = tk.Frame(self.window, bg='#2C3E50')
        button_frame.pack(pady=5)
        
        self.clear_button = tk.Button(
            button_frame,
            text="Clear Chat",
            font=("Helvetica", 10),
            bg='#3498DB',
            fg='white',
            activebackground='#2980B9',
            activeforeground='white',
            command=self.clear_chat
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.exit_button = tk.Button(
            button_frame,
            text="Exit Chat",
            font=("Helvetica", 10),
            bg='#E74C3C',
            fg='white',
            activebackground='#C0392B',
            activeforeground='white',
            command=self.window.destroy
        )
        self.exit_button.pack(side=tk.LEFT, padx=5)
        
        # Ensure chat controls are properly configured initially
        self.chat_area.configure(state='disabled')
        self.msg_entry.configure(state='disabled')
        self.send_button.configure(state='disabled')
        self.clear_button.configure(state='disabled')
        # Exit button remains enabled by default
        
        self.user_name = ""
        
        # Initialize chat state
        self.chat_enabled = False
        
        # Enable double buffering and reduce flicker
        self.window.tk.call('tk', 'scaling', 1.0)
        self.window.attributes('-alpha', 0.999)  # Enables composition
        self.window.update_idletasks()
        
        # Optimize window drawing
        hwnd = self.window.winfo_id()
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        style |= win32con.WS_EX_COMPOSITED
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style)
        
        # Set window layering for smoother movement
        hwnd = self.window.winfo_id()
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, 
                             win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | 
                             win32con.WS_EX_LAYERED | win32con.WS_EX_COMPOSITED)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
        
    def start_chat(self):
        """Initialize chat after user enters name"""
        self.user_name = self.name_entry.get().strip()
        if self.user_name:
            self.chat_enabled = True
            self.name_frame.pack_forget()
            
            # Enable chat controls
            self.msg_entry.configure(state='normal')
            self.send_button.configure(state='normal')
            self.clear_button.configure(state='normal')
            self.chat_area.configure(state='normal')
            
            # Add welcome message
            self.add_message("HERALDEXX", f"Nice to meet you, {self.user_name}! 😊\nHow are you feeling today?")
            
            # Set focus to message entry
            self.msg_entry.focus_set()
    
    def process_input(self):
        """Process user input and generate response"""
        if not self.chat_enabled:
            return
            
        user_input = self.msg_entry.get().strip()
        if not user_input:  # Don't process empty input
            return
            
        # Save the input and clear entry field
        self.msg_entry.delete(0, tk.END)
        
        # Add user message first
        self.add_message("You", user_input)
        
        # Process response immediately
        if "sad" in user_input.lower():
            response = get_sad_response(self.user_name)
        elif "happy" in user_input.lower():
            response = get_happy_response(self.user_name)
        elif "stressed" in user_input.lower():
            response = get_stressed_response(self.user_name)
        elif "clear" in user_input.lower():
            self.clear_chat()
            return
        else:
            response = get_default_response(self.user_name)
        
        # Add bot response and ensure focus returns to entry
        self.add_message("HERALDEXX", response)
        self.msg_entry.focus_set()
        
    def clear_chat(self):
        self.chat_area.configure(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.configure(state='disabled')
        self.add_message("HERALDEXX", f"Chat cleared! How else can I help you, {self.user_name}? 😊")
    
    def add_message(self, sender, message):
        """Add a message to the chat area"""
        self.chat_area.configure(state='normal')
        timestamp = datetime.now().strftime("%H:%M")
        
        # Add the message with proper formatting
        self.chat_area.insert(tk.END, f"\n{timestamp} ", "time")
        if sender == "You":
            self.chat_area.insert(tk.END, f"{sender}: ", "user")
            self.chat_area.insert(tk.END, f"{message}\n", "user_msg")
        else:
            self.chat_area.insert(tk.END, f"🤖 {sender}: ", "bot")
            self.chat_area.insert(tk.END, f"{message}\n", "bot_msg")
        
        # Configure tags and ensure latest message is visible
        self.chat_area.tag_configure("time", foreground="gray")
        self.chat_area.tag_configure("user", foreground="#2980B9", font=("Helvetica", 10, "bold"))
        self.chat_area.tag_configure("bot", foreground="#27AE60", font=("Helvetica", 10, "bold"))
        self.chat_area.tag_configure("user_msg", foreground="black")
        self.chat_area.tag_configure("bot_msg", foreground="black")
        
        self.chat_area.see(tk.END)
        self.chat_area.configure(state='disabled')
    
    def start_drag(self, event):
        """Initialize drag."""
        self._drag_data["x"] = event.x_root - self.window.winfo_x()
        self._drag_data["y"] = event.y_root - self.window.winfo_y()
        self._drag_data["dragging"] = True

    def stop_drag(self, event):
        """Handle end of drag operation."""
        self._drag_data["dragging"] = False

    def drag_window(self, event):
        """Handle window dragging."""
        if self._drag_data["dragging"]:
            new_x = event.x_root - self._drag_data["x"]
            new_y = event.y_root - self._drag_data["y"]
            # Use direct win32gui call for movement
            win32gui.MoveWindow(self.hwnd, new_x, new_y, 
                              self.window.winfo_width(), 
                              self.window.winfo_height(), False)

    def update_rounded_corners(self):
        """Update the rounded corners of the window."""
        try:
            width = self.window.winfo_width()
            height = self.window.winfo_height()
            region = win32gui.CreateRoundRectRgn(0, 0, width, height, 15, 15)
            win32gui.SetWindowRgn(self.hwnd, region, True)
        except Exception:
            pass

    def on_window_configure(self, event):
        """Handle window resize events."""
        if event.widget == self.window and not self._drag_data["dragging"]:
            self.window.after_idle(self.update_rounded_corners)
            
    def run(self):
        """Start the application."""
        self.window.mainloop()

if __name__ == "__main__":
    app = ChatbotGUI()
    # Set initial focus to name entry
    app.name_entry.focus_set()
    app.run()
