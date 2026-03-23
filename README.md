# 🚨 Security Vulnerability Demonstration App

**⚠️ IMPORTANT SECURITY NOTICE:** This application intentionally uses older package versions with known vulnerabilities to demonstrate security scanning capabilities using the Qualys QScanner MCP server.

## 🎯 Purpose

This application serves as a **comprehensive security demonstration** showing how the Qualys QScanner MCP server can detect vulnerabilities in Python applications, especially those using AI/ML frameworks and dependencies with known security issues.

## 🔍 Security Demonstration Features

### Vulnerability Detection
- **106 vulnerabilities** detected across multiple package categories
- **Critical, High, Medium, Low** severity classifications
- **Real CVEs** with actual CVSS scores and QDS ratings
- **AI/ML specific vulnerabilities** in modern ML frameworks

### Package Categories with Vulnerabilities

#### 🤖 AI/ML Frameworks (High Risk)
- **TensorFlow 2.15.0** → Multiple CVEs including heap buffer overflow
- **PyTorch 2.1.0** → torch.load() and distributed training vulnerabilities
- **LangChain 0.1.0** → Critical CVEs in LLM integration
- **Transformers 4.36.0** → Model loading and serialization issues
- **scikit-learn 1.3.2** → Model serialization vulnerabilities
- **OpenCV 4.8.1.78** → Buffer overflow and memory corruption
- **Pillow 10.1.0** → Image parsing vulnerabilities

#### 🌐 Web Frameworks & Core Dependencies
- **Flask 1.1.1**, **FastAPI 0.65.2**, **Django 2.2.8** → Various security issues
- **PyYAML 5.1**, **requests 2.20.0**, **urllib3 1.24.1** → Critical vulnerabilities
- **aiohttp 3.6.2**, **certifi 2019.11.28** → Outdated security components

## 🛡️ QScanner MCP Server Integration

This application is specifically designed to work with the **Qualys QScanner MCP server** to demonstrate:

### Software Composition Analysis (SCA)
- **Dependency vulnerability scanning**
- **CVE detection and classification**
- **Risk scoring with QDS (Qualys Detection Score)**
- **Remediation recommendations**

### Vulnerability Categories Detected
- **Critical**: 18 vulnerabilities (CVSS 7.0-10.0)
- **High**: 56 vulnerabilities (CVSS 4.0-6.9)
- **Medium**: 27 vulnerabilities (CVSS 2.0-3.9)
- **Low**: 5 vulnerabilities (CVSS 0.1-1.9)

## 📊 Scan Results Summary

| Metric | Count | Severity |
|--------|-------|----------|
| **Total Vulnerabilities** | 106 | � **HIGH RISK** |
| **Critical** | 18 | 🔴 **Immediate Action Required** |
| **High** | 56 | 🔴 **High Priority** |
| **Medium** | 27 | 🟡 **Medium Priority** |
| **Low** | 5 | 🟢 **Low Priority** |

## 🔧 Usage for Security Testing

### MCP Server Configuration

#### **Step 1: Configure QScanner MCP Server**

Add this configuration to your Agentic IDE's MCP settings:

**For Claude Desktop (macOS):**
```json
{
  "mcpServers": {
    "qscanner": {
      "command": "qscanner",
      "args": [
        "mcp-server",
        "--gateway-url",
        "${QUALYS_GATEWAY_URL}",
        "--log-level",
        "info"
      ],
      "env": {
        "QUALYS_ACCESS_TOKEN": "${QUALYS_ACCESS_TOKEN}"
      },
      "disabled": false,
      "description": "Qualys QScanner for vulnerability scanning and security analysis"
    }
  }
}
```

**For Claude Code CLI:**
```bash
claude mcp add qscanner qscanner \
  -e QUALYS_ACCESS_TOKEN="${QUALYS_ACCESS_TOKEN}" \
  -- mcp-server \
  --gateway-url "${QUALYS_GATEWAY_URL}" \
  --log-level info
```

**For Windsurf/Cursor (Windows/Linux):**
```json
{
  "mcpServers": {
    "qscanner": {
      "command": "qscanner",
      "args": [
        "mcp-server",
        "--gateway-url",
        "${QUALYS_GATEWAY_URL}",
        "--log-level",
        "info"
      ],
      "env": {
        "QUALYS_ACCESS_TOKEN": "${QUALYS_ACCESS_TOKEN}"
      },
      "disabled": false,
      "description": "Qualys QScanner for vulnerability scanning and security analysis"
    }
  }
}
```

**Configuration Notes:**
- Replace `your-qualys-access-token-here` with your actual Qualys access token
- Update gateway URL to your Qualys instance
- Use environment variables for sensitive data in production
- Set log level to `debug` for troubleshooting, `info` for normal operation

#### **Step 2: Quick Scan Prompts**

**Basic Security Scan:**
```
Scan this repo for vulnerabilities using Qualys QScanner.
```

**Detailed Analysis:**
```
Perform comprehensive SCA scan with CVE details and remediation.
```

**Critical Issues Only:**
```
Show critical and high-severity vulnerabilities with fix versions.
```

**AI/ML Security Focus:**
```
Analyze AI/ML package vulnerabilities and provide risk assessment.
```

#### **Step 3: Analyze Results**

After the scan completes, review:
- **Vulnerability count** and severity distribution
- **Critical CVEs** requiring immediate attention
- **AI/ML specific vulnerabilities** in frameworks like TensorFlow, PyTorch, etc.
- **QDS scores** for risk prioritization
- **Remediation recommendations** provided by QScanner

#### **Step 4: Test Remediation**

1. **Upgrade vulnerable packages** to secure versions
2. **Re-scan** to verify vulnerability elimination
3. **Validate** application functionality post-upgrade
4. **Document** security improvements for compliance

## 🚨 Security Warning

**DO NOT USE THIS APPLICATION IN PRODUCTION**

This application contains:
- **106 known vulnerabilities**
- **Outdated dependencies with security issues**
- **Deliberately insecure configurations**

It is designed **exclusively for security demonstration and training purposes**.

## 📚 Key Vulnerability Examples

### Critical CVEs Detected
- **CVE-2025-69224** (CVSS 6.5) - aiohttp 3.6.2
- **CVE-2024-31580** (CVSS 7.5) - torch 2.1.0
- **CVE-2025-3777** (CVSS 7.5) - transformers 4.36.0
- **CVE-2020-14343** (CVSS 9.8) - PyYAML 5.1

### High-Severity CVEs
- **CVE-2021-21330** (CVSS 6.1) - aiohttp HTTP request handling
- **CVE-2023-23934** (CVSS 5.4) - Werkzeug security components
- **CVE-2026-27448** (CVSS 7.5) - pyopenssl cryptography

## 🎯 Learning Outcomes

After completing this demonstration, users will understand:

- How to use **Qualys QScanner MCP server** for vulnerability detection
- The **importance of dependency management** in AI/ML applications
- **Risk prioritization** using CVSS and QDS scores
- **Remediation strategies** for vulnerable dependencies
- **Supply chain security** best practices

---

**⚠️ Remember**: This is a controlled security demonstration. Always keep your production dependencies updated and regularly scan for vulnerabilities using Qualys QScanner MCP server.
