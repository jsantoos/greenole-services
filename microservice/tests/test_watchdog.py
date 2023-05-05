import unittest.mock as mock
import requests

from microservice.app.watchdog import (
    check_services_status,
    send_discord_notification,
    SERVICES,
)


@mock.patch("requests.post")
def test_check_services_status(mock_requests_post):
    # Define um mock para a função requests.get(), retornando um status code 200
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        check_services_status()

    # Verifica que a função requests.get() foi chamada para cada serviço definido em SERVICES
    assert mock_get.call_count == len(SERVICES)

    # Verifica que a função requests.post() não foi chamada
    mock_requests_post.assert_not_called()

    # Define um mock para a função requests.get(), retornando um status code diferente de 200
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        check_services_status()

    # Verifica que a função requests.post() foi chamada uma vez para cada serviço com status diferente de 200
    mock_requests_post.assert_called_once_with(
        "http://discord-webhook-url.com",
        json={"content": "O serviço Microservice está fora do ar."},
    )
