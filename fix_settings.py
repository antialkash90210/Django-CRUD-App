import os
import sys

# Найти файл settings.py
settings_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'settings.py':
            settings_files.append(os.path.join(root, file))

if not settings_files:
    print("No settings.py found!")
    sys.exit(1)

for settings_file in settings_files:
    print(f"Checking {settings_file}")
    
    with open(settings_file, 'r') as f:
        content = f.read()
    
    # Проверить есть ли STATIC_ROOT
    if 'STATIC_ROOT' not in content:
        print(f"Adding STATIC_ROOT to {settings_file}")
        
        # Найти BASE_DIR
        if 'BASE_DIR' in content:
            # Добавить после импортов или после BASE_DIR
            lines = content.split('\n')
            new_lines = []
            base_dir_found = False
            
            for line in lines:
                new_lines.append(line)
                if 'BASE_DIR' in line and not base_dir_found:
                    new_lines.append('')
                    new_lines.append('# Static files (CSS, JavaScript, Images)')
                    new_lines.append('STATIC_ROOT = os.path.join(BASE_DIR, \'staticfiles\')')
                    new_lines.append('STATIC_URL = \'/static/\'')
                    base_dir_found = True
            
            new_content = '\n'.join(new_lines)
            
            with open(settings_file, 'w') as f:
                f.write(new_content)
            print(f"Fixed {settings_file}")
        else:
            print(f"BASE_DIR not found in {settings_file}")
