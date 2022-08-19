from datecalc import duration
from datecalc import when
import datetime as dt
#Arrange
start_date = dt.date(2022,1,1)
end_date = dt.date(2022,1,1)
day_difference = 0
days_between = 10
day1 = dt.date(2022,1,11)
#Act
def test_zero():        
    return duration(start_date,end_date)
#Act
def test_10days():
    return when(start_date,days_between)
#Assert
assert day_difference == test_zero()
assert days_between == duration(start_date,day1)

#Arrange
start_date = dt.date(2022,1,1)
end_date = dt.date(2020,1,1)
day_difference = 731
days_between = 10
day1 = dt.date(2021,12,22)
#Act
def test_past_dates():        
    return duration(start_date,end_date)
#Act
def test_high_days():
    return when(start_date,days_between)
#Assert
assert day_difference == test_zero()
assert days_between == duration(start_date,day1)

