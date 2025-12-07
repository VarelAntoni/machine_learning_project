import pandas as pd

def load_job_dataset(csv_path):
    """Memuat satu dataset pekerjaan dari file CSV."""
    try:
        df = pd.read_csv(csv_path)
        print(f"✅ Dataset berhasil dimuat dari {csv_path}: {len(df)} baris")
        return df
    except Exception as e:
        print(f"❌ Gagal memuat dataset {csv_path}: {e}")
        return None

def search_job_info(question, df):
    """Cari informasi pekerjaan dari satu CSV menggunakan keyword match sederhana."""
    if df is None or df.empty:
        return None

    question_lower = question.lower()
    required_cols = ["Job Title", "Experience Level", "Location", "Key Technologies", "Job Description"]
    if not all(col in df.columns for col in required_cols):
        return None

    df['job_title_lower'] = df['Job Title'].str.lower()
    matches = df[df['job_title_lower'].apply(lambda title: title in question_lower or question_lower in title)]

    if matches.empty:
        words = question_lower.split()
        matches = df[df.apply(lambda row: any(word in str(row).lower() for word in words), axis=1)]

    if matches.empty:
        return None

    base_info = []
    for _, row in matches.head(3).iterrows():
        base_info.append(
            f"- {row['Job Title']} ({row['Experience Level']}), lokasi {row['Location']}, "
            f"teknologi: {row['Key Technologies']}. "
            f"Deskripsi: {row['Job Description']}"
        )

    return "\n".join(base_info)

def search_job_info_from_multiple_datasets(question, dataframes):
    """Gabungkan pencarian dari beberapa dataset CSV."""
    all_context = []
    for df in dataframes:
        context = search_job_info(question, df)
        if context:
            all_context.append(context)

    return "\n\n".join(all_context) if all_context else "Tidak ditemukan informasi dari dataset manapun."
