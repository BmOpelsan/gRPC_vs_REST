import grpc
import temperature_pb2
import temperature_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = temperature_pb2_grpc.TemperatureConverterStub(channel)

        # Пример запроса: Фаренгейт в Цельсий
        response = stub.ToCelsius(temperature_pb2.FahrenheitRequest(fahrenheit=98.6))
        print(f"98.6°F = {response.celsius}°C")

        # Пример запроса: Цельсий в Фаренгейт
        response = stub.ToFahrenheit(temperature_pb2.CelsiusRequest(celsius=37))
        print(f"37°C = {response.fahrenheit}°F")

if __name__ == '__main__':
    run()
