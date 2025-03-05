import logging

try:
    a = input("try: ")
    r = 10 / int(a)
    print("result:", r)
except ValueError as e:
    logging.exception(e)
    print('ValueError:', e)
except ZeroDivisionError as e:
    logging.exception(e)
    print('except:', e)
else:
    print('no error!')
finally:
    print('finally...')

print('END')


