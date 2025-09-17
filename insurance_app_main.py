import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# Absolute imports based on your structure
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

# If you have a views.py with a router, import it as well
try:
    from insurance_app.views import router as views_router
except ImportError:
    views_router = None

app = FastAPI(title="Insurance Company of Africa Management System")

# --- Enhancement: Robust static directory resolution for deployment ---
static_dir = os.path.join(os.path.dirname(__file__), "insurance_app", "static")
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
    print(f"Mounted static directory: {static_dir}")
else:
    print(f"Warning: Static directory '{static_dir}' does not exist. Static files will not be served.")
# --- End enhancement ---

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "insurance_app", "templates"))

# Include routers for each module
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

# Include views router if available
if views_router:
    app.include_router(views_router)

# --- Update: Serve dynamic index.html from templates ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Pass any variables you want to use in index.html
    return templates.TemplateResponse("index.html", {"request": request})

# Example: Serve other HTML pages dynamically
@app.get("/agents", response_class=HTMLResponse)
async def agents_page(request: Request):
    return templates.TemplateResponse("agents.html", {"request": request})

@app.get("/claims", response_class=HTMLResponse)
async def claims_page(request: Request):
    return templates.TemplateResponse("claims.html", {"request": request})

# Add similar routes for other HTML files in your templates directory

@app.get("/audit", response_class=HTMLResponse)
async def audit_page(request: Request):
    return templates.TemplateResponse("audit.html", {"request": request})

@app.get("/commission", response_class=HTMLResponse)
async def commission_page(request: Request):
    return templates.TemplateResponse("commission.html", {"request": request})

@app.get("/clients", response_class=HTMLResponse)
async def clients_page(request: Request):
    return templates.TemplateResponse("clients.html", {"request": request})

@app.get("/customers", response_class=HTMLResponse)
async def customers_page(request: Request):
    return templates.TemplateResponse("customers.html", {"request": request})

@app.get("/documents", response_class=HTMLResponse)
async def documents_page(request: Request):
    return templates.TemplateResponse("documents.html", {"request": request})

@app.get("/ledger", response_class=HTMLResponse)
async def ledger_page(request: Request):
    return templates.TemplateResponse("ledger.html", {"request": request})

@app.get("/policies", response_class=HTMLResponse)
async def policies_page(request: Request):
    return templates.TemplateResponse("policies.html", {"request": request})

@app.get("/premiums", response_class=HTMLResponse)
async def premiums_page(request: Request):
    return templates.TemplateResponse("premiums.html", {"request": request})

@app.get("/products", response_class=HTMLResponse)
async def products_page(request: Request):
    return templates.TemplateResponse("products.html", {"request": request})

@app.get("/reinsurance", response_class=HTMLResponse)
async def reinsurance_page(request: Request):
    return templates.TemplateResponse("reinsurance.html", {"request": request})










