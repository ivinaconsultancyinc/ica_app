import os

import time

from fastapi import FastAPI, Request, Form, Depends, HTTPException, Cookie

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from fastapi.responses import RedirectResponse, HTMLResponse

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, Session

from passlib.context import CryptContext

# --- Password hashing context ---

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):

    return pwd_context.verify(plain_password, hashed_password)

# --- SQLAlchemy setup ---

from insurance_app.models.models import User, Client, Policy, Product, Premium, Commission, Claim, Customer, Agent, Document, Audit, Ledger, Reinsurance

from insurance_app.routers.routers_client import router as client_router

from insurance_app.routers.routers_policy import router as policy_router

from insurance_app.routers.routers_product import router as product_router

from insurance_app.routers.routers_premium import router as premium_router

from insurance_app.routers.routers_commission import router as commission_router

from insurance_app.routers.routers_claim import router as claim_router

from insurance_app.routers.routers_customer import router as customer_router

from insurance_app.routers.routers_agent import router as agent_router

from insurance_app.routers.routers_document import router as document_router

from insurance_app.routers.routers_audit import router as audit_router

from insurance_app.routers.routers_ledger import router as ledger_router

from insurance_app.routers.routers_reinsurance import router as reinsurance_router

from insurance_app.routers.routers_dashboard import router as dashboard_router

from insurance_app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Insurance Company of Africa Management System")

app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])

SQLALCHEMY_DATABASE_URL = "sqlite:///./insurance.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

try:

    from insurance_app.views import router as views_router

except ImportError:

    views_router = None

from insurance_app.connection import get_db  # Use your connection.py for DB session

static_dir = os.path.join(os.path.dirname(__file__), "insurance_app", "static")

if os.path.isdir(static_dir):

    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    print(f"Mounted static directory: {static_dir}")

else:

    print(f"Warning: Static directory '{static_dir}' does not exist. Static files will not be served.")

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "insurance_app", "templates"))

app.include_router(client_router, prefix="/clients", tags=["Clients"])

app.include_router(policy_router, prefix="/policies", tags=["Policies"])

app.include_router(product_router, prefix="/products", tags=["Products"])

app.include_router(premium_router, prefix="/premiums", tags=["Premiums"])

app.include_router(commission_router, prefix="/commissions", tags=["Commissions"])

app.include_router(claim_router, prefix="/claims", tags=["Claims & Loans"])

app.include_router(customer_router, prefix="/customers", tags=["Customers"])

app.include_router(agent_router, prefix="/agents", tags=["Agents"])

app.include_router(document_router, prefix="/documents", tags=["Documents"])

app.include_router(audit_router, prefix="/audit", tags=["Audit"])

app.include_router(ledger_router, prefix="/ledger", tags=["Ledger"])

app.include_router(reinsurance_router, prefix="/reinsurance", tags=["Reinsurance"])

if views_router:

    app.include_router(views_router)

# --- Role-based access control dependency ---

def require_role(required_roles):

    def role_checker(role: str = Cookie(None)):

        if role not in required_roles:

            raise HTTPException(status_code=403, detail="Access forbidden: insufficient role")

    return Depends(role_checker)

# --- Session timeout dependency ---

SESSION_TIMEOUT = 60 * 30  # 30 minutes

def check_session(session: str = Cookie(None)):

    if session is None:

        raise HTTPException(status_code=401, detail="Session expired. Please log in again.")

    try:

        last_active = int(session)

    except Exception:

        raise HTTPException(status_code=401, detail="Invalid session. Please log in again.")

    now = int(time.time())

    if now - last_active > SESSION_TIMEOUT:

        raise HTTPException(status_code=401, detail="Session timed out. Please log in again.")

    return str(now)

# --- Serve dynamic index.html from templates ---

@app.get("/", response_class=HTMLResponse)

async def read_root(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("index.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/agents", response_class=HTMLResponse)

async def agents_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("agents.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/claims", response_class=HTMLResponse)

async def claims_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("claims.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/audit", response_class=HTMLResponse, dependencies=[require_role(["admin"])])

async def audit_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("audit.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/commission", response_class=HTMLResponse)

async def commission_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("commission.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/clients", response_class=HTMLResponse)

async def clients_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("clients.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/customers", response_class=HTMLResponse)

async def customers_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("customers.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/documents", response_class=HTMLResponse)

async def documents_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("documents.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/ledger", response_class=HTMLResponse)

async def ledger_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("ledger.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/policies", response_class=HTMLResponse)

async def policies_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("policies.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/premiums", response_class=HTMLResponse)

async def premiums_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("premiums.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/products", response_class=HTMLResponse)

async def products_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("products.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

@app.get("/reinsurance", response_class=HTMLResponse)

async def reinsurance_page(request: Request, db: Session = Depends(get_db), role: str = Cookie(None), session: str = Depends(check_session)):

    response = templates.TemplateResponse("reinsurance.html", {"request": request, "role": role})

    response.set_cookie(key="session", value=session, max_age=SESSION_TIMEOUT)

    return response

# --- LOGIN ROUTES WITH REAL USER DATABASE ---

@app.get("/login", response_class=HTMLResponse)

async def login_get(request: Request):

    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login", response_class=HTMLResponse)

async def login_post(

    request: Request,

    username: str = Form(...),

    password: str = Form(...),

    remember_me: str = Form(None),

    db: Session = Depends(get_db)

):

    now = str(int(time.time()))

    user = db.query(User).filter(User.username == username).first()

    if user and verify_password(password, user.password_hash):

        response = RedirectResponse(url="/dashboard", status_code=302)

        response.set_cookie(key="role", value=user.role, max_age=60*60*24*30)

        response.set_cookie(key="session", value=now, max_age=SESSION_TIMEOUT)

        if remember_me:

            response.set_cookie(key="remember_me", value="1", max_age=60*60*24*30)

        return response

    else:

        error = "Invalid username or password."

        return templates.TemplateResponse("login.html", {"request": request, "error": error})

# --- LOGOUT ROUTE ---

@app.get("/logout")

async def logout():

    response = RedirectResponse(url="/login", status_code=302)

    response.delete_cookie("role")

    response.delete_cookie("remember_me")

    response.delete_cookie("session")

    return response

# --- RESET PASSWORD ROUTES ---

@app.get("/reset-password", response_class=HTMLResponse)

async def reset_password_get(request: Request):

    return templates.TemplateResponse("reset-password.html", {"request": request, "message": None, "error": None})

@app.post("/reset-password", response_class=HTMLResponse)

async def reset_password_post(request: Request, email: str = Form(...)):

    # Replace with your password reset logic (send email, etc.)

    if email.endswith("@example.com"):  # Dummy check

        message = "A password reset link has been sent to your email."

        return templates.TemplateResponse("reset-password.html", {"request": request, "message": message, "error": None})

    else:

        error = "Email address not found."

        return templates.TemplateResponse("reset-password.html", {"request": request, "message": None, "error": error})

@app.get("/health")

async def health_check():

    return {"status": "healthy", "message": "Insurance Management System is running"}

# (All your other API endpoints remain unchanged)

 


