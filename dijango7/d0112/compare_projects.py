"""
Django Project Comparison Script
Compares files between mompjt성훈, mompjt혜은, and mompjt a (main)
"""

import os
import hashlib
from pathlib import Path
import json

def get_file_hash(filepath):
    """Get MD5 hash of file"""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return None

def get_file_list(root_dir, extensions=['.py', '.html', '.css', '.js']):
    """Get all files with given extensions, excluding migrations and cache"""
    files = []
    exclude_dirs = {'migrations', '__pycache__', 'staticfiles\\admin', '.git', 'media'}
    
    for root, dirs, filenames in os.walk(root_dir):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs and 'admin' not in root]
        
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, root_dir)
                files.append((rel_path, full_path))
    
    return files

def compare_projects():
    """Main comparison function"""
    base_dir = Path(r"c:\workspace\dijango7")
    
    성훈_dir = base_dir / "프로젝트" / "mompjt성훈"
    혜은_dir = base_dir / "프로젝트" / "mompjt혜은"
    main_dir = base_dir / "d0112" / "mompjt a"
    
    print("=" * 80)
    print("DJANGO PROJECT COMPARISON REPORT")
    print("=" * 80)
    print(f"Main Project: {main_dir}")
    print(f"성훈's Version: {성훈_dir}")
    print(f"혜은's Version: {혜은_dir}")
    print("=" * 80)
    
    # Get file lists
    print("\n⏳ Scanning files...")
    성훈_files = dict(get_file_list(성훈_dir))
    혜은_files = dict(get_file_list(혜은_dir))
    main_files = dict(get_file_list(main_dir))
    
    print(f"  성훈: {len(성훈_files)} files")
    print(f"  혜은: {len(혜은_files)} files")
    print(f"  Main: {len(main_files)} files")
    
    # Results
    results = {
        '성훈': {'new': [], 'modified': [], 'identical': []},
        '혜은': {'new': [], 'modified': [], 'identical': []}
    }
    
    # Compare 성훈's files
    print("\n🔍 Comparing 성훈's version...")
    for rel_path, full_path in 성훈_files.items():
        if rel_path in main_files:
            성훈_hash = get_file_hash(full_path)
            main_hash = get_file_hash(main_files[rel_path])
            
            if 성훈_hash != main_hash:
                성훈_size = os.path.getsize(full_path)
                main_size = os.path.getsize(main_files[rel_path])
                results['성훈']['modified'].append({
                    'path': rel_path,
                    '성훈_size': 성훈_size,
                    'main_size': main_size,
                    'size_diff': 성훈_size - main_size
                })
            else:
                results['성훈']['identical'].append(rel_path)
        else:
            results['성훈']['new'].append(rel_path)
    
    # Compare 혜은's files
    print("🔍 Comparing 혜은's version...")
    for rel_path, full_path in 혜은_files.items():
        if rel_path in main_files:
            혜은_hash = get_file_hash(full_path)
            main_hash = get_file_hash(main_files[rel_path])
            
            if 혜은_hash != main_hash:
                혜은_size = os.path.getsize(full_path)
                main_size = os.path.getsize(main_files[rel_path])
                results['혜은']['modified'].append({
                    'path': rel_path,
                    '혜은_size': 혜은_size,
                    'main_size': main_size,
                    'size_diff': 혜은_size - main_size
                })
            else:
                results['혜은']['identical'].append(rel_path)
        else:
            results['혜은']['new'].append(rel_path)
    
    # Check for files only in main (might indicate deletions)
    main_only = set(main_files.keys()) - set(성훈_files.keys()) - set(혜은_files.keys())
    
    # Print results
    print("\n" + "=" * 80)
    print("📊 COMPARISON RESULTS")
    print("=" * 80)
    
    # 성훈's NEW files
    print("\n" + "🆕 NEW FILES - 성훈 (%d files)" % len(results['성훈']['new']))
    print("-" * 80)
    if results['성훈']['new']:
        for f in sorted(results['성훈']['new']):
            print(f"  ✨ {f}")
    else:
        print("  (None)")
    
    # 성훈's MODIFIED files
    print("\n" + "📝 MODIFIED FILES - 성훈 (%d files)" % len(results['성훈']['modified']))
    print("-" * 80)
    if results['성훈']['modified']:
        for item in sorted(results['성훈']['modified'], key=lambda x: abs(x['size_diff']), reverse=True):
            size_indicator = "+" if item['size_diff'] > 0 else ""
            print(f"  🔧 {item['path']}")
            print(f"      성훈: {item['성훈_size']:,} bytes | Main: {item['main_size']:,} bytes | Diff: {size_indicator}{item['size_diff']:,} bytes")
    else:
        print("  (None)")
    
    # 혜은's NEW files
    print("\n" + "🆕 NEW FILES - 혜은 (%d files)" % len(results['혜은']['new']))
    print("-" * 80)
    if results['혜은']['new']:
        for f in sorted(results['혜은']['new']):
            print(f"  ✨ {f}")
    else:
        print("  (None)")
    
    # 혜은's MODIFIED files
    print("\n" + "📝 MODIFIED FILES - 혜은 (%d files)" % len(results['혜은']['modified']))
    print("-" * 80)
    if results['혜은']['modified']:
        for item in sorted(results['혜은']['modified'], key=lambda x: abs(x['size_diff']), reverse=True):
            size_indicator = "+" if item['size_diff'] > 0 else ""
            print(f"  🔧 {item['path']}")
            print(f"      혜은: {item['혜은_size']:,} bytes | Main: {item['main_size']:,} bytes | Diff: {size_indicator}{item['size_diff']:,} bytes")
    else:
        print("  (None)")
    
    # Files only in main
    print("\n" + "⚠️  FILES ONLY IN MAIN (%d files)" % len(main_only))
    print("-" * 80)
    if main_only:
        for f in sorted(main_only)[:20]:  # Show first 20
            print(f"  🔹 {f}")
        if len(main_only) > 20:
            print(f"  ... and {len(main_only) - 20} more")
    else:
        print("  (None)")
    
    # Summary
    print("\n" + "=" * 80)
    print("📋 SUMMARY")
    print("=" * 80)
    print(f"성훈's version:")
    print(f"  - {len(results['성훈']['new'])} NEW files")
    print(f"  - {len(results['성훈']['modified'])} MODIFIED files")
    print(f"  - {len(results['성훈']['identical'])} IDENTICAL files")
    print(f"\n혜은's version:")
    print(f"  - {len(results['혜은']['new'])} NEW files")
    print(f"  - {len(results['혜은']['modified'])} MODIFIED files")
    print(f"  - {len(results['혜은']['identical'])} IDENTICAL files")
    print(f"\nMain project has {len(main_only)} files not in either source")
    
    # Save detailed results
    output_file = Path(r"c:\workspace\dijango7\d0112\comparison_results.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Detailed results saved to: {output_file}")
    
    return results

if __name__ == "__main__":
    compare_projects()
