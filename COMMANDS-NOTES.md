# Commands Notes

## Linux
| Command | Meaning |
|---|---|
| `pwd` | Print current directory |
| `ls -la` | List all files (long format, including hidden) |
| `mkdir -p dir` | Create a directory, no error if it exists |
| `cat file` | Print a file |
| `grep -n text file` | Search a file, show line numbers |
| `sudo` | Run a command as administrator |
| `dnf install -y pkg` | Install a package on Amazon Linux 2023 |

## systemd
| Command | Meaning |
|---|---|
| `sudo systemctl enable --now docker` | Start now and on every boot |
| `sudo systemctl status docker --no-pager` | Check service state |

## Git
| Command | Meaning |
|---|---|
| `git init -b main` | Create a repo with a main branch |
| `git add <files>` | Stage files for commit |
| `git commit -m "msg"` | Save a snapshot |
| `git commit --amend --reset-author` | Rewrite the last commit's author (before pushing only) |
| `git log --oneline` | Show history |

## Docker (container basics)
| Command | Meaning |
|---|---|
| `docker run -d --name web1 -p 8080:80 nginx` | Start nginx in background, host port 8080 -> container port 80 |
| `docker ps` / `docker ps -a` | List running / all containers |
| `docker logs web1` (`--tail 5`, `-f`) | Show container output (last 5 lines / follow live) |
| `docker exec -it web1 bash` | Open an interactive shell inside a running container |
| `docker stop web1` | Gracefully stop a container |
| `docker rm web1` | Remove a stopped container |
