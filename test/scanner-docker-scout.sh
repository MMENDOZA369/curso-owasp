docker scout quickview
docker scout view --json \
  --output-file /tmp/scout.json \
  --dockerfile /tmp/Dockerfile \
  --image-name "$1" \
  --image-tag "$2" \
  --dockerfile-path /tmp
docker scout recommendations local://my-angular-app:latest