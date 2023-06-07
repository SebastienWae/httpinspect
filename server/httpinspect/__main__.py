from sys import exit, stderr

import uvicorn

if __name__ == "__main__":
    hostname = "localhost"

    if hostname is not None:
        uvicorn.run(
            "httpinspect.app:server",
            host=hostname,
            port=8000,
            reload=True,
        )
    else:
        print("HOSTNAME environment variable not set.", stderr)
        exit(1)
