# Python Simple Server Counter

_sorry for the delay 😓_

## **Installation**

```docker
cd docker/

docker build -t server-req:latest .
```

## **Run**

```docker
docker run --name server-req --rm -it -p 80:80 server-req:latest
```

## **Test**

```bash
curl 127.0.0.1:80
```

**Example output**

```
IP address: 127.0.0.1 | Request count: 1
```
