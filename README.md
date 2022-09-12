# Python Simple Server Counter

## Installation

```docker
docker build -t server-req:latest .
```

## Run

```docker
docker run --name server-req --rm -it -p 80:80 server-req:latest
```

## Test

```bash
curl 127.0.0.1:80
```
