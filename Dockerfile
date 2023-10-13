FROM cgr.dev/chainguard/python:latest-dev as builder

WORKDIR /app
ENV PATH="${PATH}:/home/nonroot/.local/bin"

COPY requirements.txt .
RUN pip install -r requirements.txt --user

FROM cgr.dev/chainguard/python:latest

WORKDIR /app
COPY . /

COPY --from=builder /home/nonroot/.local/lib /home/nonroot/.local/lib
COPY --from=builder /home/nonroot/.local/bin /home/nonroot/.local/bin

ENV PATH="${PATH}:/home/nonroot/.local/bin"

ENTRYPOINT [ "python", "/app/main.py" ]
