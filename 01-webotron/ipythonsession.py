# coding: utf-8
import boto3
session = boto3.Session(profile_name='default')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucjet='rmn-automatingaws')
new_bucket = s3.create_bucket(Bucket='rmn-automatingaws')
new_bucket = s3.create_bucket(Bucket='rmn-automatingaws', CreateBucketConfiguration={'LocationConstraint': 'ap-southeast-2'})
for bucket in s3.buckets.all():
    print(bucket)
    
ec2_client = session.client
ec2_client = session.client('ec2')
