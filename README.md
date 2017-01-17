# serverless-starter
Starter repository for serverless functions

# Requirements:
1. Install serverless framework:
```bash
npm install serverless -g
```

2. Create AWS credentials for test account (ask DevOps if you don't have them yet).

3. Add credentials to `~/.aws/credentials`:
```bash
[default]
aws_access_key_id=ACCESS_KEY
aws_secret_access_key=SECRET_KEY
```

# Deployment

- deploy whole service:
```bash
cd sample_service
sls deploy
```

- deploy single function:
```bash
cd sample_service
sls deploy -f read
```

- check logs:
```bash
cd sample_service
sls logs -f read -t
```

For more sls options, please go to: https://serverless.com/framework/docs/
