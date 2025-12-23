# UDP Echo Client–Server (Python)

A lightweight UDP-based client–server application demonstrates
connectionless communication, timeout handling, and message echoing
using Python socket programming.

## How the Application Works

### Server Behavior
- The server binds to a UDP socket and listens on a fixed port.
- It waits for incoming datagrams from any client.
- Upon receiving a message:
  - The server records the timestamp and message size.
  - It sends the same message back (echo) to the client.
- The server runs continuously until manually stopped.

### Client Behavior
- The client sends text messages to the server using UDP.
- After sending a message, the client waits for a response.
- A timeout is set to handle cases where:
  - The server is not running
  - The packet or response is lost
- If a response is received, the echoed message is displayed.
- Typing `exit` cleanly terminates the client.

## Key Concepts Demonstrated
- UDP (User Datagram Protocol)
- Connectionless client–server architecture
- Unreliable data transmission
- Timeout-based error handling
- Network observability (timestamps, message size)

## Project Structure

```
udp-echo-client-server/
├── src/
│ ├── client.py
│ └── server.py
├── README.md
└── .gitignore
```  

## How to Run

### Start the server

Open a terminal and run:

```bash
python src/server.py
```

The server will start listening for incoming messages.

### Start the client

Open a new terminal and run:

```bash
python src/client.py
```

Type messages in the client terminal.  
Type `exit` to terminate the client.

## Example Output
**Client Side**
```text
[2025-12-23 14:20:56] Echo (9 bytes): hello udp
```

**Server Side**
```text
[2025-12-23 14:20:56] Received 9 bytes from ('127.0.0.1', 54321)
[2025-12-23 14:20:56] Echoed message back to client
```

## Notes

- The client uses a timeout to handle cases where the server is unavailable.
- Since UDP is connectionless, messages may be sent even if the server is
  not running, and responses are not guaranteed.


## Skills Demonstrated

- Python socket programming
- UDP and connectionless networking
- Basic distributed systems concepts
- Clean code structure and error handling
