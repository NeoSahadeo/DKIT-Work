# devops-lab-3

Devops Lab 3 Pipeline

# Files explained

- `dockerfile-python` is the Python deployment image
- `dockerfile-runner1` is the first gitlab runner that runs Python
- `dockerfile-runner2` is the second gitlab runner that runs gitlab:Alpine
- `compose.yml` is the compose file for the gitlab-runners
- `compose-python.yml` is the compose file for the Python deployment
- `build.sh` is the quick-and-dirty build script to automate build-up and take-down for the gitlab-runners
- `.gitlab-ci.yml` is my gitlab ci script

## A few liberties taken

I found it easier to run docker images that ran
gitlab-runner over running it directly on the VM.

### This caused a few problems

The problem I was stuck with for quite a bit was
running the docker builds in the runner. It was
essentially a docker in a docker.

Many, many hours later I found (building docker images in docker)[https://docs.gitlab.com/ee/ci/docker/using_docker_build.html].
I resolved the issue by running the runner with the shell as
the executer. And by installing docker and docker-compose
on the image.

Everything after that was straight forward.

Well... almost.

`COPY templates` didn't work, it didn't copy the folder contents.
I found `ADD` which fixed that.
