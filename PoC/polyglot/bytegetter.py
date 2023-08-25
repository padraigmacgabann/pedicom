def read_dicom_file(file_path):
    with open(file_path, "rb") as file:
        byte_content = file.read()
    return byte_content

if __name__ == "__main__":
    dicom_file_path = "pedicom-cylera.dcm" #"path_to_your_file.dcm"
    content = read_dicom_file(dicom_file_path)
    
    # Just for demonstration purposes, you can print the first 100 bytes
    # Be careful when printing raw bytes to the console, as it might be unreadable or cause display issues
    #print(content[:100])
    #print(content[:128])

    # Print the first 128 bytes in raw hex
    hex_content = ''.join(f'{byte:02x}' for byte in content[:128])
    print(hex_content)


