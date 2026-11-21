import boto3


def main() -> None:
    buckets = boto3.client("s3").list_buckets()["Buckets"]
    if not buckets:
        print("No S3 buckets found.")
        return

    for bucket in buckets:
        print(bucket["Name"])


if __name__ == "__main__":
    main()
