import csv

def txt_to_csv(txt_file, csv_file):
    # Open the txt file and read the MAC addresses
    with open(txt_file, 'r') as file:
        mac_addresses = file.readlines()

    # Remove any leading/trailing whitespace characters like newline
    mac_addresses = [mac.strip() for mac in mac_addresses]

    # Write the MAC addresses to the csv file with a header
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['Mac addresses'])
        
        # Write the MAC addresses
        for mac in mac_addresses:
            writer.writerow([mac])

# Example usage
txt_file = 'mac_addresses.txt'
csv_file = 'mac_addresses.csv'
txt_to_csv(txt_file, csv_file)
