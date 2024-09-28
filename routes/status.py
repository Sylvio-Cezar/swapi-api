from . import router;

@router.get("/")
def status():
    return{"status": "ok"}