import os
import boto3
import json
import click


with open("keys.json", "r") as f:
    keys = json.load(f)
ACCESS_ID = keys["ACCESS_ID"]
SECRET_KEY = keys["SECRET_KEY"]


@click.command()
@click.pass_context
@click.option('--directory', 'local_directory', help='local directory', required=True)
@click.option('--bucket', 'bucket', help='space bucket', required=True)
@click.option('--destination', thelp='destination file', required=True)
def export_to_space(
    ctx: click.Context,
    local_directory: str,
    bucket: str,
    destination: str
):

    client = boto3.client('s3',
                          region_name='fr1',
                          endpoint_url='https://fra1.digitaloceanspaces.com',
                          aws_access_key_id=ACCESS_ID,
                          aws_secret_access_key=SECRET_KEY)
    # enumerate local files recursively
    for root, dirs, files in os.walk(local_directory):
        for filename in files:

            local_path = os.path.join(root, filename)

            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(destination, relative_path)
            client.upload_file(local_path, bucket, s3_path, ExtraArgs={'ACL': 'public-read'})


if __name__ == "__main__":
    export_to_space()
