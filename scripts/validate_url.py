import requests

def validate_url(url):

    response = requests.get(url)

    if response.ok:
        print(f"""
        Requisição bem sucedida.
        HTTP status {response.status_code} {response.reason}
        """)
        return response.content

    else:
        print(f"""
        Requisição não foi bem sucedida
        HTTP status {response.status_code} {response.reason}
        """)
        return

if __name__ == "__main__":
    validate_url()