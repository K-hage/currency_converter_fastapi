import requests
from fastapi import HTTPException

from src.rates.schemas import Result


def get_conversion(
        api_key: str,
        from_: str,
        to: str,
        value: float
) -> Result:
    """
    Конвертирует валюту

    :param api_key: YOUR_API_KEY для exchangerate-api.com
    :param from_: базовая валюта
    :param to:  целевая валюта
    :param value: сумма для преобразования
    :return: преобразованная сумма
    """

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_}/{to}/{value}'

    try:
        response = requests.get(url)
        data = response.json()
        if data.get('result') == 'error':
            raise HTTPException(
                status_code=404, detail=data.get('error-type')
            )
        result = Result(result=data.get('conversion_result'))
        return result

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=500, detail='Ошибка со стороны сервера'
        )
