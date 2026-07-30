# MCP-Powered AI Assistant

A comprehensive, production-ready portfolio project featuring a FastAPI backend, a LangGraph-based agentic workflow, custom FastMCP servers/clients, JWT authentication, and structured conversation memory.

---



## 🏗️ Architecture Overview

The system is designed with a decoupled architecture that separates the API server, authentication layer, orchestrator (LangGraph), and tool execution ecosystem (MCP).

```
               User
                  │
                  ▼
          FastAPI REST/WebSocket
                  │
                  ▼
          Authentication Layer
                  │
                  ▼
          LangGraph Agent
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
   Memory      MCP Client    Planner
     │            │            │
     ▼            ▼            ▼
SQLite DB    FastMCP Server   Executor
                  │
      ┌───────────┼────────────┐
      ▼           ▼            ▼
  Weather      GitHub      Calculator
      ▼           ▼            ▼
 PDF Reader   Calendar     Email Tool
      ▼           ▼            ▼
 Image Gen   Web Search   File System
```

---

## 🗺️ Recommended Development Order & Roadmap

The project is structured into distinct phases to ensure clean integration, iterative testing, and stable development.

| Phase | Milestone | Description |
| :--- | :--- | :--- |
| **Phase 1** | **FastAPI Backend** | Initialize the web application, routing, error handling, and basic health checks. |
| **Phase 2** | **Authentication (JWT)** | Implement user login/signup, password hashing, and secure routes via JSON Web Tokens. |
| **Phase 3** | **LangGraph Agent** | Set up the state graph, agent nodes, state definitions, and LLM orchestration flow. |
| **Phase 4** | **FastMCP Server & Client** | Establish the Model Context Protocol (MCP) server framework and client connector for extensible tools. |
| **Phase 5** | **Basic Tools (Calculator & File)** | Implement local utilities: calculator for arithmetic operations and File System tools. |
| **Phase 6** | **Integrations (Weather & Web Search)**| Implement external APIs for fetching weather and performing web queries. |
| **Phase 7** | **Document Processing (PDF Reader)** | Set up PDF parsing, tokenization, and metadata extraction. |
| **Phase 8** | **SQLite Conversation Memory** | Connect SQLite database to persist session messages and agent states across requests. |
| **Phase 9** | **Productivity Tools (GitHub, Email, Cal)**| Integrate GitHub APIs, SMTP email sending, and calendar events tracking. |
| **Phase 10**| **Creative Tools (Image Gen)** | Integrate DALL-E or Stable Diffusion API for on-the-fly image creation. |
| **Phase 11**| **Streaming Responses** | Implement WebSockets or Server-Sent Events (SSE) for real-time token streaming. |
| **Phase 12**| **Docker & Deployment** | Multi-stage Dockerfiles, Docker Compose setups, and production configurations. |
| **Phase 13**| **Testing & Documentation** | Comprehensive unit/integration tests with pytest and complete API documentations. |

---

## ⏱️ Estimation & Extensibility

* **Backend Development Target:** Fully customisable backend system allowing simple API scaling.
* **Frontend Compatibility:** The API-first design (REST + WebSockets) makes it completely compatible with a future React, React Native, or Flutter frontend with minimal to no changes to the core agent logic.
