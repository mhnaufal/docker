FROM python:3.8.14-alpine3.16

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install --user --no-cache -r requirements.txt

COPY script.py script.py

EXPOSE 80

ENTRYPOINT [ "python" ]

CMD [ "script.py" ]
