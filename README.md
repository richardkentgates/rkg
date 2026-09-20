# richardkentgates.com

Personal website and research portfolio for Richard Kent Gates. Hosted on GitHub Pages at [richardkentgates.com](https://richardkentgates.com).

### Web Development

<img src="https://img.shields.io/badge/WordPress-21759B?logo=wordpress&logoColor=white" alt="WordPress" height="22">
<img src="https://img.shields.io/badge/Debian-A80030?logo=debian&logoColor=white" alt="Debian" height="22">
<img src="https://img.shields.io/badge/Apache-D22128?logo=apache&logoColor=white" alt="Apache" height="22">
<img src="https://img.shields.io/badge/MariaDB-003545?logo=mariadb&logoColor=white" alt="MariaDB" height="22">
<img src="https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white" alt="PHP" height="22">
<img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white" alt="HTML5" height="22">
<img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white" alt="CSS3" height="22">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript" height="22">

### Theoretical Physics

<img src="https://img.shields.io/static/v1?label=%20&labelColor=6B7280&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+PHBvbHlsaW5lIHBvaW50cz0iMCwzMiAxNiwxNiAzMiw0OCA0OCwxNiA2NCwzMiIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjYiIGZpbGw9Im5vbmUiLz48L3N2Zz4=&message=Unified+Scalar+Field+G(t)&color=4F46E5" alt="Unified Scalar Field G(t)" height="22">
<img src="https://img.shields.io/static/v1?label=%20&labelColor=6B7280&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+PGxpbmUgeDE9IjgiIHkxPSIzMiIgeDI9IjU2IiB5Mj0iMzIiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI2Ii8+PHBvbHlnb24gcG9pbnRzPSI0OCwyMCA1NiwzMiA0OCw0NCIgZmlsbD0iI0ZGRkZGRiIvPjwvc3ZnPg==&message=Entropy+Arrow&color=F97316" alt="Entropy Arrow" height="22">
<img src="https://img.shields.io/static/v1?label=%20&labelColor=6B7280&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+PGNpcmNsZSBjeD0iMjAiIGN5PSIzMiIgcj0iMTIiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI2IiBmaWxsPSJub25lIi8+PGNpcmNsZSBjeD0iNDQiIGN5PSIzMiIgcj0iMTIiIHN0cm9rZT0iI0ZGRkZGRiIgc3Ryb2tlLXdpZHRoPSI2IiBmaWxsPSJub25lIi8+PGxpbmUgeDE9IjI4IiB5MT0iMzIiIHgyPSIzNiIgeTI9IjMyIiBzdHJva2U9IiNGRkZGRkYiIHN0cm9rZS13aWR0aD0iNiIvPjwvc3ZnPg==&message=Entanglement+Formalization&color=039003" alt="Entanglement Formalization" height="22">
<img src="https://img.shields.io/static/v1?label=%20&labelColor=6B7280&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+PGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMTAiIGZpbGw9IiNGRkZGRkYiLz48Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIyMiIgc3Ryb2tlPSIjRkZGRkZGIiBzdHJva2Utd2lkdGg9IjYiIGZpbGw9Im5vbmUiLz48L3N2Zz4=&message=Black+Hole+Lifecycle&color=990900" alt="Black Hole Lifecycle" height="22">

## Architecture

Static site. No build step, no framework, no dependencies. Just `index.html` and `style.css`.

- `index.html` — the complete page, served by GitHub Pages
- `style.css` — external stylesheet (linked via `https://richardkentgates.com/style.css`)
- `CNAME` — custom domain: `richardkentgates.com`
- `.nojekyll` — disables Jekyll processing

### Directory layout

```
rkg/
├── index.html              # The site
├── style.css               # Stylesheet
├── CNAME                   # Custom domain
├── .nojekyll               # Disable Jekyll
├── license.txt             # CC BY 4.0 for research materials
├── images/                 # Logo and avatar assets
│   ├── rkg_logo_640x640.jpg
│   ├── rkg_logo_300x300.jpg
│   ├── rkg_logo_64x64_fav.png
│   ├── rkg_logo_64x64.jpg
│   ├── rkg_logo_github_493_270.jpg
│   ├── rkg_logo_translucent_493_270.png
│   └── rkg-avitar.png      # Header avatar (background-image via CSS)
├── papers/                 # Physics research (HTML, PDF, TeX, Python, results)
└── .github/workflows/
    └── convert-papers.yml  # Auto-converts HTML papers to PDF and TeX
```

## Papers

The `papers/` directory contains the Unified Scalar Time-Gradient Field Theory research:

| Paper | Description |
|---|---|
| theory-of-everything | Capstone: one axiom, one field, all of physics |
| foundation-proof | Distance → time → information → singularities forbidden |
| unified-proof | The field IS the universe; no beginning, no singularity |
| blackhole-lifecycle | BH mass evolution, relics as dark matter, rotation curves |
| entanglement-formalization | Entanglement, frame dragging, GWs in the G(t) framework |
| time-gradient-field-model | Decay-rate and lifetime anomalies |
| temporal-gradient-gravity-proposal | Gravity as a pure temporal gradient |
| time-gradient-verification | Independent verification from experimental data |
| statistical-verification | Fisher Information and Cramer-Rao closure |
| unified-scalar-field-consistency | Cross-sector unification proof |
| unified-scalar-time-gradient-field | Complete formalized synthesis |
| renormalization-proof | Why G(t) needs no fine-tuning |

Each paper has three formats:
- `.html` — source (authored directly, renders with MathJax)
- `.pdf` — generated by CI via headless Chrome
- `.tex` — generated by CI via pandoc

### Interactive calculators

- `calc-field-visualizer.html` — G(t) scalar field with interactive sliders
- `calc-forward-prediction.html` — Unified correction law predictions
- `calc-fisher-information.html` — Multi-channel Fisher Information reconstruction

### Computation source and results

Python scripts (NumPy only, no external dependencies) and their tab-separated output:

| Script | Results |
|---|---|
| `scalar_field_tests.py` | `forward_results.txt`, `backward_results.txt`, `fisher_results.txt` |
| `signal_processing_proof.py` | `signal_processing_proof.txt` |
| `foundation_proof.py` | `foundation_proof_results.txt` |
| `unified_proof.py` | `unified_proof_results.txt` |
| `theory_of_everything.py` | `theory_of_everything_results.txt` |
| `blackhole_lifecycle.py` | `blackhole_lifecycle_results.txt` |
| `renormalization_proof.py` | `renormalization_proof_results.txt` |
| `entanglement_formalization.py` | `entanglement_formalization_results.txt` |

## CI/CD

### Paper conversion (`convert-papers.yml`)

Triggers on push to `master` when `papers/*.html` or `papers/fig-*` change (or manually via workflow_dispatch).

1. Converts each HTML paper to PDF using headless Chrome (`--print-to-pdf`)
2. Converts each HTML paper to TeX using pandoc
3. Commits the generated `.pdf` and `.tex` files back to the repo

## Physics badge SVGs

The four theoretical physics badges use custom inline SVG logos encoded as base64 data URIs via the `shields.io/static/v1` endpoint. Each badge has a distinct icon and color:

| Badge | Icon | Color |
|---|---|---|
| Unified Scalar Field G(t) | Sine wave (polyline) | `#4F46E5` (indigo) |
| Entropy Arrow | Right arrow (line + polygon) | `#F97316` (orange) |
| Entanglement Formalization | Two linked circles | `#039003` (green) |
| Black Hole Lifecycle | Dot-in-circle (filled circle + stroked ring) | `#990900` (dark red) |

All badges share `labelColor=6B7280` (gray) for the left label panel.

## Structured data

`index.html` includes JSON-LD schema.org markup:
- `Person` — author identity and contact
- `WebSite` — site metadata
- `ScholarlyArticle` — one entry per paper (10 total)
- `SoftwareSourceCode` — one entry per open source project (6 total)

## Design

- Fonts: Inter (sans-serif) + JetBrains Mono (monospace)
- Color: dark header (#0f1623), blue accent (#2d8cf0), light background (#f8fafc)
- Layout: CSS Grid with sticky sidebar, responsive breakpoints at 860px and 540px
- Components: project cards, collapse toggles, hero section with badge pills
- Header avatar: `rkg-avitar.png` via CSS `background-image` on `h1.rkg`

## License

- Site design and code: Copyright Richard Kent Gates
- Research materials (theoretical framework, equations, manuscripts, diagrams): [CC BY 4.0](license.txt)
- Open source projects: see individual repositories
