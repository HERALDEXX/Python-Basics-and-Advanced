import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

streaks = [1, 2, 4, 10, 3, 2, 1]

plt.plot(days, streaks)
plt.title("Habit Streak Progress")
plt.xlabel("Day")
plt.ylabel("Streak")
plt.show()
