
'''
this module handles time zone requirements

'''
from datetime import timedelta
import numbers
class TimeZone:
    def __init__(self , name:str ,
                 offset_hours :int ,
                 offset_minutes :int):
        name = name.strip()
        if not name:
            raise ValueError('name of time zone cannot be empty.')

        self._name = name

        # check offset minutes to be integer

        if not isinstance(offset_minutes , numbers.Integral):
            raise ValueError('offset minutes must be integer.')
        # check the range of minutes

        if abs(offset_minutes)>59:
            raise ValueError('offset minutes can not be > 59')

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('offset hours must be integer.')


        offset  = timedelta( hours= offset_hours ,
                            minutes = offset_minutes
                            )

        # check the range of time delta
        if (offset > timedelta(hours = 18 , minutes=0)
                or offset < timedelta(hours=-18  , minutes=0)):
            raise ValueError('range is invalid')


        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes



    @property
    def offset_hours(self):
        return self._offset_hours

    @property
    def offset_minutes(self):
        return self._offset_minutes

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        if not isinstance(other,TimeZone):
            raise NotImplemented

        return ( other.name ,
                 other.offset_hours
                 , self.offset_minutes)== (self.name ,
                                           self.offset_hours ,
                                           self._offset_minutes)


    def __repr__(self):
        return (f'TimeZone(name ={self.name} , offset_hours = {self.offset_hours})'
                f'offset_minutes = {self.offset_minutes}')


