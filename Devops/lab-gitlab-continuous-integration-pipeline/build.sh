echo "Cleaning"
docker compose down
docker image rm runner1
docker image rm runner2

echo "Building images"
docker build -t runner1 --file dockerfile-runner1 .
docker build -t runner2 --file dockerfile-runner2 .

# Add compose?
docker compose up -d

echo "Done!"
