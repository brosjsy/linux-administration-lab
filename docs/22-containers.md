# 22. Containers: Docker and Podman

Level: intermediate

```bash
sudo apt install docker.io && sudo usermod -aG docker $USER   # Rocky: dnf install podman
docker run -d --name web -p 8080:80 nginx:stable
docker ps; docker logs -f web; docker exec -it web sh
docker stats --no-stream
docker stop web && docker rm web
docker system df; docker system prune     # free space (ticket: disk full on a Docker host)
```
`compose.yaml`
```yaml
services:
  web:
    image: nginx:stable
    ports: ["8080:80"]
    volumes: ["./html:/usr/share/nginx/html:ro"]
    restart: unless-stopped
```
`docker compose up -d`

Security basics: do not run containers as root when avoidable, pin image versions, never mount `/var/run/docker.sock` into untrusted containers, membership of the `docker` group equals root access.
