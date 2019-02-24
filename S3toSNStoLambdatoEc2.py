import paramiko
import base64
import boto3
def lambda_handler(event,context):
        s3 = boto3.resource('s3')
        s3.Bucket('xxxxxxxxxx').download_file('xxxxxx.pem','/tmp/xxxxx.pem')
        k = paramiko.RSAKey.from_private_key_file("/tmp/20181216.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print "connecting"
        c.connect( hostname = "ec2-5xxxxxxxxxxxxxxamazonaws.com", username = "ec2-user", pkey = k )
        commands = ["/home/ec2-user/helloworld.sh","/home/ec2-user/goodbye.sh"]
        for x in commands:
                print("Executing".format(x))
                stdin , stdout, stderr = c.exec_command(x)
                print stdout.read()
                print(stderr.read())
        c.close()

