#!/bin/bash

cluster_name=$1
if [ -z "$cluster_name" ]; then
    echo "No cluster name provided."
    exit 1
fi


eksctl create cluster --name $cluster_name --region ap-south-1
echo "cluster is created successfully if [✓]  EKS cluster $cluster_name in ap-south-1 region is ready"
echo "eksctl created a kubectl config file in ~/.kube"
echo "view the AWS CloudFormation stack named eksctl-$cluster_name-cluster in the AWS CloudFormation console at https://console.aws.amazon.com/cloudformation"