import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from agent import app

# Vercel serverless function handler
def handler(request):
    return app
