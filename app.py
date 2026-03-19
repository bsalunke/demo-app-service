#!/usr/bin/env python3
"""
Multi-Package Python Application with AI/ML
Demonstrates usage of various Python packages including older versions with known vulnerabilities
This is a SECURITY DEMONSTRATION showing how older AI/ML packages can have vulnerabilities
"""

import os
import sys
import json
import datetime
from typing import Dict, List, Any

# Web frameworks
from flask import Flask, jsonify, request, render_template_string
from fastapi import FastAPI
import uvicorn

# Data processing
import numpy as np
import pandas as pd
import scipy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# AI/ML and Deep Learning
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoTokenizer, AutoModel, pipeline
import openai
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import nltk
import spacy
import gensim
from gensim.models import Word2Vec
import xgboost as xgb
import lightgbm as lgb

# Computer Vision
import cv2
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models

# Web scraping and HTTP
import requests
from bs4 import BeautifulSoup
import httpx

# Database and ORM
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Task queue
import celery
import redis

# Image processing
from PIL import Image
import cv2

# Machine Learning
import tensorflow as tf
import keras

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

# Testing and development
import pytest
import jupyter

# Security and authentication
from passlib.context import CryptContext
import jwt
from cryptography.fernet import Fernet

# Configuration
import yaml
from pydantic import BaseModel

# Async support
import asyncio
import aiofiles

# Email and messaging
import smtplib
from email.mime.text import MIMEText

# Date/time utilities
import pytz
from dateutil import parser

# Text processing
import markdown
import bleach
from bs4 import BeautifulSoup

# File handling
import zipfile
import tarfile
import hashlib
import base64

# Monitoring and logging
import logging
from prometheus_client import Counter, Histogram, generate_latest

# Create Flask app
flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = 'your-secret-key-here'

# Create FastAPI app
fastapi_app = FastAPI(title="Multi-Package Demo", version="1.0.0")

# Database setup
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Configuration model
class AppConfig(BaseModel):
    app_name: str
    debug: bool
    database_url: str
    redis_url: str

# Sample data for ML
def generate_sample_data():
    """Generate sample data for machine learning demo"""
    np.random.seed(42)
    X = np.random.randn(1000, 10)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    return X, y

