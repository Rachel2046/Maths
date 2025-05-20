# Serve files on local machine in my LAN through QRcode
import http.server, socketserver, subprocess, webbrowser, socket
import pyqrcode, os

if __name__ == '__main__':
    # Part 1: Run in the directory with the animation page
    page_directory = os.path.join(os.path.expanduser('~'), 'Python/mouse_following_animation/')
    os.chdir(page_directory)

    # Part 2: Set port number and get IPV4 ip address
    port = 8080
    # Find local machine IP: Linux
    host = subprocess.run(["hostname", "-I"], capture_output=True).stdout[:10].decode('utf-8')
    ip = 'http://' + host + ":" + str(port)
    # Link to the page
    link = ip + "/animation.html"

    # Part 3: Generate QR code from link
    qrcode = pyqrcode.create(link)
    qrcode.svg('myqr.svg', scale=8)
    # Display QR code SVG image
    webbrowser.open('myqr.svg')

    # Part 4: Serve the page
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((host, port), handler) as httpd:
        print("Scan the QR code...")
        print(f"Or try this in your browser: {link}")
        try:  # Start server
            httpd.serve_forever()
        except(KeyboardInterrupt, SystemExit):
            print("Shutting down the server...")

