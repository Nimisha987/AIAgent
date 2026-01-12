
An intelligent, stateful AI agent that answers product questions using Retrieval-Augmented Generation (RAG) and captures high‑intent leads (name, email, platform) using a LangGraph workflow and Groq LLM.

---



* 🧠 **Intent Detection** – Greeting, product queries, and high‑intent purchase detection
* 📚 **RAG (FAISS + HuggingFace embeddings)** – Accurate answers from a local knowledge base
* 🧩 **LangGraph Workflow** – Deterministic multi‑step conversation flow
* 📝 **Lead Capture Tool** – Collects name, email, and platform
* ⚡ **Groq LLM Integration** – Fast inference using LLaMA models
* 💬 **Stateful Conversations** – Remembers user details across turns

---

```
User
  │
  ▼
Intent Detection ──► Router ──► Greeting
                         │
                         ├──► RAG (Pricing / Features)
                         │
                         └──► Lead Collection Flow
                                   ├─ Name
                                   ├─ Email
                                   ├─ Platform
                                   └─ Tool Call (mock_lead_capture)
```

---

```
task/
│
├── agent/
│   ├── graph.py          # LangGraph workflow
│   ├── intent.py         # Intent detection logic
│   ├── rag.py            # FAISS + embeddings RAG engine
│   ├── tools.py          # Lead capture tool
│   ├── memory.py         # Agent state definition
│   └── prompts.py        # System prompt
│
├── config/
│   └── settings.py       # Groq configuration
│
├── data/
│   └── knowledge_base.json
│
├── app.py                # CLI chat application
├── requirements.txt
├── .env
└── README.md
```

---

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```



```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install langchain langgraph langchain-groq langchain-community langchain-huggingface faiss-cpu python-dotenv
```

---



Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---


```bash
python app.py
```

---


```
You: hi
Agent: Hello! How can I help you with AutoStream today?

You: i want to buy pro plan
Agent: May I have your name?

You: Nimisha
Agent: Please share your email address.

You: nimisha@gmail.com
Agent: Which platform do you create content for?

You: YouTube
Agent: You are all set! Our team will contact you shortly.
```

Terminal Output:

```
Lead captured successfully:
Name: Nimisha
Email: nimisha@gmail.com
Platform: YouTube
```

---


* Python 3.11+
* LangGraph
* LangChain
* Groq API (LLaMA‑3 models)
* FAISS Vector Database
* HuggingFace Sentence Transformers

---

## 📌 Future Improvements

* WhatsApp / Web UI integration
* Persistent database for leads
* User authentication
* Multi‑language support
* Admin dashboard

---

## 📄 License

MIT License

---

## 👩‍💻 Author

Nimisha Agrawal

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!
