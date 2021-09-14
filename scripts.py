import docker

def main():
    client = docker.from_env()
    container = client.containers.run(
        image="uv",
        ports={'22/tcp': 5000},
        detach=True,
        stdin_open=True,
        auto_remove=True
    )
    print(container.id)

    stop = input()

    for container in client.containers.list():
        print(container.id)
        container.stop()

# main()