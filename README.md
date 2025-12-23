# UDP Echo Client–Server (Python)

A lightweight UDP-based client–server application demonstrates
connectionless communication, timeout handling, and message echoing
using Python socket programming.

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

```text
[2025-12-23 14:20:56] Echo (9 bytes): hello udp
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
