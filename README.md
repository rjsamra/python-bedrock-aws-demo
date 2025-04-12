# AWS Bedrock Python Demo

This is a simple demo project that shows how to use AWS Bedrock with Python.

## Prerequisites

- Python 3.7 or higher
- AWS account with Bedrock access
- AWS credentials configured (either through AWS CLI or environment variables)

## Setup

1. Clone this repository
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your AWS credentials:
   - Option 1: Using AWS CLI
     ```bash
     aws configure
     ```
   - Option 2: Using environment variables
     Create a `.env` file with:
     ```
     AWS_ACCESS_KEY_ID=your_access_key
     AWS_SECRET_ACCESS_KEY=your_secret_key
     AWS_DEFAULT_REGION=your_region
     ```

## Usage

Run the demo script:

```bash
python bedrock_demo.py
```

The script will:

1. Initialize the Bedrock client
2. Send a sample prompt to the model
3. Display the model's response

## Customization

You can modify the following parameters in `bedrock_demo.py`:

- `model_id`: Change the model you want to use (default: "anthropic.claude-v2")
- `max_tokens_to_sample`: Adjust the maximum length of the response
- `temperature`: Control the randomness of the output (0.0 to 1.0)
- `top_p`: Control the diversity of the output (0.0 to 1.0)

## Available Models

AWS Bedrock supports several foundation models. Some popular ones include:

- anthropic.claude-v2
- anthropic.claude-instant-v1
- amazon.titan-text-lite-v1
- amazon.titan-text-express-v1

## Security

Never commit your AWS credentials to version control. Always use environment variables or AWS CLI configuration for managing credentials.
