# J2pipeline

## Installation

Create Python 3.12 virtual environment, activate it and run

```sh
pip install j2pipeline
```

## Setup

J2pipeline requires an active TCP server listening on port 50027

**Server:**

-   Receives a prompt
-   Sends back AI response

**Protocol:**

1. 16 bytes header (message length)
2. Message (in UTF-8)

**For example:**

```python
data: bytes = message.encode(encoding='UTF-8')
size: bytes = f'{len(data):16}'.encode(encoding='UTF-8')
server.send(size)
server.send(data)
```

## License

J2pipeline is a free, open-source software distributed under the [MIT License](LICENSE.txt)
