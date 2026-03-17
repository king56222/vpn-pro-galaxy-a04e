#!/data/data/com.termux/files/usr/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}              الفحص النهائي لمشروع VPN Pro${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"

# Counter for passed/failed tests
PASSED=0
FAILED=0
TOTAL=0

check() {
    TOTAL=$((TOTAL+1))
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ $1${NC}"
        PASSED=$((PASSED+1))
    else
        echo -e "${RED}❌ $1${NC}"
        FAILED=$((FAILED+1))
    fi
}

# 1. التحقق من هيكل المجلدات
echo -e "\n${YELLOW}📁 1. التحقق من هيكل المجلدات:${NC}"
[ -d "src" ] && echo -e "${GREEN}✅ src موجود${NC}" || echo -e "${RED}❌ src مفقود${NC}"
[ -d "config" ] && echo -e "${GREEN}✅ config موجود${NC}" || echo -e "${RED}❌ config مفقود${NC}"
[ -d "templates" ] && echo -e "${GREEN}✅ templates موجود${NC}" || echo -e "${RED}❌ templates مفقود${NC}"
[ -d "static" ] && echo -e "${GREEN}✅ static موجود${NC}" || echo -e "${RED}❌ static مفقود${NC}"
[ -d "scripts" ] && echo -e "${GREEN}✅ scripts موجود${NC}" || echo -e "${RED}❌ scripts مفقود${NC}"
[ -d "docs" ] && echo -e "${GREEN}✅ docs موجود${NC}" || echo -e "${RED}❌ docs مفقود${NC}"
[ -d "tests" ] && echo -e "${GREEN}✅ tests موجود${NC}" || echo -e "${RED}❌ tests مفقود${NC}"

# 2. التحقق من ملفات Python في src
echo -e "\n${YELLOW}🐍 2. التحقق من ملفات Python:${NC}"
[ -f "src/__init__.py" ] && echo -e "${GREEN}✅ src/__init__.py موجود${NC}" || echo -e "${RED}❌ src/__init__.py مفقود${NC}"
[ -f "src/main.py" ] && echo -e "${GREEN}✅ src/main.py موجود${NC}" || echo -e "${RED}❌ src/main.py مفقود${NC}"
[ -f "src/vpn_manager.py" ] && echo -e "${GREEN}✅ src/vpn_manager.py موجود${NC}" || echo -e "${RED}❌ src/vpn_manager.py مفقود${NC}"
[ -f "src/web_interface.py" ] && echo -e "${GREEN}✅ src/web_interface.py موجود${NC}" || echo -e "${RED}❌ src/web_interface.py مفقود${NC}"
[ -f "src/utils.py" ] && echo -e "${GREEN}✅ src/utils.py موجود${NC}" || echo -e "${RED}❌ src/utils.py مفقود${NC}"

# 3. التحقق من ملفات الإعدادات
echo -e "\n${YELLOW}⚙️ 3. التحقق من ملفات الإعدادات:${NC}"
[ -f "config/servers.json" ] && echo -e "${GREEN}✅ config/servers.json موجود${NC}" || echo -e "${RED}❌ config/servers.json مفقود${NC}"
[ -f "config/settings.json" ] && echo -e "${GREEN}✅ config/settings.json موجود${NC}" || echo -e "${RED}❌ config/settings.json مفقود${NC}"

# 4. التحقق من صحة JSON
echo -e "\n${YELLOW}📊 4. التحقق من صحة ملفات JSON:${NC}"
if [ -f "config/servers.json" ]; then
    python3 -c "import json; json.load(open('config/servers.json'))" 2>/dev/null
    check "ملف servers.json صحيح"
else
    echo -e "${RED}❌ ملف servers.json غير موجود${NC}"
fi

if [ -f "config/settings.json" ]; then
    python3 -c "import json; json.load(open('config/settings.json'))" 2>/dev/null
    check "ملف settings.json صحيح"
else
    echo -e "${RED}❌ ملف settings.json غير موجود${NC}"
fi

# 5. التحقق من ملفات الويب
echo -e "\n${YELLOW}🌐 5. التحقق من ملفات الويب:${NC}"
[ -f "templates/index.html" ] && echo -e "${GREEN}✅ templates/index.html موجود${NC}" || echo -e "${RED}❌ templates/index.html مفقود${NC}"
[ -f "static/css/style.css" ] && echo -e "${GREEN}✅ static/css/style.css موجود${NC}" || echo -e "${RED}❌ static/css/style.css مفقود${NC}"
[ -f "static/js/app.js" ] || echo -e "${YELLOW}⚠️ static/js/app.js غير موجود (اختياري)${NC}"

