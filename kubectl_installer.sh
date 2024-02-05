#!/bin/bash

# Check if kubectl is already installed
if command -v kubectl &>/dev/null; then
    echo "kubectl is already installed."
    exit 0
fi

# Define the desired kubectl version
KUBECTL_VERSION="1.29.0"

# Download the kubectl binary
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/${KUBECTL_VERSION}/2024-01-04/bin/linux/amd64/kubectl
echo "Downloaded kubectl binary"

# Verify checksum
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/${KUBECTL_VERSION}/2024-01-04/bin/linux/amd64/kubectl.sha256
echo "kubectl checksum downloaded"

# Verify the checksum
sha256sum -c kubectl.sha256
echo "Checksum verified if already seen kubectl: OK"

# Make the kubectl binary executable
chmod +x ./kubectl

# copy the kubectl binary to the folder in the PATH
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH

# Add the $HOME/bin path to the PATH environment variable
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc

# verify the version of kubectl
kubectl version --client

echo "kubectl installation completed successfully."

echo "modifying region-code and cluster needed later ig"
# aws eks update-kubeconfig --region region-code --name my-cluster
# region-code with the AWS Region that your cluster is in. Replace my-cluster with the name of your cluster.