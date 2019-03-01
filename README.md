# automatingaws

*Automate AWS with Python*

This Repo will be host to experimentation with Python and its use to automate AWS tasks

Use pipenv(https://pipenv.readthedocs.io/en/latest/) for managing packages and dependencies

Use boto3(https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to automate AWS

-  typically you want to use the 'ServiceResource' when dealing with a Service
-  if for some reason the ServiceRecource isn't created - you can work with a low-lvel 'Client' object
	NOTE: There is a one-to-one mapping between Client and API calls allowed against a service.

## 01-webotron
This is a script that will sync a local directory to an S3 bucket
and it will optionally configure Route53 and cloudfront as well
