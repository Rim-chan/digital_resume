from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Rim_Sleimi_CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"




# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Rim Sleimi"
PAGE_ICON = ":wave:"
NAME = "Rim Sleimi"
DESCRIPTION = """
Earth Observation & Machine Learning Engineer.
"""
EMAIL = "rim.sleimi@etudiant-fst.utm.tn"


SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rim-sleimi/",
    "GitHub": "https://github.com/Rim-chan",
}


PROJECTS = {
    "🏆 Buildings Detection - Using Deep Learning to detect buildings from the curated SpaceNet7 dataset.": "https://github.com/Rim-chan/SpaceNet7-Buildings-Detection",
    "🏆 GI Tract Segmentation - Track healthy organs in medical scans to improve cancer treatment.": "https://github.com/Rim-chan/GI-Tract-Image-Segmentation",
    "🏆 Cloud Segmentation - Using Deep Learning to detect clouds from the curated 95-Cloud dataset dataset.": "https://github.com/Rim-chan/Cloud-Segmentation-Using-DL",
    "🏆 Analysis of movie data - Predicting the gender of the lead actor in a Hollywood film": "https://github.com/Rim-chan/Do-wo-men-talk-too-much-in-films-",
}






st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---

st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from remote sensing data using machine learning
- ✔️ Good hands on experience and knowledge in Python and JavaScript
- ✔️ Experience working with geospatial data and tools (Google Earth Engine, ArcGIS and QGIS)
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Good analytical and problem-solving skills
- ✔️ Good communication and teamwork skills
"""
) 



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, JavaScript (Google Earth Engine), MATLAB, SQL
- 📊 AI: Machine Learning (scikit-learn), Deep Learning (Pytorch)
- 🗄️ MLOps: FastAPI, Docker, streamlit, MLflow
- 📚 Software: ArcGIS, QGIS, Microsoft Office, Latex, SNAP
- Other: Git, Github, VSCode
"""
)

# --- MOST PROUD OF---
st.write('\n')
st.subheader("Most Proud Of")
st.write(
    """
- 🏆 Ranked the first on a national level in the admission to engineering school’s exams, and I was awarded by the minister of agriculture.
- 🏆 I was granted an Erasmus ICM scholarship to study at Uppsala University-Sweden for one year.

"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Remote Sensing and GIS Junior Expert | Sahara and Sahel Observatory (OSS)**")
st.write("09/2022 - Present")
st.write(
    """
Used GEE for:
- ► Developing GUIs for vegetation gain and loss, generating labels for LULC, and reclassifying unsupervised LULC maps.
- ► SDG 15.3.1 reporting based on the UNCCD good practice guidance-V2 for all African countries;
- ► Phenology-based land cover classification;
- ► Forest fire assessment;
"""
)


# --- JOB 2
st.write('\n')
st.write("🚧", "**Machine Learning & Remote Sensing Research Intern| International Water Management Institute (IWMI)**")
st.write("02/2022 - 12/2022")
st.write(
    """
- ► Conducted literature review regarding drought and Flood monitoring.
- ► Developed a scalable method for drought monitoring using satellite remote sensing Data and PCA.
- ► Developed a pipeline to create an off-the-shelf model for timely flood mapping using open-source labeled Sentinel-1 data.
- ► Developed a web app that enables the end users to query Sentinel-1 data and generate flood masks.
"""
)


# --- JOB 3
st.write('\n')
st.write("🚧", "**Remote Sensing & Machine Learning intern | Sahara and Sahel Observatory (OSS)**")
st.write("03/2020 - 11/2020")
st.write(
    """
    Graduation thesis: Remote Sensing Approach for Water Balance Establishment in Irrigated Areas
- ► Processed Sentinel 2 L2A and Landsat 8 remote sensing imagery.
- ► Conducted a comparative analysis of a multitude of classification models and Sentinel-2 band combinations/indices for crop type identification in Bizerte.
- ► Estimated evapotranspiration using the FAO-56 method and the SEBAL model.
"""
)


# --- JOB 4
st.write('\n')
st.write("🚧", "**GIS & Remote Sensing intern | Sahara and Sahel Observatory (OSS)**")
st.write("07/2019 - 08/2019")
st.write(
    """
    Mapping and Inventory of protected areas:
- ► Developed maps of protected areas, as well as maps of protected areas and land use, in 28 African countries, according to the IUCN categories using ArcGIS and elaborating.
- ► Writing reports.

"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

