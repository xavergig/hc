# Security Guidelines

## 🚨 NEVER Commit These Files

The following files and patterns are blocked by `.gitignore` to prevent secrets from leaking:

- `.env*` files (environment variables)
- `*.key`, `*.pem`, `*.p12`, `*.pfx` (certificates/keys)
- `secrets/`, `credentials/` directories
- `local_settings.py` (Django local settings)
- Backup files (`*.bak`, `*.backup`)

## 🛡️ Environment Variables

1. **Use `.env.example` as a template**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

2. **Never commit `.env` files**
   - `.env` is in `.gitignore`
   - Add your actual secrets to `.env` only

3. **Load environment variables in Django**
   ```python
   # In settings.py
   from dotenv import load_dotenv
   load_dotenv()
   ```

## 🔍 Secret Detection

This project uses pre-commit hooks to detect secrets:

1. **Install pre-commit**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

2. **Run secret detection**
   ```bash
   detect-secrets scan --baseline .secrets.baseline
   ```

3. **Check before committing**
   ```bash
   pre-commit run --all-files
   ```

## 📋 Security Checklist

Before committing code:

- [ ] No hardcoded secrets in code
- [ ] Environment variables used instead
- [ ] `.env` file exists and is ignored
- [ ] Pre-commit hooks pass
- [ ] No API keys, passwords, or tokens in code
- [ ] Database credentials in environment variables only

## 🚨 If You Accidentally Commit a Secret

1. **Immediately remove the secret from the code**
2. **Remove from git history** (if already pushed):
   ```bash
   git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch filename.py' --prune-empty --tag-name-filter cat -- --all
   ```
3. **Rotate the compromised secret**
4. **Force push to remove from GitHub**
5. **Consider repository as compromised**

## 🔐 Recommended Django Security Packages

Add to `requirements.txt`:
```
python-decouple  # For environment variables
django-environ   # Alternative environment manager
django-cors-headers  # CORS security
```
