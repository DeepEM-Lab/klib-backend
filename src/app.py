import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "config.asgi:application",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        access_log=True,
        use_colors=True,
        proxy_headers=True,
        lifespan="off",
    )
