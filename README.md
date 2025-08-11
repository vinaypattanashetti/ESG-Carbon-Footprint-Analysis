# ESG CarbonScope - Smart Carbon Accounting Tool leveraging AI Agents for ESG Insights

![Carbon Footprint](https://img.shields.io/badge/Carbon-Footprint-green)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-AI%20Agents-blue)
![Groq](https://img.shields.io/badge/Groq-LLM-purple)

A carbon accounting and reporting tool for SMEs in Asia, with AI-powered insights and data entry.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [AI Agents](#-ai-agents)
- [Data Structure](#-data-structure)
- [License](#-license)

## ✨ Features

### Core Features
- **Enterprise-Grade Data Entry**: Comprehensive form with business unit tracking, project categorization, facility details, and data quality indicators
- **Dashboard Visualization**: Interactive charts and graphs for emissions data analysis
- **AI-Powered Insights**: Specialized AI agents for various carbon accounting tasks
- **Data Management**: CSV import/export, robust error handling, and automatic backups
- **Multilingual Support**: Available in multiple languages

### AI Agent Features
| Agent | Role |
|-------|------|
| Data Entry Assistant | Helps users classify emissions, map to scopes, and validate data entries |
| Report Summary Generator | Converts emission data into human-readable summaries |
| Carbon Offset Advisor | Suggests verified offset options based on user profile and location |
| Regulation Radar | Notifies users of upcoming compliance needs |
| Emission Optimizer | Uses historical data to suggest reductions and savings |

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       ESG CarbonScope                          │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                ┌─────────────────────────────────────┐
                │                                     │
┌───────────────▼───────────────┐       ┌─────────────▼─────────────┐
│      Frontend (Streamlit)     │       │      Backend Services     │
│                               │       │                           │
│  ┌─────────────────────────┐  │       │  ┌─────────────────────┐  │
│  │    Navigation System    │  │       │  │   Data Management   │  │
│  │  - Dashboard            │  │       │  │  - JSON Storage     │  │
│  │  - Data Entry           │  │       │  │  - CSV Import       │  │
│  │  - AI Insights          │  │       │  │  - Backup System    │  │
│  │  - Settings             │  │       │  └─────────────────────┘  │
│  └─────────────────────────┘  │       │                           │
│                               │       │  ┌─────────────────────┐  │
│  ┌─────────────────────────┐  │       │  │  AI Agent System    │  │
│  │   Data Entry Module     │  │       │  │  - CrewAI Framework │  │
│  │  - Enterprise Form      │◄─┼───────┼──┤  - Groq LLM         │  │
│  │  - Validation           │  │       │  │  - Specialized      │  │
│  │  - AI Suggestions       │  │       │  │    Agent Roles      │  │
│  └─────────────────────────┘  │       │  └─────────────────────┘  │
│                               │       │                           │
│  ┌─────────────────────────┐  │       │  ┌─────────────────────┐  │
│  │   Dashboard Module      │  │       │  │  Analytics Engine   │  │
│  │  - Emissions Overview   │◄─┼───────┼──┤  - Data Processing  │  │
│  │  - Charts & Graphs      │  │       │  │  - Calculations     │  │
│  │  - Filtering            │  │       │  │  - Visualization    │  │
│  └─────────────────────────┘  │       │  └─────────────────────┘  │
└───────────────────────────────┘       └───────────────────────────┘
```

## 🚀 Installation

### Prerequisites
- Python 3.10+
- Groq API key (for AI features)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/vinaypattanashetti/ESG-Carbon-Footprint-Analysis/main.git
cd ESG-Carbon-Footprint-Analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

## ⚙️ Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key for AI agent functionality

### Data Storage
- Emissions data is stored in `data/emissions.json`
- Company settings are stored in `data/settings.json`
- Automatic backups are created for corrupted files with timestamped filenames

## 📊 Usage

### Running the Application

```bash
streamlit run app.py
```

### Navigation
- **Dashboard**: View emissions data visualizations and analytics
- **Data Entry**: Add new emission entries with enterprise-grade form
- **AI Insights**: Access specialized AI agents for carbon accounting assistance
- **Settings**: Configure company information and preferences

### Data Entry Form
The enhanced enterprise-grade data entry form includes:
- Business unit and project tracking
- Facility location and responsible person fields
- Data quality indicators and verification status
- AI-powered emission factor suggestions
- Financial impact tracking (optional)

### CSV Import/Export
- Upload CSV files with emissions data
- Download sample CSV template
- Export emissions data as CSV or PDF reports

## 🤖 AI Agents

ESG CarbonScope integrates five specialized AI agents using CrewAI and Groq LLM:

1. **Data Entry Assistant**: Helps classify emissions and validate data entries
2. **Report Summary Generator**: Creates human-readable summaries from emissions data
3. **Carbon Offset Advisor**: Recommends verified carbon offset options
4. **Regulation Radar**: Provides updates on compliance requirements
5. **Emission Optimizer**: Suggests ways to reduce emissions based on historical data

### AI Agent Implementation

```python
from crewai import Agent, Task, Crew, Process
from crewai.llms import LLM

# Initialize LLM
llm = LLM(provider="groq", model="llama3-70b-8192")

# Create an agent
data_entry_assistant = Agent(
    llm=llm,
    role="Data Entry Assistant",
    goal="Help users classify emissions, map to scopes, and validate data entries",
    backstory="You are an expert in carbon accounting who helps users correctly categorize "
             "their emissions data and ensure it's properly mapped to the right scope.",
    allow_delegation=False,
    verbose=False
)

# Create a task
data_entry_task = Task(
    description="Analyze the user's emission data and provide guidance on classification",
    agent=data_entry_assistant
)

# Create and run a crew
crew = Crew(
    agents=[data_entry_assistant],
    tasks=[data_entry_task],
    verbose=False,
    process=Process.sequential
)

result = crew.kickoff(inputs={"user_query": "How should I categorize my company's electricity usage?"})
```

## 📁 Data Structure

### Emissions Data Format

```json
{
  "date": "2025-01-15",
  "business_unit": "Corporate",
  "project": "Carbon Reduction Initiative",
  "scope": "Scope 2",
  "category": "Electricity",
  "activity": "Office Electricity",
  "country": "India",
  "facility": "Mumbai HQ",
  "responsible_person": "Rahul Sharma",
  "quantity": 1000.0,
  "unit": "kWh",
  "emission_factor": 0.82,
  "emissions_kgCO2e": 820.0,
  "data_quality": "High",
  "verification_status": "Internally Verified",
  "notes": "Monthly electricity bill"
}
```


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Built by Vinay Pattanashetti with 💚 for a sustainable future
