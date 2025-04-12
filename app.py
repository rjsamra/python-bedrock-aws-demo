from flask import Flask, render_template, request, jsonify
import boto3
import json
import os
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        # Prepare the request body for Nova Pro
        request_body = {
            "messages": [{
                "role": "user",
                "content": [
                    {"text": prompt}
                ]
            }]
        }
        
        logger.debug(f"Request body: {json.dumps(request_body)}")

        # Invoke the model
        response = bedrock.invoke_model(
            modelId='amazon.nova-pro-v1:0',
            body=json.dumps(request_body)
        )

        # Parse the response
        response_body = json.loads(response.get('body').read())
        logger.debug(f"Response body: {response_body}")
        
        if response_body and 'output' in response_body:
            generated_text = response_body['output']['message']['content'][0]['text']
        else:
            generated_text = 'No response generated'
            logger.error(f"Unexpected response format: {response_body}")

        return jsonify({'response': generated_text})

    except Exception as e:
        logger.error(f"Error invoking model: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 