# main.py
from blockchain import Blockchain
from steganography import hide_object_in_image, retrieve_object_from_image

# 1. Initialize Blockchain
blockchain = Blockchain()

# 2. Define a Python object to hide (can be any Python object)
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

hidden_object = Transaction(sender="Vedant", receiver="Alice", amount=100)

# 3. Hide the object in the image using steganography
image_path = 'input_image.png'
output_image_path = 'stegged_image.png'

hide_object_in_image(image_path, hidden_object, output_image_path)

# 4. Open the stegged image and read the binary data
with open(output_image_path, 'rb') as img_file:
    stegged_image_data = img_file.read()

# 5. Add the stegged image to the blockchain
blockchain.add_block(stegged_image_data)

# Print the blockchain
for block in blockchain.chain:
    print(f"Block {block.index} | Data: {block.data[:20]}... | Hash: {block.hash}")

# 6. Retrieve the hidden object from the stegged image
retrieved_object = retrieve_object_from_image(output_image_path)
print(f"Retrieved object: {retrieved_object.__dict__}")
