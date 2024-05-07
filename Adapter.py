class CelsiusTemperature:
    def __init__(self, temperature):
        self.temperature = temperature
    def get_temperature(self):
        return self.temperature
# Adaptér
class FahrenheitTemperatureAdapter:
    def __init__(self, celsius_temperature):
        self.celsius_temperature = celsius_temperature
    def get_temperature(self):
        # Převod teploty z Celsia na Fahrenheita
        celsius_temp = self.celsius_temperature.get_temperature()
        fahrenheit_temp = (celsius_temp * 9 / 5) + 32
        return fahrenheit_temp
# Testování
def main():
    celsius_temp = CelsiusTemperature(25)  # Vytvoření instance teploty v Celsiu
    fahrenheit_adapter = FahrenheitTemperatureAdapter(celsius_temp)  # Vytvoření instance adaptéru s teplotou v Celsiu
    print("Temperature in Fahrenheit:", fahrenheit_adapter.get_temperature())  # Výpis teploty v Fahrenheitech
if __name__ == "__main__":
    main()