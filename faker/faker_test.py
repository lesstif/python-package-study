from faker import Faker

f = Faker()

print(f'{f.name(),f.time()}')
print(f.date(pattern='%Y-%m-%d', end_datetime='-2years'))

print(f'text={f.text()}')