import os
print("Current working directory:", os.getcwd())

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

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
app.mount("/static", StaticFiles(directory="Insurance_app/static"), name="static")

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

@app.get("/")
def root():
    return {"message": "Welcome to the Insurance Company of Africa API"}



