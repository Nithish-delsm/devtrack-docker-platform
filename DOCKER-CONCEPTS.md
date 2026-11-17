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

## Volumes
A container's filesystem is deleted with the container. A named volume lives outside it (`-v name:/path`), so Postgres data survives `docker rm`. `docker compose down` keeps volumes; `down -v` deletes them.

## Networking
Default bridge: no name lookup. A user-defined bridge (or Compose network) lets containers find each other by service name through Docker's DNS. Only published ports (`-p`) are reachable from outside; `127.0.0.1:8000:8000` limits access to the server itself.

## Compose
One file describes services, networks and volumes. `depends_on` with a `healthcheck` controls start order. `restart: unless-stopped` restarts containers after crashes and reboots.

## Caching with Redis
Cache-aside: read Redis; on a miss read Postgres and store the result with a TTL; delete the key when the data changes. The app must keep working when Redis is down.

## Secrets
Passwords live in `.env` (git-ignored, chmod 600) and are passed with `env_file`. They are never baked into images or committed.

## Reverse proxy and network isolation
Nginx is the only service with a published port. The API is reachable only through it on the `frontend` network. The `backend` network is `internal: true`, so Postgres and Redis have no route to the internet. Compose healthchecks chain the start order: db/redis -> api -> nginx.
