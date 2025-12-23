import socket
import datetime
from typing import Tuple


def udp_echo_server(
    host: str = "127.0.0.1",
    port: int = 57682
) -> None:
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDP Echo Server listening on {host}:{port}")

    try:
        while True:
            data, client_address = server_socket.recvfrom(2048)
            message = data.decode("utf-8")

            timestamp = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
            response = (
                f"[{timestamp}] "
                f"Echo ({len(message)} bytes): {message}"
            )

            print(f"Received from {client_address}: {message}")
            server_socket.sendto(response.encode("utf-8"), client_address)

    except KeyboardInterrupt:
        print("\nServer shutting down gracefully.")

    finally:
        server_socket.close()

if __name__ == "__main__":
    udp_echo_server()
