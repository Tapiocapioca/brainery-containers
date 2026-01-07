FROM quay.io/unstructured-io/unstructured-api:latest

# Expose port 8000 (default for unstructured-api)
EXPOSE 8000

# Health check endpoint
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Default command
CMD ["uvicorn", "prepline_general.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
