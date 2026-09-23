# Stage 1: Build Stage
FROM golang:1.22-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency files first to leverage Docker caching
COPY go.mod go.sum* ./
RUN go mod download

# Copy the rest of your source code
COPY . .

# Compile the Go application into a binary named "calculator"
RUN go build -o calculator .


# Stage 2: Runtime Stage
FROM alpine:latest

# Set the working directory for the final image
WORKDIR /app

# Copy ONLY the compiled binary from the builder stage
COPY --from=builder /app/calculator .

# Expose the standard port
EXPOSE 8080

# Command to run the executable
CMD ["./calculator"]
