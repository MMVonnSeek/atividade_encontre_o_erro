from app.database import engine, SessionLocal
from app import models
from app.models import Categoria, Fornecedor, Produto


models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas!")

db = SessionLocal()

cat1 = Categoria(nome="Cimento e Argamassa")
cat2 = Categoria(nome="Ferramentas")
cat3 = Categoria(nome="Elétrica")

db.add(cat1)
db.add(cat2)
db.add(cat3)
db.commit()
db.refresh(cat1)
db.refresh(cat2)
db.refresh(cat3)
print(f"Categorias: {cat1.id}, {cat2.id}, {cat3.id}")

forn1 = Fornecedor(nome="ConstruMax Ltda", contato="construmax@email.com")
forn2 = Fornecedor(nome="FerraTech ME", contato="(61) 98888-0002")
forn3 = Fornecedor(nome="EletroObra S/A", contato="contato@eletroobra.com.br")

db.add(forn1)
db.commit()
db.refresh(forn1)
db.refresh(forn2)
db.refresh(forn3)
print(f"Fornecedores: {forn1.id}, {forn2.id}, {forn3.id}")

produtos = [
    Produto(nome="Cimento CP-II 50kg", preco=38.90, quantidade=300,
            categoria_id=cat1.id, fornecedor_id=forn1.id),
    Produto(nome="Argamassa AC-II 20kg", preco=22.50,  quantidade=150,
            categoria_id=cat1.id, fornecedor_id=forn1.id),
    Produto(nome="Furadeira de Impacto", preco=349.90, quantidade=20,
            categoria_id=cat2.id, fornecedor_id=forn2.id),
    Produto(nome="Nível de Bolha 60cm", preco=45.00, quantidade=40,
            categoria_id=cat2.id, fornecedor_id=forn2.id),
    Produto(nome="Disjuntor 20A", preco=18.90, quantidade=80,
            categoria_id=cat3.id, fornecedor_id=forn3.id),
]

for p in produtos:
    db.add(p)

for p in produtos:
    db.refresh(p)

print(f"{len(produtos)} produtos inseridos!")

todos = db.query(Produto).all()
print("\nProdutos no estoque:")
for prod in todos:
    
    print(f"  [{prod.id}] {prod.nome} | R$ {prod.preco:.2f} | Un.: {prod.unidade}")

db.close()
