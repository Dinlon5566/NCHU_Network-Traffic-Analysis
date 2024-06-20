from dotenv import load_dotenv
import os

def printEnv():
    load_dotenv()
    # print all the environment variables
    print("Environment Variables:")
    print("DB_USER:", os.getenv("DB_USER"))
    print("DB_PASS:", os.getenv("DB_PASS"))
    print("DB_HOST:", os.getenv("DB_HOST"))
    print("DB_PORT:", os.getenv("DB_PORT"))
