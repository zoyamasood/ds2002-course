#!/usr/bin/python3

import boto3
s3 = boto3.client('s3', region_name='us-east-1')

response = s3.list_buckets()

for r in response['Buckets']:
        print(r['Name'])

#create presigned url function: 
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

#put object function:
bucket_name = 'ds2002-rpk4wp'
local_file = 'project/apple_logo.png'
acl = 'public-read'

def put_object(bucket_name, local_file, object_key=none, acl=none):
	if object_key=none
		object_key=local_file
	response = s3.put_object(
		Body = local_file,
		Bucket = bucket_name, 
		Key = object_key
		acl=acl
		)
		return response
