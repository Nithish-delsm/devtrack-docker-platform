# Troubleshooting Log

| Error | Root cause | Fix |
|---|---|---|
| `git@github.com: Permission denied (publickey)` | SSH public key not added to GitHub | Generate ed25519 key, add the .pub contents in GitHub Settings -> SSH keys, test with `ssh -T git@github.com` |
| `Author identity unknown` / wrong committer email | `git config user.name/email` never set | Set both, then `git commit --amend --reset-author` (before pushing) |
| `error: unknown switch '.'` after `git status -sb.` | Stray full stop typed after the flags | Remove the typo |
| `"docker exec" requires at least 2 arguments` | Ran `docker exec` without container and command | `docker exec -it <container> bash` |
| `rm: missing operand` / `stop: command not found` | Typed Linux `rm` or bare `stop` instead of `docker rm` / `docker stop` | Docker commands always start with `docker` |
| `-p: command not found` | Typed a flag as if it were a command | Flags belong after a command, e.g. `docker run -p 8080:80 nginx` |
| `compose build requires buildx 0.17.0 or later` on `docker compose up --build` | Compose plugin v5 needs a newer buildx plugin than the one shipped with the AL2023 docker package | Install the latest buildx binary into /usr/local/lib/docker/cli-plugins/docker-buildx and `chmod +x` it |
| `__pycache__` copied into image even though `.dockerignore` listed `__pycache__/` | In .dockerignore a bare pattern only matches the top-level folder (unlike .gitignore); nested folders need `**/` | Use `**/__pycache__` and `**/*.pyc`, rebuild, verify with `docker run --rm IMAGE ls -A /code/app` |
