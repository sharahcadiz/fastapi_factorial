from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{starting_number}")
def factorial(starting_number: int):
    if starting_number == 0:
        return {"result": False}

    result = starting_number
    
    while starting_number > 1:
        starting_number -= 1
        result *= starting_number

    return {"result": result}
