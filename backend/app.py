from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from protocols.mcp_v2 import route_task
import uvicorn

app = FastAPI(title="SupplyMind Orchestrator")

# Optional: Allow frontend (like Streamlit) to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    contents = await file.read()
    request_data = {
        "file_name": file.filename,
        "raw_text": contents.decode("utf-8")
    }
    result = route_task(request_data)
    return {"status": "success", "result": result}

if __name__ == "__main__":
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
