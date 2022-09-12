FROM alpine:latest

ENV TARGET_IP=$TARGET_IP

CMD [ "curl", "TARGET_IP" ]
