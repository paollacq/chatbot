import chromadb

# Conectar ao ChromaDB
client = chromadb.PersistentClient(path="./chroma.sqlite3")

# Listar coleções disponíveis
collections = client.list_collections()
print("Coleções disponíveis:", [col.name for col in collections])  # Acesse o atributo 'name'

# Verificar se a coleção "courses" existe
if "courses" in [col.name for col in collections]:
    collection = client.get_collection("courses")
    documents = collection.peek()
    print("Documentos armazenados:", documents)
else:
    print("A coleção 'courses' não foi encontrada.")
