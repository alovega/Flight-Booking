import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Flight
from .utility import get_request_data


class BookingFlight(object):
    @staticmethod
    @csrf_exempt
    def post_flight(request):
        try:
            data = get_request_data(request)
            print(data)
            beginning = data.get('from')
            destination = data.get('to')
            start_date = datetime.datetime.strptime(data.get('start'), "%m/%d/%Y")
            return_date = datetime.datetime.strptime(data.get('return'), "%m/%d/%Y")
            adult = data.get('adults')
            children = data.get('child')

            flight_data = {
                'beginning': beginning,
                'destination': destination,
                'start_date': start_date,
                'return_date': return_date,
                'adult': adult,
                'children': children
            }

            user_flight = Flight.objects.create(**flight_data)

            data = {
                "message": f"New item added to Flight booking with id: {user_flight.id}"
            }
            return JsonResponse(data, status=201)
        except Exception as e:

            data = {
                'message': f' Error, {e} '
            }
            return JsonResponse(data, status=400)

    @staticmethod
    @csrf_exempt
    def get_flight(request):
        try:
            flights_count = Flight.objects.count()
            flights = Flight.objects.all()

            flights_data = []
            for flight in flights:
                flights_data.append({
                    'to': flight.destination,
                    'from': flight.beginning,
                    'start_date': datetime.datetime.strftime(flight.start_date, "%m/%d/%Y"),
                    'return_date': datetime.datetime.strftime(flight.return_date, "%m/%d/%Y"),
                    'adults': flight.adult,
                    'child': flight.children
                })

            data = {
                'flights': flights_data,
                'count': flights_count,
            }

            return JsonResponse(data)
        except Exception as e:

            data = {
                'message': f' Error, {e} '
            }
            return JsonResponse(data, status=400)

    @staticmethod
    @csrf_exempt
    def update_flight(request):
        try:
            data = get_request_data(request)
            flight_id = data.get('flight_id')
            flight = Flight.objects.get(id=flight_id)
            flight.beginning = data.get('from')
            flight.destination = data.get('to')
            flight.start_date = datetime.datetime.strptime(data.get('start'), "%m/%d/%Y")
            flight.return_date = datetime.datetime.strptime(data.get('return'), "%m/%d/%Y")
            flight.adult = data.get('adults')
            flight.children = data.get('child')
            flight.save()

            data = {
                'message': f'Flight {flight_id} has been updated'
            }

            return JsonResponse(data)
        except Exception as e:

            data = {
                'message': f' Error, {e} '
            }
            return JsonResponse(data, status=400)

    @staticmethod
    @csrf_exempt
    def delete_flight(request):
        try:
            data = get_request_data(request)
            flight_id = data.get('flight_id')
            flight = Flight.objects.get(id=flight_id)
            flight.delete()

            data = {
                'message': f'Flight {flight_id} has been deleted'
            }

            return JsonResponse(data)

        except Exception as e:

            data = {
                'message': f' Error, {e} '
            }
            return JsonResponse(data, status=400)