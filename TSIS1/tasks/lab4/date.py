from datetime import datetime, timedelta

current = datetime.now()

print(f"current: {current}")

fvd = current - timedelta(days=5)

print(f"five day: {fvd}")

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday, today, tomorrow)

print(today.replace(microsecond=0))

print(abs(today - yesterday).total_seconds())