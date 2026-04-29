# Django 프로젝트 머지 스크립트
# 혜은's 개선사항을 Main 프로젝트로 복사

# 색상 출력 함수
function Write-Success { Write-Host $args[0] -ForegroundColor Green }
function Write-Info { Write-Host $args[0] -ForegroundColor Cyan }
function Write-Warning { Write-Host $args[0] -ForegroundColor Yellow }
function Write-Error { Write-Host $args[0] -ForegroundColor Red }

Write-Info "=========================================="
Write-Info "Django 프로젝트 머지 스크립트"
Write-Info "=========================================="
Write-Info ""

# 경로 설정
$혜은 = "c:\workspace\dijango7\프로젝트\mompjt혜은"
$main = "c:\workspace\dijango7\d0112\mompjt a"

# 경로 확인
if (-not (Test-Path $혜은)) {
    Write-Error "❌ 혜은's 프로젝트를 찾을 수 없습니다: $혜은"
    exit 1
}

if (-not (Test-Path $main)) {
    Write-Error "❌ Main 프로젝트를 찾을 수 없습니다: $main"
    exit 1
}

Write-Success "✅ 프로젝트 경로 확인 완료"
Write-Info ""

# 백업 생성 여부 확인
Write-Warning "⚠️  Main 프로젝트 백업을 생성하시겠습니까? (권장)"
$backup = Read-Host "백업 생성? (Y/N)"

if ($backup -eq "Y" -or $backup -eq "y") {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupPath = "c:\workspace\dijango7\d0112\mompjt a_backup_$timestamp"
    
    Write-Info "백업 생성 중..."
    Copy-Item $main $backupPath -Recurse
    Write-Success "✅ 백업 완료: $backupPath"
    Write-Info ""
}

# 복사할 파일 목록
$filesToCopy = @(
    # NEW 파일
    @{
        Name = "banner-slider.js"
        Source = "$혜은\static\js\banner-slider.js"
        Dest = "$main\static\js\banner-slider.js"
        Type = "NEW"
        Force = $false
    },
    @{
        Name = "banner-slider.css"
        Source = "$혜은\static\css\banner-slider.css"
        Dest = "$main\static\css\banner-slider.css"
        Type = "NEW"
        Force = $false
    },
    # 업데이트 파일
    @{
        Name = "banner.css"
        Source = "$혜은\static\css\banner.css"
        Dest = "$main\static\css\banner.css"
        Type = "UPDATE"
        Force = $true
    },
    @{
        Name = "mindcheck.js"
        Source = "$혜은\static\js\mindcheck.js"
        Dest = "$main\static\js\mindcheck.js"
        Type = "UPDATE"
        Force = $true
    },
    @{
        Name = "mindcheck-modal.css"
        Source = "$혜은\static\css\mindcheck-modal.css"
        Dest = "$main\static\css\mindcheck-modal.css"
        Type = "UPDATE"
        Force = $true
    }
)

Write-Info "=========================================="
Write-Info "파일 복사 시작"
Write-Info "=========================================="
Write-Info ""

$successCount = 0
$skipCount = 0
$errorCount = 0

foreach ($file in $filesToCopy) {
    Write-Info "처리 중: $($file.Name)"
    
    # 소스 파일 존재 확인
    if (-not (Test-Path $file.Source)) {
        Write-Error "  ❌ 소스 파일 없음: $($file.Source)"
        $errorCount++
        continue
    }
    
    # 대상 파일이 이미 존재하는지 확인
    if ((Test-Path $file.Dest) -and -not $file.Force) {
        Write-Warning "  ⚠️  파일이 이미 존재합니다. 건너뜁니다."
        $skipCount++
        continue
    }
    
    # 파일 복사
    try {
        # 대상 디렉토리 생성 (없으면)
        $destDir = Split-Path $file.Dest -Parent
        if (-not (Test-Path $destDir)) {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
        }
        
        Copy-Item $file.Source $file.Dest -Force
        
        if ($file.Type -eq "NEW") {
            Write-Success "  ✅ NEW 파일 추가 완료"
        } else {
            Write-Success "  ✅ 파일 업데이트 완료"
        }
        
        # 파일 크기 표시
        $size = (Get-Item $file.Dest).Length
        $sizeKB = [math]::Round($size / 1KB, 2)
        Write-Info "     크기: $sizeKB KB"
        
        $successCount++
    }
    catch {
        Write-Error "  ❌ 복사 실패: $_"
        $errorCount++
    }
    
    Write-Info ""
}

# 결과 요약
Write-Info "=========================================="
Write-Info "복사 결과"
Write-Info "=========================================="
Write-Success "✅ 성공: $successCount 파일"
if ($skipCount -gt 0) {
    Write-Warning "⚠️  건너뜀: $skipCount 파일"
}
if ($errorCount -gt 0) {
    Write-Error "❌ 실패: $errorCount 파일"
}
Write-Info ""

# 다음 단계 안내
if ($successCount -gt 0) {
    Write-Info "=========================================="
    Write-Info "📋 다음 단계"
    Write-Info "=========================================="
    Write-Info "1. base.html에 배너 슬라이더 통합"
    Write-Info "   - <script src='{% static 'js/banner-slider.js' %}'></script>"
    Write-Info "   - <link rel='stylesheet' href='{% static 'css/banner-slider.css' %}'>"
    Write-Info ""
    Write-Info "2. 배너 HTML 구조 추가"
    Write-Info "   - <div class='banner2-track'>...</div>"
    Write-Info ""
    Write-Info "3. collectstatic 실행"
    Write-Info "   - python manage.py collectstatic --noinput"
    Write-Info ""
    Write-Info "4. 서버 재시작 및 테스트"
    Write-Info "   - python manage.py runserver"
    Write-Info ""
    Write-Info "=========================================="
    Write-Info ""
}

# staticfiles에도 복사 필요 여부 확인
Write-Warning "⚠️  staticfiles 디렉토리에도 복사하시겠습니까?"
Write-Info "   (개발 환경에서는 선택사항, 배포 시에는 collectstatic 사용)"
$copyStatic = Read-Host "staticfiles에 복사? (Y/N)"

if ($copyStatic -eq "Y" -or $copyStatic -eq "y") {
    Write-Info ""
    Write-Info "staticfiles에 복사 중..."
    
    foreach ($file in $filesToCopy) {
        # static/ → staticfiles/로 경로 변경
        $staticDest = $file.Dest -replace "\\static\\", "\staticfiles\"
        
        if (Test-Path $file.Source) {
            # 디렉토리 생성
            $destDir = Split-Path $staticDest -Parent
            if (-not (Test-Path $destDir)) {
                New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            }
            
            Copy-Item $file.Source $staticDest -Force
            Write-Success "  ✅ $($file.Name) → staticfiles"
        }
    }
    
    Write-Success "✅ staticfiles 복사 완료"
}

Write-Info ""
Write-Success "=========================================="
Write-Success "🎉 스크립트 실행 완료!"
Write-Success "=========================================="
