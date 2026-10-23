# blockchain.py

import hashlib
import json
from steganography import hide_data_in_image

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculate the SHA-256 hash of the block."""
        block_string = json.dumps({
            'index': self.index,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Create the first block in the chain with default values."""
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        """Return the latest block in the chain."""
        return self.chain[-1]

    def add_block(self, new_block):
        """Add a new block to the chain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Check the validity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

def main():
    blockchain = Blockchain()
    
    # Define user details
    users = [
        {"username": "user1", "password": "pass1", "profile_image": "user1.jpg"},
        {"username": "user2", "password": "pass2", "profile_image": "user2.jpg"},
        # Add more users as needed
    ]
    
    for i, user in enumerate(users):
        input_image = user['profile_image']
        output_image = f"output_{i + 1}.jpg"
        
        # Hide username and password in the user's profile picture
        image_with_data = hide_data_in_image(user['username'], user['password'], input_image, output_image)
        
        # Create a new block with the output image
        block_data = {
            "username": user['username'],
            "password": user['password'],
            "image": image_with_data
        }
        new_block = Block(i + 1, block_data, blockchain.get_latest_block().hash)
        blockchain.add_block(new_block)
    
    # Check blockchain validity
    print(f"Blockchain valid: {blockchain.is_chain_valid()}")
    
    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index}:\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\nData: {block.data}\n")

if __name__ == "__main__":
    main()
