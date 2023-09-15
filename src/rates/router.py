from fastapi import APIRouter, Query

from src.config import CURRENCY_APY_KEY
from src.rates.schemas import Result
from src.rates.utils import get_conversion

router = APIRouter(
    prefix='/rates',
    tags=['Rates']
)


@router.get('')
async def rates(
        from_: str = Query(
            alias='from',
            description="Исходная валюта",
            max_length=3,
            regex="^[A-Z]{3}$"
        ),
        to: str = Query(
            description="Целевая валюта",
            max_length=3,
            regex="^[A-Z]{3}$"
        ),
        value: float = Query(
            description="Сумма для конвертации"
        ),
) -> Result:
    """Конвертирует выбранную валюту"""

    result = get_conversion(
        api_key=CURRENCY_APY_KEY,
        from_=from_,
        to=to,
        value=value
    )
    return result
