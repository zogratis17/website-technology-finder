import subprocess
import webbrowser
import os
import json
import builtwith

def start_server():
    try:
        # Change directory to the server file location
        server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server.py')
        os.chdir(os.path.dirname(server_path))
        
        # Start the Python server in a separate process
        subprocess.Popen(['python', 'server.py'])
        
        print('Server started successfully!')
    except Exception as e:
        print('Error occurred while starting the server:', str(e))


def detect_technologies(url):
    try:
        # Add the 'http://' or 'https://' prefix to the URL
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        
        # Perform technology detection using the builtwith library
        technologies = builtwith.builtwith(url)
        return technologies
    except Exception as e:
        print('Error occurred while detecting technologies:', str(e))
        return None

if __name__ == "__main__":
    # Start the Python server
    start_server()

    # Open the browser extension

    # Get input URL from the user
    url = input('Enter the URL to detect technologies: ')
    
    # Detect technologies
    technologies = detect_technologies(url)
    
    if technologies:
        # Print the detected technologies
        print('Detected Technologies:')
        for tech, info in technologies.items():
            print(tech)
            print('--------------')
            if isinstance(info, list):
                for item in info:
                    print(item)
            else:
                for key, value in info.items():
                    if isinstance(value, list):
                        for version in value:
                            print(key, ':', version)
                    else:
                        print(key, ':', value)
            print()
    else:
        print('Failed to detect technologies.')
