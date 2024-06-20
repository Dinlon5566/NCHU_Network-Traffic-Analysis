from dotenv import load_dotenv
import os


def check_and_set_env_var(var_name, default_value=None):
    value = os.getenv(var_name)
    if value is None:
        if default_value:
            value = default_value
        else:
            print(f"Environment variable {var_name} is not set.")
            value = input(f"請輸入 {var_name}: ")
        with open('.env', 'a') as env_file:
            env_file.write(f"{var_name}={value}\n")
        load_dotenv()  # Reload environment variables
    return value


def printEnv():
    load_dotenv()
    print("Environment Variables:")
    db_user = check_and_set_env_var("DB_USER")
    db_pass = check_and_set_env_var("DB_PASSWORD")
    db_host = check_and_set_env_var("DB_HOST")
    db_port = check_and_set_env_var("DB_PORT")

    print("DB_USER:", db_user)
    print("DB_PASSWORD:", db_pass)
    print("DB_HOST:", db_host)
    print("DB_PORT:", db_port)


if __name__ == "__main__":
    printEnv()
