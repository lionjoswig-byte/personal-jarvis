from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Personal Jarvis API")


class Query(BaseModel):
    question: str
    agent: str = "orchestrator"


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/query")
def query_endpoint(query: Query):
    return {"answer": f"Response to: {query.question}"}


@app.get("/agents")
def get_agents():
    return {"agents": ["react", "orchestrator", "simple"]}


@app.get("/tools")
def get_tools():
    return {"tools": ["calculator", "file_read", "web_search"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)