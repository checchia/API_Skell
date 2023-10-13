FROM cgr.dev/chainguard/python:latest-dev as builder

WORKDIR /app
ENV PATH="${PATH}:/home/nonroot/.local/bin"

COPY requirements.txt .
RUN pip install -r requirements.txt --user

FROM cgr.dev/chainguard/python:latest

WORKDIR /app
COPY . /

COPY --from=builder /home/nonroot/.local /home/nonroot/.local

ENV PATH="${PATH}:/home/nonroot/.local/bin"

ENTRYPOINT [ "python", "/app/main.py" ]
