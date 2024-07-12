import nmap  # Import the nmap module for port scanning

# Function to scan ports on a target IP address
def scan_ports(target, begin, end):
    scanner = nmap.PortScanner()  # Initialize the PortScanner object
    open_ports = []  # List to store open ports

    # Loop through the specified range of ports
    for i in range(begin, end + 1):
        try:
            # Perform the scan on the current port
            res = scanner.scan(target, str(i))
            
            # Check if the scan result contains the expected structure
            if 'scan' in res and target in res['scan'] and 'tcp' in res['scan'][target] and i in res['scan'][target]['tcp']:
                state = res['scan'][target]['tcp'][i]['state']  # Get the state of the current port
                
                # If the port is open, add it to the list and print the result
                if state == 'open':
                    open_ports.append(i)
                    print(f'Port {i} is open')
            else:
                # If the scan data is not available, print a message
                print(f'Port {i} scan data is not available')
        except Exception as e:
            # Handle any exceptions that occur during the scan
            print(f'Error scanning port {i}: {e}')

    return open_ports  # Return the list of open ports

if __name__ == "__main__":
    target = input("Please enter the IP address: ")  # Prompt the user to enter the target IP address
    begin = 80  # Define the starting port number
    end = 443  # Define the ending port number

    # Call the scan_ports function and store the result
    open_ports = scan_ports(target, begin, end)
    
    # Print the list of open ports or a message if none are found
    if open_ports:
        print(f'Open ports: {open_ports}')
    else:
        print('No open ports found')

