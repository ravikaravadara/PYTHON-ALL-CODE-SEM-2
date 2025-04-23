def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

print(sum_avg([78, 85, 90, 95, 88]))
