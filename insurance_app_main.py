import os
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

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
from insurance_app.models.models import Client, Policy, Product, Premium, Commission, Claim, Customer, Agent, Document, Audit, Ledger, Reinsurance

app = FastAPI(title="Insurance Company of Africa Management System")

@app.post("/api/clients/")
def create_client(name: str, email: str, phone: str = None, db: Session = Depends(get_db)):
    client = Client(name=name, email=email, phone=phone)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@app.get("/api/clients/")
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

@app.get("/api/clients/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.put("/api/clients/{client_id}")
def update_client(client_id: int, name: str = None, email: str = None, phone: str = None, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    if name: client.name = name
    if email: client.email = email
    if phone: client.phone = phone
    db.commit()
    db.refresh(client)
    return client

@app.delete("/api/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    return {"detail": "Client deleted"}

@app.post("/api/policies/")
def create_policy(policy_number: str, client_id: int, product_id: int, db: Session = Depends(get_db)):
    policy = Policy(policy_number=policy_number, client_id=client_id, product_id=product_id)
    db.add(policy)
    db.commit()
    db.refresh(policy)
    return policy

@app.get("/api/policies/")
def get_policies(db: Session = Depends(get_db)):
    return db.query(Policy).all()

@app.get("/api/policies/{policy_id}")
def get_policy(policy_id: int, db: Session = Depends(get_db)):
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy

@app.put("/api/policies/{policy_id}")
def update_policy(policy_id: int, status: str = None, db: Session = Depends(get_db)):
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    if status: policy.status = status
    db.commit()
    db.refresh(policy)
    return policy

@app.delete("/api/policies/{policy_id}")
def delete_policy(policy_id: int, db: Session = Depends(get_db)):
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    db.delete(policy)
    db.commit()
    return {"detail": "Policy deleted"}

@app.post("/api/products/")
def create_product(name: str, description: str = None, db: Session = Depends(get_db)):
    product = Product(name=name, description=description)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@app.get("/api/products/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.get("/api/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/api/products/{product_id}")
def update_product(product_id: int, name: str = None, description: str = None, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if name: product.name = name
    if description: product.description = description
    db.commit()
    db.refresh(product)
    return product

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}

@app.post("/api/premiums/")
def create_premium(policy_id: int, amount: float, due_date: str = None, paid_date: str = None, db: Session = Depends(get_db)):
    premium = Premium(policy_id=policy_id, amount=amount, due_date=due_date, paid_date=paid_date)
    db.add(premium)
    db.commit()
    db.refresh(premium)
    return premium

@app.get("/api/premiums/")
def get_premiums(db: Session = Depends(get_db)):
    return db.query(Premium).all()

@app.get("/api/premiums/{premium_id}")
def get_premium(premium_id: int, db: Session = Depends(get_db)):
    premium = db.query(Premium).filter(Premium.id == premium_id).first()
    if not premium:
        raise HTTPException(status_code=404, detail="Premium not found")
    return premium

@app.put("/api/premiums/{premium_id}")
def update_premium(premium_id: int, amount: float = None, due_date: str = None, paid_date: str = None, db: Session = Depends(get_db)):
    premium = db.query(Premium).filter(Premium.id == premium_id).first()
    if not premium:
        raise HTTPException(status_code=404, detail="Premium not found")
    if amount: premium.amount = amount
    if due_date: premium.due_date = due_date
    if paid_date: premium.paid_date = paid_date
    db.commit()
    db.refresh(premium)
    return premium

@app.delete("/api/premiums/{premium_id}")
def delete_premium(premium_id: int, db: Session = Depends(get_db)):
    premium = db.query(Premium).filter(Premium.id == premium_id).first()
    if not premium:
        raise HTTPException(status_code=404, detail="Premium not found")
    db.delete(premium)
    db.commit()
    return {"detail": "Premium deleted"}

@app.post("/api/commissions/")
def create_commission(agent_id: int, amount: float, date: str = None, db: Session = Depends(get_db)):
    commission = Commission(agent_id=agent_id, amount=amount, date=date)
    db.add(commission)
    db.commit()
    db.refresh(commission)
    return commission

@app.get("/api/commissions/")
def get_commissions(db: Session = Depends(get_db)):
    return db.query(Commission).all()

@app.get("/api/commissions/{commission_id}")
def get_commission(commission_id: int, db: Session = Depends(get_db)):
    commission = db.query(Commission).filter(Commission.id == commission_id).first()
    if not commission:
        raise HTTPException(status_code=404, detail="Commission not found")
    return commission

@app.put("/api/commissions/{commission_id}")
def update_commission(commission_id: int, amount: float = None, date: str = None, db: Session = Depends(get_db)):
    commission = db.query(Commission).filter(Commission.id == commission_id).first()
    if not commission:
        raise HTTPException(status_code=404, detail="Commission not found")
    if amount: commission.amount = amount
    if date: commission.date = date
    db.commit()
    db.refresh(commission)
    return commission

@app.delete("/api/commissions/{commission_id}")
def delete_commission(commission_id: int, db: Session = Depends(get_db)):
    commission = db.query(Commission).filter(Commission.id == commission_id).first()
    if not commission:
        raise HTTPException(status_code=404, detail="Commission not found")
    db.delete(commission)
    db.commit()
    return {"detail": "Commission deleted"}

@app.post("/api/claims/")
def create_claim(policy_id: int, claim_number: str, amount: float = None, status: str = None, filed_date: str = None, settled_date: str = None, db: Session = Depends(get_db)):
    claim = Claim(policy_id=policy_id, claim_number=claim_number, amount=amount, status=status, filed_date=filed_date, settled_date=settled_date)
    db.add(claim)
    db.commit()
    db.refresh(claim)
    return claim

@app.get("/api/claims/")
def get_claims(db: Session = Depends(get_db)):
    return db.query(Claim).all()

@app.get("/api/claims/{claim_id}")
def get_claim(claim_id: int, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim

@app.put("/api/claims/{claim_id}")
def update_claim(claim_id: int, amount: float = None, status: str = None, filed_date: str = None, settled_date: str = None, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    if amount: claim.amount = amount
    if status: claim.status = status
    if filed_date: claim.filed_date = filed_date
    if settled_date: claim.settled_date = settled_date
    db.commit()
    db.refresh(claim)
    return claim

@app.delete("/api/claims/{claim_id}")
def delete_claim(claim_id: int, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    db.delete(claim)
    db.commit()
    return {"detail": "Claim deleted"}

@app.post("/api/customers/")
def create_customer(name: str, email: str = None, phone: str = None, db: Session = Depends(get_db)):
    customer = Customer(name=name, email=email, phone=phone)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

@app.get("/api/customers/")
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.put("/api/customers/{customer_id}")
def update_customer(customer_id: int, name: str = None, email: str = None, phone: str = None, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    if name: customer.name = name
    if email: customer.email = email
    if phone: customer.phone = phone
    db.commit()
    db.refresh(customer)
    return customer

@app.delete("/api/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"detail": "Customer deleted"}

@app.post("/api/agents/")
def create_agent(name: str, email: str = None, phone: str = None, db: Session = Depends(get_db)):
    agent = Agent(name=name, email=email, phone=phone)
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

@app.get("/api/agents/")
def get_agents(db: Session = Depends(get_db)):
    return db.query(Agent).all()

@app.get("/api/agents/{agent_id}")
def get_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@app.put("/api/agents/{agent_id}")
def update_agent(agent_id: int, name: str = None, email: str = None, phone: str = None, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    if name: agent.name = name
    if email: agent.email = email
    if phone: agent.phone = phone
    db.commit()
    db.refresh(agent)
    return agent

@app.delete("/api/agents/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    db.delete(agent)
    db.commit()
    return {"detail": "Agent deleted"}

@app.post("/api/documents/")
def create_document(title: str, file_path: str = None, uploaded_date: str = None, db: Session = Depends(get_db)):
    document = Document(title=title, file_path=file_path, uploaded_date=uploaded_date)
    db.add(document)
    db.commit()
    db.refresh(document)
    return document

@app.get("/api/documents/")
def get_documents(db: Session = Depends(get_db)):
    return db.query(Document).all()

@app.get("/api/documents/{document_id}")
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@app.put("/api/documents/{document_id}")
def update_document(document_id: int, title: str = None, file_path: str = None, uploaded_date: str = None, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    if title: document.title = title
    if file_path: document.file_path = file_path
    if uploaded_date: document.uploaded_date = uploaded_date
    db.commit()
    db.refresh(document)
    return document

@app.delete("/api/documents/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(document)
    db.commit()
    return {"detail": "Document deleted"}

@app.post("/api/audit/")
def create_audit(action: str, user: str = None, timestamp: str = None, details: str = None, db: Session = Depends(get_db)):
    audit = Audit(action=action, user=user, timestamp=timestamp, details=details)
    db.add(audit)
    db.commit()
    db.refresh(audit)
    return audit

@app.get("/api/audit/")
def get_audits(db: Session = Depends(get_db)):
    return db.query(Audit).all()

@app.get("/api/audit/{audit_id}")
def get_audit(audit_id: int, db: Session = Depends(get_db)):
    audit = db.query(Audit).filter(Audit.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit not found")
    return audit

@app.put("/api/audit/{audit_id}")
def update_audit(audit_id: int, action: str = None, user: str = None, timestamp: str = None, details: str = None, db: Session = Depends(get_db)):
    audit = db.query(Audit).filter(Audit.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit not found")
    if action: audit.action = action
    if user: audit.user = user
    if timestamp: audit.timestamp = timestamp
    if details: audit.details = details
    db.commit()
    db.refresh(audit)
    return audit

@app.delete("/api/audit/{audit_id}")
def delete_audit(audit_id: int, db: Session = Depends(get_db)):
    audit = db.query(Audit).filter(Audit.id == audit_id).first()
    if not audit:
        raise HTTPException(status_code=404, detail="Audit not found")
    db.delete(audit)
    db.commit()
    return {"detail": "Audit deleted"}

@app.post("/api/ledger/")
def create_ledger(entry_date: str, description: str = None, amount: float = None, entry_type: str = None, db: Session = Depends(get_db)):
    ledger = Ledger(entry_date=entry_date, description=description, amount=amount, entry_type=entry_type)
    db.add(ledger)
    db.commit()
    db.refresh(ledger)
    return ledger

@app.get("/api/ledger/")
def get_ledgers(db: Session = Depends(get_db)):
    return db.query(Ledger).all

# --- REINSURANCE CRUD API ---

@app.post("/api/reinsurance/")
def create_reinsurance(
    policy_id: int,
    reinsurer: str,
    coverage_amount: float,
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(get_db)
):
    reinsurance = Reinsurance(
        policy_id=policy_id,
        reinsurer=reinsurer,
        coverage_amount=coverage_amount,
        start_date=start_date,
        end_date=end_date
    )
    db.add(reinsurance)
    db.commit()
    db.refresh(reinsurance)
    return reinsurance

@app.get("/api/reinsurance/")
def get_reinsurances(db: Session = Depends(get_db)):
    return db.query(Reinsurance).all()

@app.get("/api/reinsurance/{reinsurance_id}")
def get_reinsurance(reinsurance_id: int, db: Session = Depends(get_db)):
    reinsurance = db.query(Reinsurance).filter(Reinsurance.id == reinsurance_id).first()
    if not reinsurance:
        raise HTTPException(status_code=404, detail="Reinsurance not found")
    return reinsurance

@app.put("/api/reinsurance/{reinsurance_id}")
def update_reinsurance(
    reinsurance_id: int,
    policy_id: int = None,
    reinsurer: str = None,
    coverage_amount: float = None,
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(get_db)
):
    reinsurance = db.query(Reinsurance).filter(Reinsurance.id == reinsurance_id).first()
    if not reinsurance:
        raise HTTPException(status_code=404, detail="Reinsurance not found")
    if policy_id is not None:
        reinsurance.policy_id = policy_id
    if reinsurer is not None:
        reinsurance.reinsurer = reinsurer
    if coverage_amount is not None:
        reinsurance.coverage_amount = coverage_amount
    if start_date is not None:
        reinsurance.start_date = start_date
    if end_date is not None:
        reinsurance.end_date = end_date
    db.commit()
    db.refresh(reinsurance)
    return reinsurance

@app.delete("/api/reinsurance/{reinsurance_id}")
def delete_reinsurance(reinsurance_id: int, db: Session = Depends(get_db)):
    reinsurance = db.query(Reinsurance).filter(Reinsurance.id == reinsurance_id).first()
    if not reinsurance:
        raise HTTPException(status_code=404, detail="Reinsurance not found")
    db.delete(reinsurance)
    db.commit()
    return {"detail": "Reinsurance deleted"}

# If you have a views.py with a router, import it as well
try:
    from insurance_app.views import router as views_router
except ImportError:
    views_router = None

# --- Database integration ---
from insurance_app.connection import get_db  # Use your connection.py for DB session
# Import your ORM models as needed, e.g. from models import Client

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
async def read_root(request: Request, db: Session = Depends(get_db)):
    # Example: Pass ORM data to index.html if needed
    # e.g., clients = db.query(Client).limit(5).all()
    # return templates.TemplateResponse("index.html", {"request": request, "clients": clients})
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/agents", response_class=HTMLResponse)
async def agents_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query agents from DB if needed
    # agents = db.query(Agent).all()
    return templates.TemplateResponse("agents.html", {"request": request})

@app.get("/claims", response_class=HTMLResponse)
async def claims_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query claims from DB if needed
    # claims = db.query(Claim).all()
    return templates.TemplateResponse("claims.html", {"request": request})

@app.get("/audit", response_class=HTMLResponse)
async def audit_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query audit records from DB if needed
    # audits = db.query(Audit).all()
    return templates.TemplateResponse("audit.html", {"request": request})

@app.get("/commission", response_class=HTMLResponse)
async def commission_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query commissions from DB if needed
    # commissions = db.query(Commission).all()
    return templates.TemplateResponse("commission.html", {"request": request})

@app.get("/clients", response_class=HTMLResponse)
async def clients_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query clients from DB if needed
    # clients = db.query(Client).all()
    return templates.TemplateResponse("clients.html", {"request": request})

@app.get("/customers", response_class=HTMLResponse)
async def customers_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query customers from DB if needed
    # customers = db.query(Customer).all()
    return templates.TemplateResponse("customers.html", {"request": request})

@app.get("/documents", response_class=HTMLResponse)
async def documents_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query documents from DB if needed
    # documents = db.query(Document).all()
    return templates.TemplateResponse("documents.html", {"request": request})

@app.get("/ledger", response_class=HTMLResponse)
async def ledger_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query ledger entries from DB if needed
    # ledgers = db.query(Ledger).all()
    return templates.TemplateResponse("ledger.html", {"request": request})

@app.get("/policies", response_class=HTMLResponse)
async def policies_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query policies from DB if needed
    # policies = db.query(Policy).all()
    return templates.TemplateResponse("policies.html", {"request": request})

@app.get("/premiums", response_class=HTMLResponse)
async def premiums_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query premiums from DB if needed
    # premiums = db.query(Premium).all()
    return templates.TemplateResponse("premiums.html", {"request": request})

@app.get("/products", response_class=HTMLResponse)
async def products_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query products from DB if needed
    # products = db.query(Product).all()
    return templates.TemplateResponse("products.html", {"request": request})

@app.get("/reinsurance", response_class=HTMLResponse)
async def reinsurance_page(request: Request, db: Session = Depends(get_db)):
    # Example: Query reinsurance records from DB if needed
    # reinsurances = db.query(Reinsurance).all()
    return templates.TemplateResponse("reinsurance.html", {"request": request})







