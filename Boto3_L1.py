#!/usr/bin/env python3.7

#Creating AWS S3 Bucket using Boto3

import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("jeffreylearningboto3withluit")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint':'us-east-1'
    },
    
)

print(response)