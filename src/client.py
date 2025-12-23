import socket
from typing import Tuple


def create_udp_socket(timeout: int) -> socket.socket:
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(timeout)
    return udp_socket


def udp_client(
    server_address: Tuple[str, int] = ("127.0.0.1", 57682),
    timeout: int = 6
) -> None:
    
    socket_client = create_udp_socket(timeout)
    print("UDP Echo Client started")
    print("Type messages to send. Type 'exit' to quit.\n")

    try:
        while True:
            user_message = input("Client > ").strip()

            if not user_message:
                continue

            if user_message.lower() == "exit":
                print("Shutting down client.")
                break

            socket_client.sendto(
                user_message.encode("utf-8"),
                server_address
            )

            try:
                response, server = socket_client.recvfrom(2048)
                print(f"Server {server} > {response.decode('utf-8')}")
            except socket.timeout:
                print("Warning: No response received (timeout).")

    finally:
        socket_client.close()

if __name__ == "__main__":
    udp_client()
