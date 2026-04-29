"""
Detailed Change Analysis
Analyzes modified files to identify specific changes and their sources
"""

import os
import re
from pathlib import Path

def search_markers(filepath, markers):
    """Search for date/author markers in file"""
    found = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
            
            for i, line in enumerate(lines, 1):
                for marker in markers:
                    if marker in line:
                        # Get context (3 lines before and after)
                        start = max(0, i-4)
                        end = min(len(lines), i+3)
                        context = '\n'.join(lines[start:end])
                        found.append({
                            'line': i,
                            'marker': marker,
                            'text': line.strip(),
                            'context': context
                        })
    except:
        pass
    
    return found

def analyze_changes():
    """Analyze specific changes in modified files"""
    base_dir = Path(r"c:\workspace\dijango7")
    
    성훈_dir = base_dir / "프로젝트" / "mompjt성훈"
    혜은_dir = base_dir / "프로젝트" / "mompjt혜은"
    main_dir = base_dir / "d0112" / "mompjt a"
    
    # Markers to search for
    markers = ['성훈', '혜은', '0105', '0106', '0107', '0108', '0109', '1231', '26-01']
    
    # Key files to analyze in detail
    key_files = [
        'accounts/views.py',
        'accounts/urls.py',
        'board/views.py',
        'board/urls.py',
        'board/models.py',
        'main/views.py',
        'main/urls.py',
        'mompjt/settings.py',
        'chat/views.py',
    ]
    
    print("=" * 100)
    print("DETAILED CHANGE ANALYSIS")
    print("=" * 100)
    
    for file_path in key_files:
        print(f"\n{'='*100}")
        print(f"📄 FILE: {file_path}")
        print('='*100)
        
        성훈_file = 성훈_dir / file_path.replace('/', '\\')
        혜은_file = 혜은_dir / file_path.replace('/', '\\')
        main_file = main_dir / file_path.replace('/', '\\')
        
        # Check 성훈's version
        if 성훈_file.exists():
            print(f"\n🔹 성훈's version:")
            markers_found = search_markers(성훈_file, markers)
            if markers_found:
                for m in markers_found[:5]:  # Show first 5
                    print(f"  Line {m['line']}: {m['text'][:100]}")
            else:
                print("  (No markers found)")
        
        # Check 혜은's version
        if 혜은_file.exists():
            print(f"\n🔸 혜은's version:")
            markers_found = search_markers(혜은_file, markers)
            if markers_found:
                for m in markers_found[:5]:  # Show first 5
                    print(f"  Line {m['line']}: {m['text'][:100]}")
            else:
                print("  (No markers found)")
        
        # Check main version
        if main_file.exists():
            print(f"\n🔷 Main version:")
            markers_found = search_markers(main_file, markers)
            if markers_found:
                for m in markers_found[:5]:  # Show first 5
                    print(f"  Line {m['line']}: {m['text'][:100]}")
            else:
                print("  (No markers found)")
    
    # Now check which files have NEW features
    print("\n\n" + "=" * 100)
    print("🎯 FEATURE-SPECIFIC ANALYSIS")
    print("=" * 100)
    
    # Check for mind check feature (혜은)
    print("\n📊 Mind Check Feature (혜은):")
    mind_check_files = [
        'board/views.py',
        'static/js/mindcheck.js',
        'staticfiles/css/mindcheck-modal.css',
        'board/urls.py'
    ]
    for f in mind_check_files:
        혜은_path = 혜은_dir / f.replace('/', '\\')
        main_path = main_dir / f.replace('/', '\\')
        if 혜은_path.exists():
            print(f"  ✓ {f} - Exists in 혜은")
            if main_path.exists():
                # Check if content differs
                try:
                    with open(혜은_path, 'rb') as f1, open(main_path, 'rb') as f2:
                        if f1.read() != f2.read():
                            print(f"    ⚠️  Different from main")
                        else:
                            print(f"    ✓ Same as main")
                except:
                    pass
            else:
                print(f"    ⚠️  Not in main")
    
    # Check for mypage features (성훈)
    print("\n👤 MyPage Features (성훈):")
    mypage_markers = search_markers(성훈_dir / "accounts" / "views.py", ['mypage', '0105', '성훈'])
    if mypage_markers:
        print(f"  Found {len(mypage_markers)} mypage-related changes")
        for m in mypage_markers[:3]:
            print(f"    Line {m['line']}: {m['text'][:80]}")
    
    # Check for banner slider (혜은)
    print("\n🎨 Banner Slider Feature (혜은):")
    banner_files = [
        'static/css/banner-slider.css',
        'static/js/banner-slider.js',
        'static/css/banner.css'
    ]
    for f in banner_files:
        혜은_path = 혜은_dir / f.replace('/', '\\')
        if 혜은_path.exists():
            print(f"  ✓ {f} - Exists in 혜은")
        else:
            print(f"  ✗ {f} - Not found")
    
    print("\n" + "=" * 100)
    print("ANALYSIS COMPLETE")
    print("=" * 100)

if __name__ == "__main__":
    analyze_changes()
