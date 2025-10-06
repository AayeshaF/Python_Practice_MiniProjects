age = float(input("What is your age in years? "))
unit = input("What unit do you want to convert your age into? (months,weeks,days,hours,minutes,seconds) or (m,w,d,h,min,s)  ").strip().lower()

if unit == "months" or unit == "m":
    answer = age*12
    print(f"You lived for {answer} months.")

elif unit == "weeks" or unit == "w":
    answer = age *52
    print(f"You lived for {answer} weeks.")

elif unit == "days" or unit == "d":
    answer = age * 365
    print(f"You lived for {answer} days.")

elif unit == "hours" or unit =="h":
    answer = age * 365 *24
    print(f"You lived for {answer} hours.")

elif unit == "minutes" or unit == "min":
    answer = age *  365 *24*60
    print(f"You lived for {answer} minutes.")

elif unit == "seconds" or unit == "s":
    answer = age  *  365 *24*60*60
    print(f"You lived for {answer} seconds.")

else:
    print("invalid choice")
