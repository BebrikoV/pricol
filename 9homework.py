import logging
import random
logging.basicConfig(level=logging.ERROR,filename="errorHw9.log",filemode="w",format="%(asctine)s: %(levelname)s - %(massage)s")
rangeProgres = range(0,10)
itRangeProgres = iter(rangeProgres)
progres = [(3+8*next(itRangeProgres)) for i in range(10)]
itProgges = iter(progres)
while itProgges:
    try:
        randomNum = random.randint(-5,5)
        print(next(itProgges), "/", randomNum, "=", next(itProgges) / randomNum)

    except ZeroDivisionError:
        logging.error("an error occurred while dividing the progression element by 8")
        logging.error(ZeroDivisionError)
    except StopIteration:
        logging.error("end progrea")