import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def get_seconds():
    while True:
        try:
            user = int(input("Enter the time in seconds: "))
            if user <= 0:
                raise ValueError("error! should be more than zero.")
            return user
        except ValueError as e:
            print(e)

def main():
    user = get_seconds()
    countdown(user)

if __name__ == '__main__':
    main()