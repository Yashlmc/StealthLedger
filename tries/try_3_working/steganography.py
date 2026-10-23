from stegano import lsb
from PIL import Image
from io import BytesIO
import pickle
import base64

def hide_object_in_image(image, obj):
    # If the image is passed as bytes, convert it to a PIL Image
    if isinstance(image, bytes):
        image = Image.open(BytesIO(image))
    
    # Serialize the object to a byte stream
    obj_bytes = pickle.dumps(obj)
    
    # Convert the byte stream to a base64 string (for easy embedding)
    obj_string = base64.b64encode(obj_bytes).decode()

    # Embed the base64 string into the image using LSB steganography
    secret_image = lsb.hide(image, obj_string)

    # Save the image into a byte stream (to return it)
    output_stream = BytesIO()
    secret_image.save(output_stream, format="PNG")
    output_stream.seek(0)  # Reset the stream position to the beginning

    return output_stream  # Return the byte stream of the modified image

def retrieve_object_from_image(image):
    # If the image is passed as bytes, convert it to a PIL Image
    if isinstance(image, bytes):
        image = Image.open(BytesIO(image))

    # Extract the hidden base64 string from the image
    obj_string = lsb.reveal(image)

    # Convert the base64 string back to bytes
    obj_bytes = base64.b64decode(obj_string)

    # Deserialize the byte stream back into the original Python object
    return pickle.loads(obj_bytes)

if __name__ == "__main__":
    with open('user_1.jpg', 'rb') as img_file:
        image_data = img_file.read()  # Read image as bytes

    # 2. Python object to hide (e.g., a dictionary or any object)
    hidden_object = {"sender": "Vedant", "amount": 100, "receiver": "Alice"}

    # 3. Hide the object in the image
    stegged_image_stream = hide_object_in_image(image_data, hidden_object)

    # 4. Save the output image to a file
    with open('stegged_image.jpg', 'wb') as out_file:
        out_file.write(stegged_image_stream.read())  # Write the steganographed image



    with open('stegged_image.jpg', 'rb') as img_file:
        image_data = img_file.read() 

    # 5. Retrieve the hidden object from the stegged image
    retrieved_object = retrieve_object_from_image(image_data)

    # 6. Print the retrieved object
    print(f"Retrieved object: {retrieved_object}")