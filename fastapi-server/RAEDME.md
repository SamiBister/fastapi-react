# FASTAPI service

## Project creation

Create project

```bash
poetry new fastapi-server
```

Go to new service directory

```bash
cd fastapi-server/
```

Add dependencies

```bash
poetry add fastapi
poetry add SQLAlchemy
poetry add "uvicorn[standard]"
```

Start poetry shell

```bash
poetry shell
```

Start uvicorn
```bash
uvicorn main:app --reload
```

Test with browser

-[API](http://127.0.0.1:8000/)
-[Swagger UI](http://127.0.0.1:8000/docs)
-[Alternative UI](http://127.0.0.1:8000/redoc)

To exit poetry shell
```bash
exit
```
