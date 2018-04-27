import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print bucket.name
    print "\n"
    for item in bucket.objects.all():
        print "\t%s" % item.key
