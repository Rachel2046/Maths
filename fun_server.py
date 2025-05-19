# Serve files on local machine in my LAN through QRcode
import http.server, socketserver, subprocess, webbrowser, socket
import pyqrcode, os

if __name__ == '__main__':
    # Run in the directory with the animation page
    page_directory = ('path/to/your/page')
    os.chdir(page_directory)

    # Set port number and get IPV4 ip address
    port = 8080
    # host = subprocess.run(["hostname", "-I"], capture_output=True).stdout[:10].decode('utf-8')
    host = socket.gethostbyname(socket.gethostname())
    ip = 'http://' + host + ":" + str(port)
    # Link to the page
    link = ip + "/animation.html"

    # Generate QR code from link
    qrcode = pyqrcode.create(link)
    qrcode.svg('myqr.svg', scale=8)
    # Display QR code SVG image
    webbrowser.open('myqr.svg')

    # Serve the page
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((host, port), handler) as httpd:
        print("Scan the QR code...")
        print(f"Or try this in your browser: {link}")
        try:  # Start server
            httpd.serve_forever()
        except(KeyboardInterrupt, SystemExit):
            print("Shutting down the server...")