# 6. التحقق من ملفات السكريبتات
echo -e "\n${YELLOW}📜 6. التحقق من ملفات السكريبتات:${NC}"
[ -f "scripts/install.sh" ] && echo -e "${GREEN}✅ scripts/install.sh موجود${NC}" || echo -e "${RED}❌ scripts/install.sh مفقود${NC}"
[ -f "scripts/start.sh" ] && echo -e "${GREEN}✅ scripts/start.sh موجود${NC}" || echo -e "${RED}❌ scripts/start.sh مفقود${NC}"
[ -f "scripts/stop.sh" ] && echo -e "${GREEN}✅ scripts/stop.sh موجود${NC}" || echo -e "${RED}❌ scripts/stop.sh مفقود${NC}"
[ -f "scripts/update_servers.py" ] && echo -e "${GREEN}✅ scripts/update_servers.py موجود${NC}" || echo -e "${RED}❌ scripts/update_servers.py مفقود${NC}"

# 7. التحقق من صلاحيات التنفيذ
echo -e "\n${YELLOW}🔐 7. التحقق من صلاحيات التنفيذ:${NC}"
[ -x "scripts/install.sh" ] && echo -e "${GREEN}✅ install.sh قابل للتنفيذ${NC}" || echo -e "${RED}❌ install.sh غير قابل للتنفيذ${NC}"
[ -x "scripts/start.sh" ] && echo -e "${GREEN}✅ start.sh قابل للتنفيذ${NC}" || echo -e "${RED}❌ start.sh غير قابل للتنفيذ${NC}"
[ -x "scripts/stop.sh" ] && echo -e "${GREEN}✅ stop.sh قابل للتنفيذ${NC}" || echo -e "${RED}❌ stop.sh غير قابل للتنفيذ${NC}"

# 8. التحقق من ملفات التوثيق
echo -e "\n${YELLOW}📚 8. التحقق من ملفات التوثيق:${NC}"
[ -f "README.md" ] && echo -e "${GREEN}✅ README.md موجود${NC}" || echo -e "${RED}❌ README.md مفقود${NC}"
[ -f "README.ar.md" ] && echo -e "${GREEN}✅ README.ar.md موجود${NC}" || echo -e "${RED}❌ README.ar.md مفقود${NC}"
[ -f "README.en.md" ] && echo -e "${GREEN}✅ README.en.md موجود${NC}" || echo -e "${RED}❌ README.en.md مفقود${NC}"
[ -f "LICENSE" ] && echo -e "${GREEN}✅ LICENSE موجود${NC}" || echo -e "${RED}❌ LICENSE مفقود${NC}"
[ -f "CONTRIBUTING.md" ] && echo -e "${GREEN}✅ CONTRIBUTING.md موجود${NC}" || echo -e "${RED}❌ CONTRIBUTING.md مفقود${NC}"
[ -f "requirements.txt" ] && echo -e "${GREEN}✅ requirements.txt موجود${NC}" || echo -e "${RED}❌ requirements.txt مفقود${NC}"
[ -f "setup.py" ] && echo -e "${GREEN}✅ setup.py موجود${NC}" || echo -e "${RED}❌ setup.py مفقود${NC}"
[ -f ".gitignore" ] && echo -e "${GREEN}✅ .gitignore موجود${NC}" || echo -e "${RED}❌ .gitignore مفقود${NC}"

# 9. التحقق من روابط GitHub
echo -e "\n${YELLOW}🔗 9. التحقق من روابط GitHub:${NC}"
if grep -q "king56222" README.md; then
    echo -e "${GREEN}✅ روابط GitHub صحيحة في README.md${NC}"
else
    echo -e "${RED}❌ روابط GitHub تحتاج تحديث في README.md${NC}"
fi

# 10. التحقق من إعدادات Git
echo -e "\n${YELLOW}🔧 10. التحقق من إعدادات Git:${NC}"
echo -n "اسم المستخدم: "
git config user.name || echo -e "${RED}غير مضبوط${NC}"
echo -n "البريد الإلكتروني: "
git config user.email || echo -e "${RED}غير مضبوط${NC}"
echo -n "الـ remote: "
git remote -v | head -1 || echo -e "${RED}غير مضبوط${NC}"

# 11. التحقق من عدد السيرفرات
echo -e "\n${YELLOW}🌍 11. التحقق من السيرفرات:${NC}"
if [ -f "config/servers.json" ]; then
    COUNT=$(python3 -c "import json; print(len(json.load(open('config/servers.json')).get('servers', [])))" 2>/dev/null)
    echo -e "${GREEN}✅ $COUNT سيرفر متاح${NC}"
fi

# 12. اختبار تشغيل بسيط (اختياري)
echo -e "\n${YELLOW}🚀 12. اختبار تشغيل سريع:${NC}"
echo -e "${BLUE}لم يتم تشغيل التطبيق تلقائياً. للتشغيل:${NC}"
echo "   python3 src/main.py"

# النتائج النهائية
echo -e "\n${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}                      النتائج النهائية${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ تم اجتياز: $PASSED فحص${NC}"
echo -e "${RED}❌ لم يتم اجتياز: $FAILED فحص${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 تهانينا! المشروع جاهز للنشر على GitHub!${NC}"
    echo -e "${GREEN}📦 رابط المشروع: https://github.com/king56222/vpn-pro-galaxy-a04e${NC}"
else
    echo -e "${YELLOW}⚠️ هناك بعض المشاكل التي تحتاج إلى إصلاح${NC}"
fi
