import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.file_services import save_chunk, serve_chunk, calculate_checksum

# Mock socket object for testing
class MockSocket:
    def __init__(self, data):
        self.data = data
        self.received_data = b''

    def recv(self, buffer_size):
        # Simulate receiving data from a socket in 512-byte chunks
        chunk, self.data = self.data[:buffer_size], self.data[buffer_size:]
        return chunk

    def sendall(self, data):
        # Simulate sending data to a socket
        self.received_data += data

def test_chunking_and_reassembly():
    # Create a mock file of test data
    original_data = b'This is a test file. ' * 100  # Larger than 512 bytes

    # Write this mock file to simulate file serving
    filename = 'test_file.txt'
    with open(filename, 'wb') as f:
        f.write(original_data)

    # Use a mock socket to serve the file chunks
    mock_socket = MockSocket(b'')
    serve_chunk(mock_socket, filename, '')  # Simulate serving file

    # Use a mock socket to save the file chunks
    received_file = 'received_file.txt'
    mock_receive_socket = MockSocket(mock_socket.received_data)
    save_chunk(mock_receive_socket, received_file)

    # Compare checksums of original and received files to verify integrity
    original_checksum = calculate_checksum(filename)
    received_checksum = calculate_checksum(received_file)
    assert original_checksum == received_checksum, "File reassembly failed!"

    # Cleanup test files
    os.remove(filename)
    os.remove(received_file)

if __name__ == "__main__":
    test_chunking_and_reassembly()
    print("Chunking and reassembly test passed!")
