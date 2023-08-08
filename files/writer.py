
def write_binary_string_to_file(binary_string, output_file_path):
    with open(output_file_path, 'wb') as file:
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i + 8]
            if len(byte) < 8:
                byte = byte + '0' * (8 - len(byte))
            file.write(bytes([int(byte, 2)]))

# # Example usage
# binary_string = data
# output_file_path = f'out/output_file.{ex}'
# write_binary_string_to_file(binary_string, output_file_path)