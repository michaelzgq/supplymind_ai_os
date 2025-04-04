# SupplyMind AI Operating System

**SupplyMind** is an AI-native operating system designed specifically for the logistics and supply chain industry. Its core goal is to create an AI-first, multi-agent protocol platform that breaks information gaps, predicts uncertainty, and coordinates complex operations — enabling a system where **AI leads and humans assist**.

## 🚀 Features
- Multi-agent collaboration (each module is a specialized Agent)
- Unified task coordination using the MCP v2 protocol
- Integration with open-source LLMs (starting with Mistral)
- Automated processing of uploaded files (Excel, emails, plain text)
- Outputs include quote suggestions, time estimates, delay risks, clearance recommendations
- Fully open-source with community-driven development

## 📁 Project Structure
/agents - Custom intelligent modules: inquiry, quoting, risk analysis, etc.
/protocols - Protocol logic for MCP v2 (model coordination & routing)
/backend - FastAPI orchestrator (task controller)
/frontend - Streamlit UI for user interaction
/data - Example input files (invoices, inquiries, emails)
/examples - Workflow demos (input → orchestration → output)
/deploy - Docker and CI/CD deployment configs

