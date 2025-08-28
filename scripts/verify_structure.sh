
#!/bin/bash

echo "🔍 Verifying repository structure..."

# Define required folders
folders=(
  "src/api"
  "src/training"
  "src/frontend"
  "docs"
  "configs"
  "scripts"
)

# Define required files
files=(
  "configs/default.yaml"
  "requirements.txt"
  "README.md"
  "submission/SUBMISSION.md"
)

# Check folders
for folder in "${folders[@]}"; do
  if [ -d "$folder" ]; then
    echo "✅ Found folder: $folder"
  else
    echo "❌ Missing folder: $folder"
  fi
done

# Check files
for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    echo "✅ Found file: $file"
  else
    echo "❌ Missing file: $file"
  fi
done

echo "✅ Verification complete!"
