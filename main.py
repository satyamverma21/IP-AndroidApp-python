from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import socket

class IPApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Create a label to display the IP address
        self.ip_label = Label(text='Your IP Address will be displayed here')
        layout.add_widget(self.ip_label)

        # Create a button to refresh the IP address
        refresh_button = Button(text='Refresh IP', size_hint=(None, None), size=(150, 50))
        refresh_button.bind(on_press=self.refresh_ip)
        layout.add_widget(refresh_button)

        return layout

    def refresh_ip(self, instance):
        # Get the IP address
        ip_address = self.get_ip_address()

        # Update the label with the new IP address
        self.ip_label.text = f'Your IP Address: {ip_address}' if ip_address else 'Unable to retrieve the IP address.'

    def get_ip_address(self):
        try:
           
            # Creating a socket objectexport PATH=$PATH:~/.local/bin/
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Connecting to an external server (doesn't actually send data)
            s.connect(('8.8.8.8', 1))

            # Getting the IP address from the socket
            ip_address = s.getsockname()[0]

            return ip_address

        except Exception as e:
            print(f"Error: {e}")
            return None

        finally:
            # Closing the socket
            s.close()

if __name__ == '__main__':
    IPApp().run()
