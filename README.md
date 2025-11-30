# Morphin': Morphology Fixin'

**Morphin'** (atau _Morphin_) adalah bagian dari _final project_ mata kuliah Pemrosesan Bahasa Alami (Natural Language Processing; NLP) kelas B sebagai bagian untuk mengembangkan Grammarly untuk versi bahasa Indonesia. Proyek ini dikembangkan oleh kelompok **Never Like Programming (NLP)** dengan fokus masalah **perbaikan morfologi** yang mencakup:

* Kesalahan penggunaan imbuhan (awalan, akhiran, sisipan, konfiks)
* Kesalahan penulisan kata depan (di-, ke-, dari)
* Kesalahan bentukan kata dengan konfiks
* Kesalahan reduplikasi kata

Contoh: "mengdapatkan" → "mendapatkan", "didalam" → "di dalam", "mempertanggung jawabkan" → "mempertanggungjawabkan"

## Tentang Fail
Struktur folder Morphin adalah sebagai berikut

```
Morphin/
├── morphin/
│   ├── imbuhan.py
│   └── reduplikasi.py
├── Notebook Sketches/
│   ├── PyMuPDF_learning
│   ├── morphin'_morphology_fixin'.ipynb
│   └── sketch_imbuhan.ipynb
└── testing.py
```

Fail `imbuhan.py` merupakan fungsi dari perbaikan morfologi yang berisi fungsi-fungsi untuk memperbaiki awalan, akhiran, sisipan, dan konfiks. Lalu, `reduplikasi.py` adalah fail yang menampung fungsi untuk memperbaiki duplikasi kata. Fungsi-fungsi tersebut diuji di fail `testing.py`.