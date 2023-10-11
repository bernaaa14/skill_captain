import asyncio


async def countdown(n):
    # While loop for counting down from arg n to 1
    while n > 0:
        print(n)
        n -= 1
        # requirement to run a coroutine, pause the execution of the function for 1 second
        await asyncio.sleep(1)


# asynchronous function main  that Creates wrapper that returns a coroutine object
async def main():
    # Ask user for a valid n that will be the start of countdown
    while True:
        try:
            countdown_from = int(input("Countdown from? "))
            # Once input is validated we can now call the countdown function, await the coroutine
            await countdown(countdown_from)
        except ValueError:
            print("Not a valid input")


# asyncio that runs the coroutine
asyncio.run(main())
