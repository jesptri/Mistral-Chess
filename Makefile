.PHONY: run test build
run:
	uvicorn app.main:app --reload
