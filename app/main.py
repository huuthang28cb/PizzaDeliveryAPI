from fastapi import FastAPI
from app.auth_routes import auth_router
from app.order_routes import order_router
# from fastapi_jwt_auth import AuthJWT
# from schemas import Settings
# import inspect, re
# from fastapi.routing import APIRoute
# from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(order_router)