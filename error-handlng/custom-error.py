#!/usr/bin/env python3


class ElectricalError(Exception):

    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f'The {self.device} is {self.problem}'


class PlumbingError(Exception):

    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f'The {self.device} is {self.problem}'


def cause_error(error_type):

    if error_type == 'electrical':
        raise ElectricalError('circuit breaker', 'overloaded')
    elif(error_type == 'plumbing'):
        raise PlumbingError('dishwasher', 'spraying water')
    else:
        raise Exception('A generic household problem')


def main():
    try:
        cause_error('electrical')
    except ElectricalError as e:
        print(e)
        print('Call the electrician')
    except PlumbingError as e:
        print(e)
        print('Call the plumber')
    except:
        print('Call the landlord')
    else:
        print('Everything is fine')


if __name__ == '__main__':
    main()
