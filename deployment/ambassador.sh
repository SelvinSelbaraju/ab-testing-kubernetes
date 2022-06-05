helm repo add datawire https://www.getambassador.io
helm upgrade --install ambassador datawire/ambassador \
  --set service.type=ClusterIP \
  --set replicaCount=1 \
  --set crds.keep=false \
  --set enableAES=false \
  --namespace ambassador