# Log Parser & Report Tool

**TL;DR:** A simple Python tool to parse Apache/Nginx access logs and generate CSV + summary reports.  
*(Educational & defensive project — run only on your own logs / lab environments.)*


## Features
- Parse common Apache/Nginx log formats
- Export to CSV for further analysis
- Generate summary (top IPs, HTTP methods, response codes)

## Why I built this
- Practice Python scripting for cybersecurity
- Show log analysis skills
- Build defensive tools for portfolio

## How to Run
1. Clone repo:
   ```bash
   git clone https://github.com/G41US/log-parser-tool.git
   cd log-parser-tool
   ```
2. Install deps:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run parser:
   ```bash
   python src/parser.py sample_logs/access.log output.csv
   ```

## Tests
```bash
pytest -q
```

## Files
- `src/` — main code
- `tests/` — unit tests
- `sample_logs/` — demo logs
- `.github/workflows/ci.yml` — CI pipeline

## Ethics
⚠️ **Use only on logs you are authorized to access.**  
This tool is for educational & defensive purposes.

## License
MIT

## Contact
Gaius Marvelous — [LinkedIn](https://linkedin.com/in/marvelous-gaius-643358256)
