import uuid
from app.db.session import SessionLocal
from app.db.models import Document

def main():
    db = SessionLocal()
    try:
        doc = Document(
            id=uuid.uuid4(),
            s3_bucket="demo-bucket",
            s3_key="demo/file.pdf",
            s3_url="s3://demo-bucket/demo/file.pdf",
            file_type="pdf",
        )
        db.add(doc)
        db.commit()
        print("Inserted document:", doc.id)
    finally:
        db.close()

if __name__ == "__main__":
    main()
