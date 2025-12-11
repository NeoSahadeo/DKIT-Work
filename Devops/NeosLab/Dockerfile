FROM gitlab/gitlab-runner:alpine

RUN <<EOF
gitlab-runner register \
	--non-interactive \
	--executor "docker" \
  --docker-image alpine:latest \
  --description "docker-runner" \
	--url https://gitlab.comp.dkit.ie \
	--token glrt-xwLmQqpi7BhcKu227iCi
EOF
