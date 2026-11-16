# Troubleshooting Log

| Error | Root cause | Fix |
|---|---|---|
| `git@github.com: Permission denied (publickey)` | SSH public key not added to GitHub | Generate ed25519 key, add the .pub contents in GitHub Settings -> SSH keys, test with `ssh -T git@github.com` |
| `Author identity unknown` / wrong committer email | `git config user.name/email` never set | Set both, then `git commit --amend --reset-author` (before pushing) |
| `error: unknown switch '.'` after `git status -sb.` | Stray full stop typed after the flags | Remove the typo |
| `"docker exec" requires at least 2 arguments` | Ran `docker exec` without container and command | `docker exec -it <container> bash` |
| `rm: missing operand` / `stop: command not found` | Typed Linux `rm` or bare `stop` instead of `docker rm` / `docker stop` | Docker commands always start with `docker` |
| `-p: command not found` | Typed a flag as if it were a command | Flags belong after a command, e.g. `docker run -p 8080:80 nginx` |
