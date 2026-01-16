# 🚀 GitHub Repository Setup Guide for Streamlit Cloud

This guide will help you set up your GitHub repository to deploy your Bangalore House Price Prediction app on Streamlit Cloud.

## 📋 Required Files Checklist

Make sure these files are in your GitHub repository root:

### ✅ Essential Files (MUST HAVE)

- [x] `app.py` - Main Streamlit application
- [x] `requirements.txt` - Python dependencies
- [x] `RidgeModel.pkl` - Trained machine learning model
- [x] `Cleaned_data.csv` - Preprocessed dataset
- [x] `README.md` - Project documentation
- [x] `.streamlit/config.toml` - Streamlit configuration (optional but recommended)

### 📁 Optional Files (Nice to Have)

- [ ] `Bangalore_House_Price_Prediction.ipynb` - Jupyter notebook (for reference)
- [ ] `Bengaluru_House_Data.csv` - Original dataset (for reference)
- [ ] `.gitignore` - Git ignore file
- [ ] `Description.pdf` - Project description

## 🔧 Step-by-Step GitHub Setup

### Step 1: Initialize Git Repository (if not already done)

```bash
# Navigate to your project directory
cd "Bangalore House Price Prediction"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Bangalore House Price Prediction app"
```

### Step 2: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository name: `bangalore-house-price-prediction` (or your preferred name)
4. Description: "Machine Learning app to predict house prices in Bangalore"
5. Choose **Public** (required for free Streamlit Cloud) or **Private**
6. **DO NOT** initialize with README, .gitignore, or license (you already have these)
7. Click **"Create repository"**

### Step 3: Connect Local Repository to GitHub

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/bangalore-house-price-prediction.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 4: Verify Files on GitHub

1. Go to your repository on GitHub
2. Verify these files are present:
   - ✅ `app.py`
   - ✅ `requirements.txt`
   - ✅ `RidgeModel.pkl`
   - ✅ `Cleaned_data.csv`
   - ✅ `README.md`
   - ✅ `.streamlit/config.toml` (if you created it)

## ☁️ Streamlit Cloud Deployment

### Step 5: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Fill in the details:
   - **Repository**: Select `YOUR_USERNAME/bangalore-house-price-prediction`
   - **Branch**: `main` (or `master`)
   - **Main file path**: `app.py`
   - **App URL**: (auto-generated, you can customize)
5. Click **"Deploy"**
6. Wait for the build to complete (usually 1-2 minutes)

## 🔍 Troubleshooting

### Issue: "File not found" error

**Solution**: Make sure all required files are committed and pushed to GitHub:
```bash
git status  # Check if any files are untracked
git add .    # Add all files
git commit -m "Add missing files"
git push     # Push to GitHub
```

### Issue: "Invalid requirement" error

**Solution**: Check `requirements.txt` format:
- One package per line
- No empty lines at the end
- No version constraints (or use compatible versions)

### Issue: Large file upload fails

**Solution**: Your files are small enough, but if you encounter this:
- Use Git LFS for large files: `git lfs track "*.pkl" "*.csv"`
- Or compress files before committing

### Issue: Model file not loading

**Solution**: 
- Verify `RidgeModel.pkl` is in the root directory
- Check file path in `app.py` matches exactly: `'RidgeModel.pkl'`
- Ensure the file is committed: `git ls-files | grep RidgeModel.pkl`

## 📝 Quick Commands Reference

```bash
# Check repository status
git status

# Add all files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# Check if files are tracked
git ls-files

# View file sizes
git ls-files -z | xargs -0 du -h | sort -h
```

## ✅ Final Checklist Before Deployment

- [ ] All files committed to Git
- [ ] All files pushed to GitHub
- [ ] `requirements.txt` is in root directory
- [ ] `app.py` is in root directory
- [ ] `RidgeModel.pkl` is in root directory
- [ ] `Cleaned_data.csv` is in root directory
- [ ] Repository is public (for free Streamlit Cloud) or you have Streamlit Cloud Pro
- [ ] Main branch is `main` or `master`

## 🎉 You're Ready!

Once deployed, your app will be live at:
`https://YOUR_APP_NAME.streamlit.app`

Share this URL with others to use your Bangalore House Price Prediction app!
