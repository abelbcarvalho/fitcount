from decimal import Decimal

from src.models.fit_calc import FitCalc

from src.utilities.enum.enums import ManGeb, WomanGeb, Gender


class Calories:
    def __init__(self) -> None:
        self._geb: Decimal = Decimal("0")

    @property
    def geb(self) -> Decimal:
        return self._geb

    async def man_geb(self, fit_calc: FitCalc) -> None:
        self._geb = (
            ManGeb.f1.value * fit_calc.weight +
            ManGeb.f2.value + fit_calc.height +
            ManGeb.f3.value * fit_calc.age +
            ManGeb.f4.value
        )

    async def woman_geb(self, fit_calc: FitCalc) -> None:
        self._geb = (
            WomanGeb.f1.value * fit_calc.weight +
            WomanGeb.f2.value + fit_calc.height +
            WomanGeb.f3.value * fit_calc.age +
            WomanGeb.f4.value
        )

    async def energy_expenditure(self, fit_calc: FitCalc) -> Decimal:
        {
            Gender.MALE.value: await self.man_geb(fit_calc),
            Gender.FEMALE.value: await self.woman_geb(fit_calc),
        }.get(fit_calc.gender, None)

        calories = self.geb * fit_calc.level.value

        return calories
