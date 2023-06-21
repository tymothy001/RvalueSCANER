import requests
from tqdm import tqdm

def scan_addresses(addresses):
    duplicates_found = False
    with open("fundDuplicate.txt", "w") as output_file:
        progress_bar = tqdm(addresses, desc="Scanning addresses", unit="address")
        for addr in progress_bar:
            progress_bar.set_postfix(address=addr)
            output_file.write(f"Scanning address: {addr}\n")
            url = f"https://blockchain.info/address/{addr}?format=json&offset=0"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                txs = data['txs']
                inputs = []
                duplicates = []
                for tx in txs:
                    for inp in tx['inputs']:
                        r_value = inp['script'][10:74]
                        if r_value in inputs:
                            duplicates.append((tx['hash'], r_value))
                        else:
                            inputs.append(r_value)
                if duplicates:
                    output_file.write("Found duplicates:\n")
                    for duplicate in duplicates:
                        output_file.write(f"Transaction: {duplicate[0]}, r-value: {duplicate[1]}\n")
                        duplicates_found = True
                else:
                    output_file.write("No duplicates found.\n")

    if duplicates_found:
        print("Duplicate results saved to fundDuplicate.txt")
    else:
        print("No duplicates found.")

# Wczytanie adresów z pliku tekstowego
addresses = []
with open("addr.txt", "r") as file:
    addresses = [line.strip() for line in file]

# Ustawienie nazwy programu
print(" ")

print("\033[0;32m██████╗               ██╗   ██╗ █████╗ ██╗     ██╗   ██╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███████╗██████╗ \033[00m")
print("\033[0;32m██╔══██╗              ██║   ██║██╔══██╗██║     ██║   ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗\033[00m")
print("\033[0;32m██████╔╝    █████╗    ██║   ██║███████║██║     ██║   ██║█████╗      ███████╗██║     ███████║██╔██╗ ██║█████╗  ██████╔╝\033[00m")
print("\033[0;32m██╔══██╗    ╚════╝    ╚██╗ ██╔╝██╔══██║██║     ██║   ██║██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗\033[00m")
print("\033[0;32m██║  ██║               ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗    ███████║╚██████╗██║  ██║██║ ╚████║███████╗██║  ██║\033[00m")
print("\033[0;32m╚═╝  ╚═╝                ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝\033[00m")
print("                                                                                           ")

print("                                                                                           ")
print(" donate :  1xxxxieunR11dGzNz4ChUdQrhqQAdwUTq                                                                                  ")
print("                                                                                          ")
print("                                                                                           ")
print(" Check address for duplicated r values                                                                                        ")
print("                                                                                           ")




scan_addresses(addresses)
