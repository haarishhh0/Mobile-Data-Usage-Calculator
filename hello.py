browsing = int(input("Enter browsing data used (MB): "))
video = int(input("Enter video streaming data used (MB): "))
online_class = int(input("Enter online class data used (MB): "))

total = browsing + video + online_class

daily_limit = 2000

remaining = daily_limit - total

print("\n Mobile Data Usage")
print("Total Data Used:", total, "MB")
print("Remaining Data:", remaining, "MB")