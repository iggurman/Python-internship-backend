def emp(**yo):
    count = 0

    for key, value in yo.items():
        count += 1

    return count

print(emp(Name="Gurman", Age=22, City="Bhopal"))