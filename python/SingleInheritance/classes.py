"""
 this module contains all classes we need for the project  like
 - Resource
 - CPU
 - Storage
 - HDD
 -SDD
"""
import numbers

from mpmath import power


class Resource:
    def __init__(self, name, manufacture, total, allocated):
        self.name = name
        self.manufacture = manufacture
        self._total = Resource.check_valid_int(total, 1, float('inf'))
        self._allocated = Resource.check_valid_int(allocated, 1, self.total)

    @staticmethod
    def check_valid_int(number, start, end):
        """
        this function checks
        1. the type of the number
        2. number lies in the range [start,end]
        Args:
            number(int):  the value you want to validate
            start(int):  the start of the period
            end (int):  end of the period

        Returns:
            number : if the number is valid
        Raises:
            ValueError : if the number not in the specified range
        """

        if not isinstance(number, numbers.Integral):
            raise TypeError("number must be Integral")
        if not (start <= number <= end):
            raise ValueError(f" number must be in range[{start} , {end}]")

        return number

    @property
    def category(self):
        return self.__class__.__name__.lower()

    @property
    def total(self):
        """

        Returns:
            int : number of total resources

        """
        return self._total

    @property
    def allocated(self):
        """

        Returns:
            int : number of allocated resources
        """
        return self._allocated

    @property
    def remaining(self):
        """

        Returns:
            int : number of available resources for use
        """
        return self.total - self.allocated

    def freed_up(self, n):
        """
        free n resources
        Args:
            n (int): number of resources to free

        Returns:
            None
        """
        # cannot free up more than the allocated
        Resource.check_valid_int(n, 1, self.allocated)
        self._allocated -= n

    def died(self, n):
        """
        kill n resources
        Args:
            n(int): The number of resources to terminate

        Returns:

        """

        # cannot be > allocated
        Resource.check_valid_int(n, 1, self.allocated)
        self._allocated -= n
        # cannot be > total
        Resource.check_valid_int(n, 1, self.total)
        self._total -= n

    def __str__(self):
        return self.name

    def __repr__(self):
        return (
            f'{self.__class__.__name__}(name={self.name} ,manufacture ={self.manufacture}'
            f'total ={self.total} , allocated ={self.allocated})'
        )

    def purchase(self, n):
        # cannot be 0
        Resource.check_valid_int(n, 1, float('inf'))
        self._total += n


class CPU(Resource):
    def __init__(self, name, manufacture, total, allocated, cores: int, sockets: int, power_watts: int):
        super().__init__(name, manufacture, total, allocated)
        self.cores = Resource.check_valid_int(cores, 1 , float('inf'))
        self.sockets = Resource.check_valid_int(sockets, 1 , float('inf'))
        self.power_watts = Resource.check_valid_int(power_watts, 1 , float('inf'))





class Storage(Resource):
    def __init__(self, name, manufacture, total, allocated, capacity):
        self.capacity = capacity
        super().__init__(name, manufacture, total, allocated)


class HDD(Storage):
    def __init__(self, name, manufacture, total, allocated, capacity, size: float, rpm: int):
        self.size = size
        self.rpm = rpm
        super().__init__(name, manufacture, total, allocated, capacity)


class SSD(Storage):
    def __init__(self, name, manufacture, total, allocated, capacity, interface):
        self.interface = interface
        super().__init__(name, manufacture, total, allocated, capacity)


if __name__ == '__main__':
    resource = Resource('cpu', 'intel', 10, 10)
    print(repr(resource))
