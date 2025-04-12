import os
import json
import boto3
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize the Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'  # Change this to your preferred region
)

def invoke_model(prompt, model_id="amazon.nova-pro-v1:0"):
    """
    Invoke a Bedrock model with the given prompt.
    
    Args:
        prompt (str): The input prompt for the model
        model_id (str): The ID of the model to use
        
    Returns:
        str: The model's response
    """
    try:
        # Prepare the request body for Nova Pro
        request_body = {
            "messages": [{
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }]
        }
        body = json.dumps(request_body)
        logger.debug(f"Request body: {body}")
        
        # Invoke the model
        response = bedrock.invoke_model(
            modelId=model_id,
            body=body
        )
        
        # Parse the response
        response_body = json.loads(response.get('body').read())
        logger.debug(f"Response body: {response_body}")
        
        if response_body and 'output' in response_body:
            return response_body['output']['message']['content'][0]['text']
        logger.error(f"Unexpected response format: {response_body}")
        return None
    
    except Exception as e:
        logger.error(f"Error invoking model: {str(e)}", exc_info=True)
        return None

def main():
    # Example usage
    prompt = "What is AWS Bedrock?"
    response = invoke_model(prompt)
    
    if response:
        print("\nModel Response:")
        print(response)
    else:
        print("Failed to get response from the model")

if __name__ == "__main__":
    main() 