def remove_leading_zeros(ip_address):
    octets = ip_address.split(".")
    
    for i in range(len(octets)):
        octets[i] = str(int(octets[i]))
    
    new_ip_address = ".".join(octets)
    
    return new_ip_address

ip_address = "192.168.001.001"
new_ip_address = remove_leading_zeros(ip_address)
print(ip_address)
print(new_ip_address)