# AI/ML demo functions
def nlp_sentiment_analysis(text):
    """Perform sentiment analysis using transformers"""
    try:
        # Use a pre-trained sentiment analysis pipeline
        classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        result = classifier(text)
        return {"status": "success", "sentiment": result[0]}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def text_generation_demo(prompt):
    """Generate text using transformers"""
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        result = generator(prompt, max_length=50, num_return_sequences=1)
        return {"status": "success", "generated_text": result[0]["generated_text"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def pytorch_neural_network_demo():
    """Demonstrate PyTorch neural network"""
    try:
        # Create a simple neural network
        class SimpleNet(nn.Module):
            def __init__(self):
                super(SimpleNet, self).__init__()
                self.fc1 = nn.Linear(10, 50)
                self.fc2 = nn.Linear(50, 20)
                self.fc3 = nn.Linear(20, 2)
                self.relu = nn.ReLU()
                
            def forward(self, x):
                x = self.relu(self.fc1(x))
                x = self.relu(self.fc2(x))
                x = self.fc3(x)
                return x
        
        model = SimpleNet()
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001)
        
        # Generate sample data
        X = torch.randn(100, 10)
        y = torch.randint(0, 2, (100,))
        
        # Train for one epoch
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        
        return {
            "status": "success",
            "model_parameters": sum(p.numel() for p in model.parameters()),
            "loss": loss.item(),
            "input_shape": X.shape
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def computer_vision_demo():
    """Demonstrate computer vision capabilities"""
    try:
        # Load a pre-trained model
        model = models.resnet18(pretrained=False)
        model.eval()
        
        # Create sample image tensor
        sample_image = torch.randn(1, 3, 224, 224)
        
        with torch.no_grad():
            output = model(sample_image)
        
        return {
            "status": "success",
            "model": "ResNet18",
            "input_shape": sample_image.shape,
            "output_shape": output.shape,
            "predicted_class": torch.argmax(output, dim=1).item()
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def xgboost_demo():
    """Demonstrate XGBoost capabilities"""
    try:
        # Generate sample data
        X, y = generate_sample_data()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Create and train XGBoost model
        model = xgb.XGBClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=6,
            random_state=42
        )
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        accuracy = (y_pred == y_test).mean()
        
        return {
            "status": "success",
            "accuracy": accuracy,
            "feature_importance": model.feature_importances_.tolist(),
            "model_type": "XGBoost Classifier"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def langchain_demo(query):
    """Demonstrate LangChain capabilities"""
    try:
        # Note: This requires OpenAI API key
        # For demo purposes, we'll return a mock response
        return {
            "status": "success",
            "query": query,
            "response": "This is a mock LangChain response. In production, this would use actual LLM APIs.",
            "model": "gpt-3.5-turbo",
            "note": "Requires OpenAI API key for actual functionality"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

def word_embedding_demo():
    """Demonstrate word embeddings with Word2Vec"""
    try:
        # Sample sentences
        sentences = [
            ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],
            ['machine', 'learning', 'is', 'fun', 'and', 'exciting'],
            ['python', 'is', 'a', 'great', 'programming', 'language'],
            ['deep', 'learning', 'uses', 'neural', 'networks'],
            ['natural', 'language', 'processing', 'is', 'fascinating']
        ]
        
        # Train Word2Vec model
        model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        
        # Get similar words
        similar_words = {}
        for word in ['machine', 'learning', 'python']:
            if word in model.wv:
                similar_words[word] = [w for w, _ in model.wv.most_similar(word, topn=3)]
        
        return {
            "status": "success",
            "vocabulary_size": len(model.wv),
            "vector_size": model.vector_size,
            "similar_words": similar_words,
            "model_type": "Word2Vec"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Machine Learning demo
def ml_demo():
    """Demonstrate machine learning capabilities"""
    X, y = generate_sample_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    return {"accuracy": accuracy, "feature_importance": model.feature_importances_.tolist()}

# Web scraping demo
async def web_scraping_demo():
    """Demonstrate web scraping capabilities"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://httpbin.org/json')
            data = response.json()
            return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Image processing demo
def image_processing_demo():
    """Demonstrate image processing capabilities"""
    try:
        # Create a simple image
        img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        img = Image.fromarray(img_array)
        
        # Convert to OpenCV format
        cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        
        # Apply some processing
        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        
        return {
            "original_shape": img_array.shape,
            "processed_shape": edges.shape,
            "status": "success"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Data visualization demo
def visualization_demo():
    """Demonstrate data visualization capabilities"""
    try:
        # Create sample data
        x = np.linspace(0, 10, 100)
        y1 = np.sin(x)
        y2 = np.cos(x)
        
        # Create Plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'))
        fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'))
        
        # Convert to JSON
        fig_json = fig.to_json()
        
        return {"plot_data": json.loads(fig_json), "status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Flask routes
@flask_app.route('/')
def flask_home():
    """Flask home page"""
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Multi-Package Python Application with AI/ML</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            .feature { margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
            .status { color: green; font-weight: bold; }
            .ai-section { background-color: #e8f5e8; border-left: 4px solid #4CAF50; }
            .endpoint { background-color: #f0f8ff; padding: 10px; margin: 5px 0; border-radius: 3px; font-family: monospace; }
            .button { background-color: #007bff; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; margin: 5px; }
            .button:hover { background-color: #0056b3; }
            .demo-form { margin: 10px 0; padding: 10px; background-color: #f9f9f9; border-radius: 5px; }
            .demo-form input, .demo-form textarea { width: 100%; padding: 8px; margin: 5px 0; border: 1px solid #ddd; border-radius: 3px; }
        </style>
        <script>
            async function callAPI(endpoint, method = 'GET', data = null) {
                try {
                    const options = {
                        method: method,
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    };
                    if (data) {
                        options.body = JSON.stringify(data);
                    }
                    
                    const response = await fetch(endpoint, options);
                    const result = await response.json();
                    document.getElementById('result').textContent = JSON.stringify(result, null, 2);
                } catch (error) {
                    document.getElementById('result').textContent = 'Error: ' + error.message;
                }
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>🚨 AI/ML Security Vulnerability Demonstration</h1>
            <p><strong>⚠️ SECURITY WARNING:</strong> This application intentionally uses older AI/ML packages with known vulnerabilities to demonstrate security risks.</p>
            <p>This shows how AI/ML applications can be vulnerable when using outdated dependencies.</p>
            
            <div class="feature" style="background-color: #fff3cd; border-left: 4px solid #ffc107;">
                <h3>🔒 Security Demonstration Purpose:</h3>
                <p>This demo illustrates why keeping AI/ML packages updated is crucial for security:</p>
                <ul>
                    <li>Older ML frameworks may have unpatched vulnerabilities</li>
                    <li>AI/ML packages often have complex dependencies</li>
                    <li>Model files and data processing can be attack vectors</li>
                    <li>Package supply chain security is critical in ML</li>
                </ul>
            </div>
            
            <div class="feature">
                <h3>📦 Available Packages:</h3>
                <ul>
                    <li><strong>Web Frameworks:</strong> Flask {{ flask_version }}, FastAPI</li>
                    <li><strong>Data Processing:</strong> NumPy {{ numpy_version }}, Pandas {{ pandas_version }}, SciPy</li>
                    <li><strong>Machine Learning:</strong> Scikit-learn, XGBoost, LightGBM</li>
                    <li><strong>Deep Learning:</strong> TensorFlow {{ tensorflow_version }}, Keras, PyTorch</li>
                    <li><strong>NLP & Transformers:</strong> Transformers, LangChain, OpenAI, NLTK, spaCy</li>
                    <li><strong>Computer Vision:</strong> OpenCV, PIL, TorchVision</li>
                    <li><strong>Word Embeddings:</strong> Gensim, Word2Vec</li>
                    <li><strong>Web Scraping:</strong> Requests, BeautifulSoup, HTTPX</li>
                    <li><strong>Database:</strong> SQLAlchemy</li>
                    <li><strong>Task Queue:</strong> Celery, Redis</li>
                    <li><strong>Visualization:</strong> Matplotlib, Seaborn, Plotly</li>
                    <li><strong>Development:</strong> Jupyter, Notebook, Streamlit</li>
                </ul>
            </div>
            
            <div class="feature" style="background-color: #f8d7da; border-left: 4px solid #dc3545;">
                <h3>⚠️ Known Vulnerability Examples in AI/ML Packages:</h3>
                <p>Older AI/ML packages may contain vulnerabilities such as:</p>
                <ul>
                    <li><strong>TensorFlow < 2.4.2:</strong> Multiple CVEs including heap buffer overflow, integer overflow</li>
                    <li><strong>PyTorch < 1.8.0:</strong> Vulnerabilities in torch.load() and distributed training</li>
                    <li><strong>scikit-learn < 0.24.2:</strong> Security issues in model serialization</li>
                    <li><strong>OpenCV < 4.5.4:</strong> Buffer overflow and memory corruption issues</li>
                    <li><strong>Pillow < 8.3.0:</strong> Multiple image parsing vulnerabilities</li>
                    <li><strong>FastAPI < 0.65.3:</strong> Request validation and middleware issues</li>
                </ul>
                <p><em>Run a security scan to identify specific vulnerabilities in this environment.</em></p>
            </div>
            
            <div class="feature ai-section">
                <h3>🧠 AI/ML Features (Security Demo):</h3>
                <div class="demo-form">
                    <h4>Sentiment Analysis</h4>
                    <textarea id="sentiment-text" placeholder="Enter text for sentiment analysis...">I love this new AI application!</textarea>
                    <button class="button" onclick="callAPI('/ai/sentiment', 'POST', {text: document.getElementById('sentiment-text').value})">Analyze Sentiment</button>
                </div>
                
                <div class="demo-form">
                    <h4>Text Generation</h4>
                    <input type="text" id="text-prompt" placeholder="Enter prompt for text generation..." value="The future of artificial intelligence is">
                    <button class="button" onclick="callAPI('/ai/text-generation', 'POST', {prompt: document.getElementById('text-prompt').value})">Generate Text</button>
                </div>
                
                <div class="demo-form">
                    <h4>LangChain Query</h4>
                    <input type="text" id="langchain-query" placeholder="Enter your question..." value="What is machine learning?">
                    <button class="button" onclick="callAPI('/ai/langchain', 'POST', {query: document.getElementById('langchain-query').value})">Ask LangChain</button>
                </div>
            </div>
            
            <div class="feature">
                <h3>🔗 API Endpoints:</h3>
                <div class="endpoint">GET /health - Health check</div>
                <div class="endpoint">GET /ml-demo - Machine Learning demo</div>
                <div class="endpoint">GET /scraping-demo - Web scraping demo</div>
                <div class="endpoint">GET /image-demo - Image processing demo</div>
                <div class="endpoint">GET /viz-demo - Data visualization demo</div>
                <div class="endpoint">GET /package-info - Package information</div>
                <div class="endpoint" style="background-color: #f8d7da;">GET /security-scan - 🚨 Security vulnerability report</div>
                
                <h4>AI/ML Endpoints:</h4>
                <div class="endpoint">POST /ai/sentiment - Sentiment analysis</div>
                <div class="endpoint">POST /ai/text-generation - Text generation</div>
                <div class="endpoint">GET /ai/pytorch - PyTorch neural network</div>
                <div class="endpoint">GET /ai/computer-vision - Computer vision demo</div>
                <div class="endpoint">GET /ai/xgboost - XGBoost demo</div>
                <div class="endpoint">POST /ai/langchain - LangChain demo</div>
                <div class="endpoint">GET /ai/word-embeddings - Word embeddings</div>
            </div>
            
            <div class="feature">
                <h3>📊 System Information:</h3>
                <p>Python Version: {{ python_version }}</p>
                <p>Platform: {{ platform }}</p>
                <p>Total Packages: {{ total_packages }}</p>
            </div>
            
            <div class="feature">
                <h3>🔍 API Response:</h3>
                <pre id="result" style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto;">Click any button above to see API responses here...</pre>
            </div>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template,
        flask_version=Flask.__version__,
        numpy_version=np.__version__,
        pandas_version=pd.__version__,
        tensorflow_version=tf.__version__,
        python_version=sys.version,
        platform=sys.platform,
        total_packages=len(sys.modules)
    )

@flask_app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "version": "1.0.0"
    })

@flask_app.route('/ml-demo')
def ml_demo_endpoint():
    """Machine learning demo endpoint"""
    return jsonify(ml_demo())

@flask_app.route('/scraping-demo')
async def scraping_demo_endpoint():
    """Web scraping demo endpoint"""
    result = await web_scraping_demo()
    return jsonify(result)

@flask_app.route('/image-demo')
def image_demo_endpoint():
    """Image processing demo endpoint"""
    return jsonify(image_processing_demo())

@flask_app.route('/viz-demo')
def viz_demo_endpoint():
    """Data visualization demo endpoint"""
    return jsonify(visualization_demo())

@flask_app.route('/package-info')
def package_info():
    """Package information endpoint"""
    packages = {
        "flask": Flask.__version__,
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scipy": scipy.__version__,
        "sklearn": "0.24.2",  # Fixed version from requirements
        "tensorflow": tf.__version__,
        "keras": keras.__version__,
        "requests": requests.__version__,
        "beautifulsoup4": BeautifulSoup.__version__,
        "sqlalchemy": sqlalchemy.__version__,
        "pil": Image.__version__,
        "opencv-python": cv2.__version__,
        "matplotlib": matplotlib.__version__,
        "seaborn": sns.__version__,
        "plotly": plotly.__version__,
        "pytest": pytest.__version__,
        "jupyter": jupyter.__version__,
        "passlib": passlib.__version__,
        "cryptography": "3.4.7",  # Fixed version from requirements
        "jwt": "2.0.1",  # PyJWT version
        "yaml": yaml.__version__,
        "pydantic": pydantic.__version__,
        "httpx": httpx.__version__,
        "aiofiles": aiofiles.__version__,
        "pytz": pytz.__version__,
        "dateutil": "2.8.2",  # Fixed version from requirements
        "markdown": markdown.__version__,
        "bleach": bleach.__version__,
        "redis": redis.__version__,
        "celery": celery.__version__,
        "torch": "1.7.1",  # Older version with potential vulnerabilities
        "transformers": "3.5.1",  # Older version with potential vulnerabilities
        "openai": "0.10.0",  # Older version with potential vulnerabilities
        "langchain": "0.0.83",  # Older version with potential vulnerabilities
        "nltk": "3.6.2",  # Older version with potential vulnerabilities
        "spacy": "3.0.8",  # Older version with potential vulnerabilities
        "gensim": "3.8.3",  # Older version with potential vulnerabilities
        "xgboost": "1.4.2",  # Older version with potential vulnerabilities
        "lightgbm": "3.2.1",  # Older version with potential vulnerabilities
    }
    
    return jsonify({
        "packages": packages,
        "total_packages": len(packages),
        "python_version": sys.version,
        "platform": sys.platform
    })

# AI/ML Demo Endpoints
@flask_app.route('/ai/sentiment', methods=['POST'])
def sentiment_analysis_endpoint():
    """Sentiment analysis endpoint"""
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' field in request"}), 400
    
    result = nlp_sentiment_analysis(data['text'])
    return jsonify(result)

@flask_app.route('/ai/text-generation', methods=['POST'])
def text_generation_endpoint():
    """Text generation endpoint"""
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "Missing 'prompt' field in request"}), 400
    
    result = text_generation_demo(data['prompt'])
    return jsonify(result)

@flask_app.route('/ai/pytorch')
def pytorch_endpoint():
    """PyTorch neural network demo endpoint"""
    return jsonify(pytorch_neural_network_demo())

@flask_app.route('/ai/computer-vision')
def computer_vision_endpoint():
    """Computer vision demo endpoint"""
    return jsonify(computer_vision_demo())

@flask_app.route('/ai/xgboost')
def xgboost_endpoint():
    """XGBoost demo endpoint"""
    return jsonify(xgboost_demo())

@flask_app.route('/ai/langchain', methods=['POST'])
def langchain_endpoint():
    """LangChain demo endpoint"""
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' field in request"}), 400
    
    result = langchain_demo(data['query'])
    return jsonify(result)

@flask_app.route('/ai/word-embeddings')
def word_embeddings_endpoint():
    """Word embeddings demo endpoint"""
    return jsonify(word_embedding_demo())

@flask_app.route('/security-scan')
def security_scan_endpoint():
    """Security scan information endpoint"""
    return jsonify({
        "security_status": "VULNERABLE",
        "message": "This application intentionally uses older packages with known vulnerabilities for security demonstration",
        "vulnerable_packages": [
            {
                "package": "tensorflow",
                "current_version": "2.4.1",
                "secure_version": "2.4.2+",
                "cve_examples": ["CVE-2021-37678", "CVE-2021-37679", "CVE-2021-37680"],
                "severity": "High",
                "description": "Multiple security issues in TensorFlow core"
            },
            {
                "package": "torch",
                "current_version": "1.7.1",
                "secure_version": "1.8.0+",
                "cve_examples": ["CVE-2021-37636", "CVE-2021-37637"],
                "severity": "High",
                "description": "Vulnerabilities in torch.load() and distributed training"
            },
            {
                "package": "opencv-python",
                "current_version": "4.5.3.56",
                "secure_version": "4.5.4+",
                "cve_examples": ["CVE-2021-37645", "CVE-2021-37646"],
                "severity": "High",
                "description": "Buffer overflow and memory corruption issues"
            },
            {
                "package": "pillow",
                "current_version": "8.2.0",
                "secure_version": "8.3.0+",
                "cve_examples": ["CVE-2021-37693", "CVE-2021-37694"],
                "severity": "Medium",
                "description": "Multiple image parsing vulnerabilities"
            },
            {
                "package": "fastapi",
                "current_version": "0.65.2",
                "secure_version": "0.65.3+",
                "cve_examples": ["CVE-2021-37701"],
                "severity": "Medium",
                "description": "Request validation and middleware issues"
            },
            {
                "package": "scikit-learn",
                "current_version": "0.24.2",
                "secure_version": "0.24.2+",
                "cve_examples": ["CVE-2021-37699"],
                "severity": "Low",
                "description": "Security issues in model serialization"
            }
        ],
        "recommendation": "Upgrade all packages to their latest secure versions",
        "scan_type": "Software Composition Analysis (SCA)",
        "total_vulnerabilities": 15,
        "severity_breakdown": {
            "critical": 0,
            "high": 8,
            "medium": 5,
            "low": 2
        }
    })

# FastAPI routes
@fastapi_app.get("/")
async def fastapi_root():
    """FastAPI root endpoint"""
    return {
        "message": "Multi-Package Python Application - FastAPI",
        "framework": "FastAPI",
        "python_version": sys.version,
        "packages": {
            "fastapi": "0.68.1",
            "uvicorn": "0.15.0",
            "pydantic": "1.8.2"
        }
    }

@fastapi_app.get("/health")
async def fastapi_health():
    """FastAPI health check"""
    return {
        "status": "healthy",
        "framework": "FastAPI",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

def main():
    """Main function to run the application"""
    print("Starting Multi-Package Python Application...")
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # Print some package versions
    print(f"Flask version: {Flask.__version__}")
    print(f"NumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print(f"TensorFlow version: {tf.__version__}")
    
    # Run Flask app
    port = int(os.environ.get('PORT', 8000))
    flask_app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()
