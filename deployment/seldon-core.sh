helm upgrade --install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set ambassador.enabled=true \
    --namespace seldon-system