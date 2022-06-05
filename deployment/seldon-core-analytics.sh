helm upgrade --install seldon-core-analytics seldon-core-analytics \
    --repo https://storage.googleapis.com/seldon-charts \
    --set grafana.adminPassword="admin" \
    --namespace seldon-system