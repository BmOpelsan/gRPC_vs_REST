import grpc
from concurrent import futures
import temperature_pb2
import temperature_pb2_grpc

class TemperatureService(temperature_pb2_grpc.TemperatureConverterServicer):
    def ToCelsius(self, request, context):
        celsius = (request.fahrenheit - 32) * 5 / 9
        return temperature_pb2.CelsiusResponse(celsius=round(celsius, 2))

    def ToFahrenheit(self, request, context):
        fahrenheit = request.celsius * 9 / 5 + 32
        return temperature_pb2.FahrenheitResponse(fahrenheit=round(fahrenheit, 2))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    temperature_pb2_grpc.add_TemperatureConverterServicer_to_server(TemperatureService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер запущен на порту 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
