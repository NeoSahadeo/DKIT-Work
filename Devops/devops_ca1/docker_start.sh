echo "Cleaning"
docker compose rm -sf
docker rmi app1
docker rmi app2
docker rmi nginx_lb

echo "Building"
docker build -t app1 --file dockerfile_app1 .
docker build -t app2 --file dockerfile_app2 .
docker build -t nginx_lb --file dockerfile_nginx_lb .

echo "Composing"
docker compose up -d
