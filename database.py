from sqlalchemy import create_engine
import os

# Create a connection string
connection_string = os.environ['DB_CONNECTION_STRING']

# Create an engine
engine = create_engine((connection_string),
      connect_args={
        "ssl": {
            "ssl_ca": "ca.pem",
            "ssl_cert": "client-cert.pem",
            "ssl_key": "client-key.pem"
        }
    }
)

# Use the engine to connect to the database
#connection = engine.connect()



