from fastapi import FastAPI, HTTPException, status
from doc_reader import document_view_function

app = FastAPI()

@app.get('/count/monkeys/{no_of_monkeys}')
@document_view_function
def count_monkeys(no_of_monkeys:int):

    if no_of_monkeys <= 10:
        return  {"message":  f"Found {no_of_monkeys} monkeys on the tree!"}
    else:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='A tree can only handle up to 10 Monkeys!!')
