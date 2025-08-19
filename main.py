import uvicorn

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   uvicorn.run("services.app:app", host="127.0.0.1", port=8000, reload=True)

