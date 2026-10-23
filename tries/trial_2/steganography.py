from PIL import Image
import numpy as np

def hide_data_in_image(image_path, data, output_path):
    img = Image.open(image_path)
    img_data = np.array(img)
    
    # Flatten image data into a 1D array
    flat_img_data = img_data.flatten()
    
    # Convert data to binary format and append an end marker
    data_bin = ''.join(format(ord(i), '08b') for i in data) + '1111111111111110'
    
    # Embed binary data into image
    for i in range(len(data_bin)):
        flat_img_data[i] = (flat_img_data[i] & ~1) | int(data_bin[i])
    
    # Reshape back to original image shape and save it
    new_img_data = flat_img_data.reshape(img_data.shape)
    new_img = Image.fromarray(new_img_data)
    new_img.save(output_path)

def retrieve_data_from_image(image_path):
    img = Image.open(image_path)
    img_data = np.array(img).flatten()
    
    # Extract the least significant bits
    bin_data = ''
    for byte in img_data:
        bin_data += str(byte & 1)
    
    # Convert binary to string, stopping at the end marker
    data_bytes = [bin_data[i:i+8] for i in range(0, len(bin_data), 8)]
    data = ''.join(chr(int(byte, 2)) for byte in data_bytes)
    return data.split('1111111111111110')[0]  # Return data before end marker
