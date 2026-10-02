from fastapi import FastAPI

from app.modules.auth.api.routes import router as auth_router


app = FastAPI(
    title="RentProof API",
    description="Backend API for the RentProof rental property management platform",
    version="1.0.0",
)


app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "RentProof API"
    }