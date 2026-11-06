# Containers (60 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T0283 | L2 | any | Download image alpine:3.20 | `docker pull alpine:3.20` | Podman accepts the same commands. |
| T0284 | L2 | any | Download image grafana/grafana:11.0.0 | `docker pull grafana/grafana:11.0.0` | Podman accepts the same commands. |
| T0285 | L2 | any | Download image nginx:stable | `docker pull nginx:stable` | Podman accepts the same commands. |
| T0286 | L2 | any | Download image postgres:16 | `docker pull postgres:16` | Podman accepts the same commands. |
| T0287 | L2 | any | Download image prom/prometheus:v2.53.0 | `docker pull prom/prometheus:v2.53.0` | Podman accepts the same commands. |
| T0288 | L2 | any | Download image redis:7 | `docker pull redis:7` | Podman accepts the same commands. |
| T0289 | L2 | any | Download image ubuntu:24.04 | `docker pull ubuntu:24.04` | Podman accepts the same commands. |
| T0290 | L2 | any | List all images with size | `docker images` | docker image prune removes dangling images. |
| T0291 | L2 | any | List running containers | `docker ps` | Add -a to include stopped ones. |
| T0292 | L2 | any | Open a shell in container alpine | `docker exec -it alpine sh` | Podman accepts the same commands. |
| T0293 | L2 | any | Open a shell in container grafana | `docker exec -it grafana sh` | Podman accepts the same commands. |
| T0294 | L2 | any | Open a shell in container nginx | `docker exec -it nginx sh` | Podman accepts the same commands. |
| T0295 | L2 | any | Open a shell in container postgres | `docker exec -it postgres sh` | Podman accepts the same commands. |
| T0296 | L2 | any | Open a shell in container prometheus | `docker exec -it prometheus sh` | Podman accepts the same commands. |
| T0297 | L2 | any | Open a shell in container redis | `docker exec -it redis sh` | Podman accepts the same commands. |
| T0298 | L2 | any | Open a shell in container ubuntu | `docker exec -it ubuntu sh` | Podman accepts the same commands. |
| T0299 | L2 | any | Run alpine:3.20 in the background as alpine | `docker run -d --name alpine --restart unless-stopped alpine:3.20` | Podman accepts the same commands. |
| T0300 | L2 | any | Run grafana/grafana:11.0.0 in the background as grafana | `docker run -d --name grafana --restart unless-stopped grafana/grafana:11.0.0` | Podman accepts the same commands. |
| T0301 | L2 | any | Run nginx:stable in the background as nginx | `docker run -d --name nginx --restart unless-stopped nginx:stable` | Podman accepts the same commands. |
| T0302 | L2 | any | Run postgres:16 in the background as postgres | `docker run -d --name postgres --restart unless-stopped postgres:16` | Podman accepts the same commands. |
| T0303 | L2 | any | Run prom/prometheus:v2.53.0 in the background as prometheus | `docker run -d --name prometheus --restart unless-stopped prom/prometheus:v2.53.0` | Podman accepts the same commands. |
| T0304 | L2 | any | Run redis:7 in the background as redis | `docker run -d --name redis --restart unless-stopped redis:7` | Podman accepts the same commands. |
| T0305 | L2 | any | Run ubuntu:24.04 in the background as ubuntu | `docker run -d --name ubuntu --restart unless-stopped ubuntu:24.04` | Podman accepts the same commands. |
| T0306 | L2 | any | Show disk used by Docker | `docker system df` | Images, containers, volumes and build cache. |
| T0307 | L2 | any | Show logs of container alpine | `docker logs --tail 100 -f alpine` | Podman accepts the same commands. |
| T0308 | L2 | any | Show logs of container grafana | `docker logs --tail 100 -f grafana` | Podman accepts the same commands. |
| T0309 | L2 | any | Show logs of container nginx | `docker logs --tail 100 -f nginx` | Podman accepts the same commands. |
| T0310 | L2 | any | Show logs of container postgres | `docker logs --tail 100 -f postgres` | Podman accepts the same commands. |
| T0311 | L2 | any | Show logs of container prometheus | `docker logs --tail 100 -f prometheus` | Podman accepts the same commands. |
| T0312 | L2 | any | Show logs of container redis | `docker logs --tail 100 -f redis` | Podman accepts the same commands. |
| T0313 | L2 | any | Show logs of container ubuntu | `docker logs --tail 100 -f ubuntu` | Podman accepts the same commands. |
| T0314 | L2 | any | Stop and remove container alpine | `docker stop alpine && docker rm alpine` | Podman accepts the same commands. |
| T0315 | L2 | any | Stop and remove container grafana | `docker stop grafana && docker rm grafana` | Podman accepts the same commands. |
| T0316 | L2 | any | Stop and remove container nginx | `docker stop nginx && docker rm nginx` | Podman accepts the same commands. |
| T0317 | L2 | any | Stop and remove container postgres | `docker stop postgres && docker rm postgres` | Podman accepts the same commands. |
| T0318 | L2 | any | Stop and remove container prometheus | `docker stop prometheus && docker rm prometheus` | Podman accepts the same commands. |
| T0319 | L2 | any | Stop and remove container redis | `docker stop redis && docker rm redis` | Podman accepts the same commands. |
| T0320 | L2 | any | Stop and remove container ubuntu | `docker stop ubuntu && docker rm ubuntu` | Podman accepts the same commands. |
| T0321 | L3 | any | Free disk space used by unused Docker data | `docker system prune -f` | Add -a --volumes only if you are sure. |
| T0322 | L3 | any | Inspect IP address of container alpine | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' alpine` | Podman accepts the same commands. |
| T0323 | L3 | any | Inspect IP address of container grafana | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' grafana` | Podman accepts the same commands. |
| T0324 | L3 | any | Inspect IP address of container nginx | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' nginx` | Podman accepts the same commands. |
| T0325 | L3 | any | Inspect IP address of container postgres | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres` | Podman accepts the same commands. |
| T0326 | L3 | any | Inspect IP address of container prometheus | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' prometheus` | Podman accepts the same commands. |
| T0327 | L3 | any | Inspect IP address of container redis | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' redis` | Podman accepts the same commands. |
| T0328 | L3 | any | Inspect IP address of container ubuntu | `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ubuntu` | Podman accepts the same commands. |
| T0329 | L3 | any | Limit container alpine to 1 CPU and 512 MB | `docker update --cpus 1 --memory 512m --memory-swap 512m alpine` | Podman accepts the same commands. |
| T0330 | L3 | any | Limit container grafana to 1 CPU and 512 MB | `docker update --cpus 1 --memory 512m --memory-swap 512m grafana` | Podman accepts the same commands. |
| T0331 | L3 | any | Limit container nginx to 1 CPU and 512 MB | `docker update --cpus 1 --memory 512m --memory-swap 512m nginx` | Podman accepts the same commands. |
| T0332 | L3 | any | Limit container postgres to 1 CPU and 512 MB | `docker update --cpus 1 --memory 512m --memory-swap 512m postgres` | Podman accepts the same commands. |
| T0333 | L3 | any | Limit container prometheus to 1 CPU and 512 MB | `docker update --cpus 1 --memory 512m --memory-swap 512m prometheus` | Podman accepts the same commands. |
| T0334 | L3 | any | Limit container redis to 1 CPU and 512 MB | `docker update --cpus 1 --memory 512m --memory-swap 512m redis` | Podman accepts the same commands. |
| T0335 | L3 | any | Limit container ubuntu to 1 CPU and 512 MB | `docker update --cpus 1 --memory 512m --memory-swap 512m ubuntu` | Podman accepts the same commands. |
| T0336 | L3 | any | Show resource usage of container alpine | `docker stats --no-stream alpine` | Podman accepts the same commands. |
| T0337 | L3 | any | Show resource usage of container grafana | `docker stats --no-stream grafana` | Podman accepts the same commands. |
| T0338 | L3 | any | Show resource usage of container nginx | `docker stats --no-stream nginx` | Podman accepts the same commands. |
| T0339 | L3 | any | Show resource usage of container postgres | `docker stats --no-stream postgres` | Podman accepts the same commands. |
| T0340 | L3 | any | Show resource usage of container prometheus | `docker stats --no-stream prometheus` | Podman accepts the same commands. |
| T0341 | L3 | any | Show resource usage of container redis | `docker stats --no-stream redis` | Podman accepts the same commands. |
| T0342 | L3 | any | Show resource usage of container ubuntu | `docker stats --no-stream ubuntu` | Podman accepts the same commands. |
