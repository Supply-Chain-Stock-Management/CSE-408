#!/bin/bash

helm repo add kong https://charts.konghq.com
helm repo update
echo "Kong helm repo added and updated"

helm install kong kong/ingress -n kong --create-namespace
echo "Kong helm chart installed with kong namespace"