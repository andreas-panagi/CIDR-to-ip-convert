import ipaddress

# Define the file containing the CIDR notations
cidr_file = "test.txt"

# Define the file to write the IP addresses to
ip_file = "ip_addresses.txt"

# Loop through each CIDR notation in the file
with open(cidr_file, "r") as f, open(ip_file, "w") as out:
    for line in f:
        cidr_notation = line.strip()
        # Create an IPv4 network object from the CIDR notation
        net = ipaddress.IPv4Network(cidr_notation)
        # Loop through each IP address in the range and write it to a file
        for ip_address in net:
            out.write(str(ip_address) + "\n")
