# Dimple Shukla - ATS-Optimized CV

This repository contains an ATS-optimized, recruiter-ready CV tailored for the **Amazon Lead Client Portal Mobile Engineer** position.

## 📋 Structure

- **cv.json** — Single source of truth for CV data (optimized for ATS parsing)
- **Dimple_Shukla_CV.pdf** — Generated recruiter-ready PDF (auto-updated on commits)
- **scripts/generate_cv_pdf.py** — Python script that generates PDF from JSON
- **.github/workflows/export-cv.yml** — GitHub Actions workflow for auto-export

## 🎯 ATS Optimization Strategy

### 1. **Keyword Alignment** ✅
- **Flutter/Dart internals**: Widget lifecycle, performance profiling, DevTools
- **Real-time systems**: WebSockets, low-latency design, stream processing
- **Advanced state management**: BLoC, Provider, Clean Architecture
- **Testing**: Unit, widget, integration, automation testing
- **API Integration**: REST, Protobuf, gRPC, OAuth2, JWT
- **AI-assisted development**: LLM code generation, prompt engineering, hallucination mitigation

### 2. **Structure for ATS Parsing** ✅
- Clear section headers (PROFESSIONAL SUMMARY, PROFESSIONAL EXPERIENCE, TECHNICAL SKILLS, EDUCATION)
- Consistent date formatting (MMM YYYY format)
- Bullet-point highlights (scanned for keywords)
- Full keyword expansion in skills section
- No tables, images, or complex formatting

### 3. **Quantified Impact** ✅
Each role includes:
- **Performance metrics**: Latency improvements, crash rate reductions, uptime percentages
- **Scale indicators**: User counts, transaction volumes, concurrent connections
- **Leadership evidence**: Team mentoring, delivery acceleration, process improvements
- **Technical depth**: Architecture decisions, technology choices, integration complexity

## 🚀 Setup & Usage

### Initial Setup
```bash
# Clone repository
git clone https://github.com/yourusername/dim-cv.git
cd dim-cv

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install reportlab
```

### Generate PDF Locally
```bash
python3 scripts/generate_cv_pdf.py
```

### Auto-Generate via GitHub
1. Push changes to `cv.json`
2. GitHub Actions automatically:
   - Installs dependencies
   - Generates PDF
   - Commits PDF back to repo
   - Creates release artifacts

## 📊 Amazon Role Alignment

| Requirement | Coverage |
|------------|----------|
| 8+ years engineering | 6+ years Flutter/mobile (since 2018) |
| 3+ years Flutter/Dart | ✅ Across 4 companies (2018-present) |
| Widget lifecycle mastery | ✅ Performance profiling & DevTools expertise |
| BLoC/state management | ✅ Complex financial apps, real-time trading |
| Real-time systems | ✅ Trading platforms (5K+ orders/sec), market feeds |
| Protobuf/gRPC | ✅ Listed in skills with examples |
| Testing practices | ✅ Unit, widget, integration, 85% coverage |
| AI-assisted dev | ✅ LLM code generation, prompt engineering |
| Low-latency optimization | ✅ <100ms latency for trading, 25% improvements |
| Communication skills | ✅ Tech lead, mentoring, documentation |

## 🎨 Customization

### Update CV Data
Edit `cv.json`:
```json
{
  "basics": {
    "name": "Your Name",
    "label": "Your Title",
    "summary": "Your professional summary..."
  },
  "work": [ ... ],
  "skills": [ ... ],
  "education": [ ... ]
}
```

Then run:
```bash
python3 scripts/generate_cv_pdf.py
```

## 🔍 ATS Scanning Tips

### What ATS Looks For:
1. **Exact keyword matches** → Skills are keyword-rich
2. **Chronological work history** → Dates clearly formatted
3. **Quantified achievements** → Metrics included (latency, uptime, user counts)
4. **Technical specificity** → Framework/tool names, library versions
5. **Consistent formatting** → No special characters, tables, or images

### What to Avoid:
- ❌ Images, tables, columns (not ATS-readable)
- ❌ Uncommon fonts or colors
- ❌ Headers/footers with contact info repeated
- ❌ Abbreviations without expansion (define acronyms first)
- ❌ Vague descriptions ("worked on project") without impact

## 📈 Performance Metrics

- **PDF Size**: ~6KB (ultra-lightweight for email)
- **Pages**: 1-2 (concise, scannable)
- **ATS Score**: Estimated 95%+ (all required keywords included)
- **Recruiter Scanability**: High (clear sections, quantified metrics)

## 🔗 Quick Links

- **PDF Download**: [Dimple_Shukla_CV.pdf](./Dimple_Shukla_CV.pdf)
- **LinkedIn**: https://linkedin.com/in/dmple/
- **Target Role**: Amazon Lead Client Portal Mobile Engineer

## ✨ Key Differentiators for Amazon

1. **Real-time system expertise** — Trading platforms with <100ms latency
2. **Performance obsession** — 35% latency reduction, 60fps stability focus
3. **Financial domain knowledge** — 3 fintech companies (mutual funds, trading, wealth management)
4. **Leadership at scale** — Team mentoring, architecture decisions, velocity improvements
5. **AI-native development** — Active LLM integration, prompt engineering, code generation

---

**Last Updated**: March 30, 2026
**Status**: ATS-Optimized, Recruiter-Ready ✅
