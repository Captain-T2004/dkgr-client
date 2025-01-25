# dkgr-client

## Installation

```bash
pip install dkgr-client
```

## Usage

```python
from dkgr-client import ValidationClient

try:
    # Initialize the client
    client = ValidationClient(
        api_key='your_api_key', 
        base_url='https://api.example.com'
    )
    
    # Start a new event
    client.start_event()

    # Validate
    results = client.validate(
        type,
        text,
    )

    # Extract useful info from results
    client.humaize_response(results))

    # Close the client
    client.close()
```