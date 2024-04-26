read -e -p "Enter path (full qualififed) to Dockerfile: " path
read -p "Enter a name: " name

echo "Building docker image now..."
docker build -t $name:1.0.0 $path

echo "Done!"

echo "Saving image to file..."
docker save --output $path/$name.tar $name:1.0.0
echo "Done!"

echo "Cleaning up..."
docker image rm $name:1.0.0
echo Done!
