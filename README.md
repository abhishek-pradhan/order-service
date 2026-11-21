# order-service

A Python project managed with [uv](https://docs.astral.sh/uv/). It currently
includes a basic greeting command and a command for listing Amazon S3 buckets.

## Requirements

- Python 3.15 or later
- uv
- AWS credentials configured through the standard boto3 credential chain to use
  the S3 command

## Setup

Install the project and its dependencies:

```bash
uv sync
```

## Commands

Print a greeting:

```bash
uv run order-service
```

List the bucket names visible to the configured AWS identity:

```bash
uv run list-s3-buckets
```

The AWS identity needs permission to call `s3:ListAllMyBuckets`. Select a
configured AWS profile like this:

```bash
AWS_PROFILE=my-profile uv run list-s3-buckets
```

## Development

Run the linter:

```bash
uv run ruff check .
```

Run the test suite:

```bash
uv run pytest
```

## Project layout

```text
src/order_service/
├── __init__.py          # Greeting command
└── list_s3_buckets.py   # S3 bucket listing command
```