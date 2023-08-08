


def read_file_in_chunks(file_path, chunk_size=10):
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            
            binary_string = ''.join(format(byte, '08b') for byte in chunk)
            yield binary_string

# # Example usage
# file_path = 'rick___roll.jpg'
# acc = ''
# for chunk in read_file_in_chunks(file_path):
#     acc += chunk

# # len(acc) - 796*8