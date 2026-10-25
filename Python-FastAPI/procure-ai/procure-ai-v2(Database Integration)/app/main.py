from fastapi import FastAPI
from app.api.suppliers import router as supplier_router
from app.api.products import router as product_router
from app.api.purchase_orders import router as purchase_orders_router
app=FastAPI(
    title='ProcureAI API',
    description='Enterprise Procurement Management Platform',
    version='1.0.0'
)
app.include_router(supplier_router)
app.include_router(product_router)
app.include_router(purchase_orders_router)
@app.get('/')
async def root():
    return{
        'message':'Welcome to ProcureAI API'
    }


@app.get('/api/v1/invoices')
async def get_invoices():
    return []