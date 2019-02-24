import paramiko
import base64
import boto3
def lambda_handler(event,context):
        s3 = boto3.resource('s3')
        s3.Bucket('sparkscalap').download_file('20181216.pem','/tmp/20181216.pem')
        k = paramiko.RSAKey.from_private_key_file("/tmp/20181216.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print "connecting"
        c.connect( hostname = "ec2-52-10-86-65.us-west-2.compute.amazonaws.com", username = "ec2-user", pkey = k )
        commands = ["/home/ec2-user/helloworld.sh","/home/ec2-user/goodbye.sh"]
        for x in commands:
                print("Executing".format(x))
                stdin , stdout, stderr = c.exec_command(x)
                print stdout.read()
                print(stderr.read())
        c.close()

