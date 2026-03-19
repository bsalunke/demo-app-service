# 🚨 Security Vulnerability Demonstration App

**⚠️ IMPORTANT SECURITY NOTICE:** This application intentionally uses older package versions with known vulnerabilities to demonstrate security scanning capabilities using the Qualys QScanner MCP server.

## 🎯 Purpose

This application serves as a **comprehensive security demonstration** showing how the Qualys QScanner MCP server can detect vulnerabilities in Python applications, especially those using AI/ML frameworks and dependencies with known security issues.

## 🔍 Security Demonstration Features

### Vulnerability Detection
- **524+ vulnerabilities** detected across multiple package categories
- **Critical, High, Medium, Low** severity classifications
- **Real CVEs** with actual CVSS scores and QDS ratings
- **AI/ML specific vulnerabilities** in modern ML frameworks

### Package Categories with Vulnerabilities

#### 🤖 AI/ML Frameworks (High Risk)
- **TensorFlow 2.4.1** → Multiple CVEs including heap buffer overflow
- **PyTorch 1.7.1** → torch.load() and distributed training vulnerabilities
- **LangChain 0.0.83** → 15+ critical/high CVEs in LLM integration
- **Transformers 3.5.1** → Model loading and serialization issues
- **scikit-learn 0.24.2** → Model serialization vulnerabilities
- **OpenCV 4.5.3.56** → Buffer overflow and memory corruption
- **Pillow 8.2.0** → Image parsing vulnerabilities

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
- **Critical**: 18 vulnerabilities (CVSS 9.0-10.0)
- **High**: 164 vulnerabilities (CVSS 7.0-8.9)
- **Medium**: 211 vulnerabilities (CVSS 4.0-6.9)
- **Low**: 131 vulnerabilities (CVSS 0.1-3.9)

## 📊 Scan Results Summary

| Metric | Count | Severity |
|--------|-------|----------|
| **Total Vulnerabilities** | 524 | 🚨 **EXTREME RISK** |
| **Critical** | 18 | 🔴 **Immediate Action Required** |
| **High** | 164 | 🔴 **High Priority** |
| **Medium** | 211 | 🟡 **Medium Priority** |
| **Low** | 131 | 🟢 **Low Priority** |

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

#### **Step 2: Sample Agent Prompts for Security Scanning**

**Prompt for Agent IDE (Chat Interface):**
```
Please perform a comprehensive SCA vulnerability scan of this repository using the Qualys QScanner MCP server. 

Scan the current directory and provide:
1. Total vulnerability count and severity breakdown
2. Critical and high-priority vulnerabilities with CVE details
3. AI/ML specific security issues
4. Remediation recommendations for the most critical issues

```

**Prompt for Agent CLI:**
```bash
# Interactive scan request
"Scan this Python application for security vulnerabilities using Qualys QScanner. Focus on AI/ML package vulnerabilities and provide a detailed risk assessment with CVE details and remediation guidance."

# Specific scan with parameters
"Perform SCA scan on /path/to/demo-app-service directory. Use get-report mode and provide vulnerability summary with QDS scores greater than 70."
```

**Advanced Analysis Prompt:**
```
Using the Qualys QScanner MCP server, analyze this codebase for:

1. Software composition analysis (SCA) vulnerabilities
2. Dependency security risks in AI/ML frameworks
3. Critical CVEs with CVSS scores 8.0+
4. Supply chain security issues
5. Remediation prioritization based on QDS scores

Generate a comprehensive security report with actionable recommendations for the development team.
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
- **524 known vulnerabilities**
- **Outdated dependencies with security issues**
- **Deliberately insecure configurations**

It is designed **exclusively for security demonstration and training purposes**.

## 📚 Key Vulnerability Examples

### Critical CVEs Detected
- **CVE-2025-14009** (CVSS 10.0) - NLTK 3.6.2
- **CVE-2022-45907** (CVSS 9.8) - PyTorch 1.7.1
- **CVE-2023-39659** (CVSS 9.8) - LangChain 0.0.83
- **CVE-2020-14343** (CVSS 9.8) - PyYAML 5.1

### High-Severity CVEs
- **CVE-2023-46229** (CVSS 8.8) - LangChain LLM integration
- **CVE-2023-4863** (CVSS 8.8) - Pillow image parsing
- **CVE-2024-11393** (CVSS 8.8) - Transformers model loading

## 🎯 Learning Outcomes

After completing this demonstration, users will understand:

- How to use **Qualys QScanner MCP server** for vulnerability detection
- The **importance of dependency management** in AI/ML applications
- **Risk prioritization** using CVSS and QDS scores
- **Remediation strategies** for vulnerable dependencies
- **Supply chain security** best practices

---

**⚠️ Remember**: This is a controlled security demonstration. Always keep your production dependencies updated and regularly scan for vulnerabilities using Qualys QScanner MCP server.
