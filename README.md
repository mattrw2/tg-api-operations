
## About The Project

I created this project to give TeamGantt users some boilerplate python code to make it easier to get started with the API.

## Getting Started

### Prerequisites

* python3

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mattrw2/tg-api-operations.git
   ```
1. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
1. Retrieve your client_id and client_secret from https://app.teamgantt.com/admin/app-clients
1. Enter your client_id, client_secret, and TeamGantt credentials in `example_config.py` and save it as `config.py`
   ```py
   client_id='xxxxxxx'
   client_secret = 'xxxxxxxx'
   username = 'matt@example.com'
   password = 'password'   
   ```
## Usage
* Import the API connector class and initialize it.

    ```py
    from tg import TG

    obj = TG()
    ```    
* Use the connector object to get
