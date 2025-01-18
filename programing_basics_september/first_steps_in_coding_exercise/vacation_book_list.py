book_pages = int(input())
book_pages_per_hour = int(input())
days_to_read = int(input())

total_time = book_pages // book_pages_per_hour
needed_time_per_day = total_time // days_to_read

print(needed_time_per_day)
