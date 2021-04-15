FROM golang:1.16-alpine as builder
ENV CGO_ENABLED=0
WORKDIR /app
COPY . /app/
RUN go build -o server

FROM scratch
ENTRYPOINT ["/server"]
COPY --from=builder /app/server /