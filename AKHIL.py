from fastapi import FastAPI
import uvicorn


app = FastAPI()



@app.get("/")
async def root():
    return{"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("AKHIL:app", host="127.0.0.1", port=5000, log_level="info")

x={};
@app.put("/posts")
def put_post():
    a=input("Enter the task")
    b=input("Enter the task")
    x.update({a:b})


@app.get("/post/search")
def post_search():
    s=input("Enter whatever")
    for i in range(len(x)):
        if (x[i])==s:
            print(x[i])