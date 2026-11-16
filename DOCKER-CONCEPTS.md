# Docker Concepts

## Image vs container
An image is a read-only template. A container is a running instance of it.

## Container lifecycle
run -> running -> stop -> exited -> rm -> gone.
`docker exec` opens a shell in a running container; exiting that shell does not stop the container.

## Port mapping
`-p HOST:CONTAINER` forwards a port on the server to a port inside the container.
Example: `-p 8080:80` -> server:8080 reaches nginx on container port 80.

## Exit codes
`Exited (0)` = clean stop. A non-zero code means the process failed.

## Default bridge network
Requests from the host appeared in nginx logs as 172.17.0.1, Docker's default bridge gateway.
