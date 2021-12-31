import asyncio

async def func2():
    await asyncio.sleep(3)
    print('Msg FUNC2')

async def func3():
    await asyncio.sleep(2)
    print('Msg FUNC3')


async def func1():
    print('executando f2 (task)')
    task = asyncio.create_task(func2())
    print('executando f3 (task2)')
    task2 = asyncio.create_task(func3())
    print('esperando task')
    # a execucao só continua após task ser retornado
    await task
    print('esperando task2')
    await task2


# func1()
asyncio.run(func1())