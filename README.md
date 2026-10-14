## Setup
1. Clone the repository
```bash
git clone https://github.com/sarah-larkin/uil_1.git

cd uil_1
```
2. Create a virtual environment
```bash
python -m venv venv

source venv/bin/activate
```
3. Install dependencies
```python
pip install requests
```

4. Add your local configuration
Create a file at:

```
config/settings.json
```
Use this structure:
```json
{
    "visco_base_url": "<your-visco-url>/ViscoMobile.aspx",
    "action": "getScan",
    "function": "InventoryManagement",
    "token": "<your-token>",
    "database_path": "data/inventory.db"
}
```
This is included in the gitignore and will not be committed. 

5. Run the ETL
```python
python src/main.py
```

