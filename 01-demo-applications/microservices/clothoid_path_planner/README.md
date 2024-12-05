# Clothoid Microservice
This microservice calculates a clothoid from a start to a target position.

### Build

Run by docker-compose:
```
docker-compose up
```

Or you can build your own python virtual environment, install all dependencies and run it in your host machine.

- Creat python virtual environment
    ```
    python -m venv osmenv
    osmenv\Scripts\activate.bat
    # or
    osmenv\Scripts\Activate.ps1
    ```

- Install packages:
    ```
    python -m pip install -r requirements.txt
    ```
- Run:
    ```
    python ./src/service.py
    ```
