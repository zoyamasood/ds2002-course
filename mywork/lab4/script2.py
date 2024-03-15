#!/usr/bin/python3

import boto3
s3 = boto3.client('s3', region_name='us-east-1')

response = s3.list_buckets()

for r in response['Buckets']:
        print(r['Name'])

bucket_name = 'ds2002-rpk4wp'
object_name = 'project/google_logo.png'
expires_in = 604800

def create_presigned_url_expanded(bucket_name, object_name, expires_in=604800):
        response = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': object_name}, 
                ExpiresIn=expires_in
        )
print(create_presigned_url_expanded(bucket_name, object_name, expires_in=604800))

#https://ds2002-rpk4wp.s3.us-east-1.amazonaws.com/google_logo.png?X-Amz-Algorithm=A$

