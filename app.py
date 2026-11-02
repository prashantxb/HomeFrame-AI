
import streamlit as st
import os
import textwrap
import numpy as np
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, concatenate_videoclips, AudioFileClip, vfx
import tempfile


# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="HomeFrame AI | Luxury Property Studio",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==================================================
# 2. LUXURY CUSTOM CSS
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 85% 5%, #263B32 0%, transparent 35%),
        linear-gradient(135deg, #111815, #0B0E0C 65%);
    color: #F4EFE4;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1180px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Main typography */

h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, serif !important;
}

h1 {
    color: #E0C58F !important;
    font-size: 3.1rem !important;
}

h2, h3 {
    color: #DCC18C !important;
}

p, label {
    color: #EEE9DF !important;
}

/* Hero banner */

.hero {
    background: linear-gradient(120deg, #23362C, #111A15);
    border: 1px solid #A98B56;
    border-radius: 22px;
    padding: 48px 30px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 15px 40px #00000055;
}

.hero-tag {
    color: #D5B77D;
    letter-spacing: 5px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
}

.hero-title {
    font-family: 'Playfair Display', Georgia, serif;
    color: #E5CA91;
    font-size: 48px;
    font-weight: 700;
    margin: 15px 0;
}

.hero-subtitle {
    color: #F1EBDD;
    font-size: 18px;
    letter-spacing: 1px;
}

.hero-description {
    color: #BDBBAF;
    font-size: 14px;
}

/* Feature cards */

.feature-card {
    background: linear-gradient(145deg, #26352D, #171F1A);
    border: 1px solid #766440;
    border-radius: 15px;
    padding: 22px;
    text-align: center;
    min-height: 110px;
    box-shadow: 0 5px 18px #00000035;
}

.feature-icon {
    font-size: 27px;
}

.feature-number {
    color: #E0C58F;
    font-size: 23px;
    font-weight: 700;
    margin-top: 5px;
}

.feature-label {
    color: #C6C1B5;
    font-size: 12px;
}

/* Section cards */

.section-card {
    background: linear-gradient(145deg, #1D2922, #141B17);
    border: 1px solid #65583D;
    border-radius: 17px;
    padding: 24px;
    margin-top: 18px;
    margin-bottom: 18px;
}

/* Input fields */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: #202923;
    color: #F5F0E6;
    border: 1px solid #776544;
    border-radius: 10px;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #DCC18C;
    box-shadow: 0 0 10px #DCC18C30;
}

/* Buttons */

.stButton > button {
    background: linear-gradient(110deg, #927344, #E2C58B, #B18B50);
    color: #111411;
    border: 1px solid #E2C58B;
    border-radius: 12px;
    min-height: 52px;
    font-weight: 700;
    font-size: 16px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: #F0D9A6;
    color: #111411;
    box-shadow: 0 0 18px #D9BD8355;
    transform: translateY(-2px);
}

/* File uploader */

[data-testid="stFileUploader"] {
    background: #1D2821;
    border: 1px dashed #C5A66A;
    border-radius: 15px;
    padding: 18px;
}

/* Metrics */

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #26352D, #171F1A);
    border: 1px solid #806B43;
    padding: 17px;
    border-radius: 14px;
}

[data-testid="stMetricValue"] {
    color: #E2C58B;
}

/* Divider */

hr {
    border-color: #806B43;
    opacity: 0.6;
}

/* Alerts */

[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Footer */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# 3. HERO HEADER
# ==================================================


# ==================================================
# 3. HERO HEADER
# ==================================================

st.html("""
<div style="
    background: linear-gradient(120deg,#23362C,#111A15);
    border: 1px solid #B89A62;
    border-radius: 22px;
    padding: 48px 25px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 15px 40px #00000055;
">

    <div style="
        color:#D5B77D;
        letter-spacing:5px;
        font-size:12px;
        font-weight:bold;
    ">
        LUXURY REAL ESTATE VIDEO STUDIO
    </div>

    <h1 style="
        color:#E5CA91;
        font-family:Georgia,serif;
        font-size:48px;
        margin:20px 0;
    ">
        🏡 HomeFrame AI
    </h1>

    <p style="
        color:#F1EBDD;
        font-size:19px;
    ">
        Turn Property Photos into Cinematic Stories
    </p>

    <p style="
        color:#BDBBAF;
        font-size:14px;
    ">
        Your Property. Your Vision. Our Creation.
    </p>

</div>
""")



# ==================================================
# 4. FEATURE CARDS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📸</div>
        <div class="feature-number">4–8</div>
        <div class="feature-label">PROPERTY PHOTOS</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎬</div>
        <div class="feature-number">HD</div>
        <div class="feature-label">VIDEO EXPORT</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">✨</div>
        <div class="feature-number">Easy</div>
        <div class="feature-label">VIDEO CREATION</div>
    </div>
    """, unsafe_allow_html=True)


st.write("")
st.divider()


# ==================================================
# 5. PROPERTY DETAILS
# ==================================================

st.header("🏠 Property Details")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Property Name",
        placeholder="e.g. Royal Green Villas"
    )

    location = st.text_input(
        "Location",
        placeholder="e.g. Chandigarh"
    )

    price = st.text_input(
        "Property Price",
        placeholder="e.g. ₹75 Lakh"
    )

with col2:

    property_type = st.selectbox(
        "Property Type",
        [
            "Apartment",
            "Villa",
            "Luxury House",
            "Plot",
            "Penthouse"
        ]
    )

    contact = st.text_input(
        "Contact / Call to Action",
        value="Contact us for a private site visit"
    )

features = st.text_area(
    "Key Property Features",
    placeholder="Swimming pool, garden, parking, modular kitchen, balcony...",
    height=110
)


st.divider()


# ==================================================
# 6. PROPERTY PHOTO GALLERY
# ==================================================

st.header("📸 Property Photo Studio")

st.caption(
    "Upload 4–8 high-quality property photographs."
)

images = st.file_uploader(
    "Choose your property images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if images:

    st.write(f"**{len(images)} photos uploaded**")

    preview_cols = st.columns(min(len(images), 4))

    for i, uploaded_file in enumerate(images):

        with preview_cols[i % len(preview_cols)]:

            st.image(
                uploaded_file.getvalue(),
                caption=f"Property Photo {i + 1}",
                use_container_width=True
            )


st.divider()


# ==================================================
# 7. VIDEO SETTINGS
# ==================================================

st.header("🎞️ Video Studio")

st.write("")

st.markdown("### ✨ Your Video Preferences")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📱 Instagram Reels\n\nVertical 9:16")

with col2:
    st.info("🖥️ YouTube & Websites\n\nLandscape 16:9")

with col3:
    st.info("🎨 Luxury Themes\n\nGold • Dark • White")


col1, col2 = st.columns(2)

with col1:

    video_format = st.selectbox(
        "Video Format",
        [
            "Landscape (16:9)",
            "Instagram Reel (9:16)"
        ]
    )

with col2:

    video_theme = st.selectbox(
        "Video Theme",
        [
            "Luxury Gold",
            "Elegant Dark",
            "Classic White"
        ]
    )

st.caption(
    "Choose your preferred video format and visual theme."
)

# Professional video enhancements
st.subheader("🎵 Music, Transitions & Branding")

music_file = st.file_uploader(
    "Upload background music (optional: MP3, WAV, M4A)",
    type=["mp3", "wav", "m4a"],
    key="background_music"
)

col_a, col_b = st.columns(2)
with col_a:
    transition_duration = st.slider(
        "Photo transition duration (seconds)",
        min_value=0.2,
        max_value=1.0,
        value=0.5,
        step=0.1
    )

with col_b:
    show_watermark = st.checkbox("Show HomeFrame AI watermark", value=True)

watermark_text = st.text_input(
    "Watermark text",
    value="HOMEFRAME AI",
    disabled=not show_watermark
)

st.caption(
    "Add your own licensed music file. The watermark is placed on every scene."
)

st.divider()


# ==================================================
# 8. VIDEO GENERATION
# ==================================================

st.header("✨ Create Your Property Video")

if st.button(
    "🎬 Generate Luxury Property Video",
    use_container_width=True
):

    # Validate input

    if not name.strip() or not location.strip() or not price.strip():

        st.error(
            "Please enter property name, location and price."
        )

    elif not features.strip() or not contact.strip():

        st.error(
            "Please enter property features and contact details."
        )

    elif not images or not 4 <= len(images) <= 8:

        st.error(
            "Please upload between 4 and 8 property images."
        )

    else:

        # Generate promotional script

        script = (
            f"Welcome to {name}, located in {location}. "
            f"This beautiful {property_type.lower()} "
            f"is available at {price}. "
            f"Enjoy premium features including {features}. "
            f"{contact}."
        )

        captions = [
            f"Welcome to {name}",
            f"Discover {location}",
            f"{property_type} | {price}",
            f"Features: {features}",
            contact
        ]

        st.success(
            "Property details successfully validated!"
        )

        # Show script

        st.subheader("📝 Promotional Script")

        st.info(script)

        # Show captions

        st.subheader("🎞️ Scene Captions")

        for i, caption in enumerate(captions, start=1):

            st.write(f"**Scene {i}:** {caption}")

        # Video settings

        if video_format == "Instagram Reel (9:16)":
            width, height = 720, 1280
        else:
            width, height = 1280, 720

        # Select theme colors

        themes = {
            "Luxury Gold": (20, 27, 23),
            "Elegant Dark": (15, 20, 25),
            "Classic White": (238, 234, 222)
        }

        bg_color = themes[video_theme]

        text_color = (
            (255, 255, 255)
            if video_theme != "Classic White"
            else (35, 35, 35)
        )

        os.makedirs("output", exist_ok=True)

        clips = []
        final_video = None

        try:

            with st.spinner(
                "Creating your luxury property video... Please wait."
            ):

                for i, uploaded_file in enumerate(images):

                    # Open image safely

                    photo = Image.open(
                        BytesIO(uploaded_file.getvalue())
                    ).convert("RGB")

                    # Resize and crop to selected format

                    ratio = max(
                        width / photo.width,
                        height / photo.height
                    )

                    new_size = (
                        int(photo.width * ratio),
                        int(photo.height * ratio)
                    )

                    photo = photo.resize(
                        new_size,
                        Image.Resampling.LANCZOS
                    )

                    left = (photo.width - width) // 2
                    top = (photo.height - height) // 2

                    photo = photo.crop((
                        left,
                        top,
                        left + width,
                        top + height
                    ))

                    # Add HomeFrame AI watermark
                    if show_watermark and watermark_text.strip():
                        watermark_draw = ImageDraw.Draw(photo)
                        try:
                            watermark_font = ImageFont.truetype(
                                "C:/Windows/Fonts/arial.ttf",
                                22 if height > width else 26
                            )
                        except OSError:
                            watermark_font = ImageFont.load_default()

                        watermark_label = watermark_text.strip()
                        watermark_box = watermark_draw.textbbox(
                            (0, 0), watermark_label, font=watermark_font
                        )
                        watermark_width = watermark_box[2] - watermark_box[0]
                        watermark_x = width - watermark_width - 35
                        watermark_y = 30

                        watermark_draw.rounded_rectangle(
                            (
                                watermark_x - 12,
                                watermark_y - 8,
                                width - 18,
                                watermark_y + 34
                            ),
                            radius=10,
                            fill=(18, 27, 22)
                        )
                        watermark_draw.text(
                            (watermark_x, watermark_y),
                            watermark_label,
                            fill=(224, 197, 143),
                            font=watermark_font
                        )

                    # Add caption background

                    draw = ImageDraw.Draw(photo)

                    banner_height = min(
                        190 if height > width else 150,
                        height // 3
                    )

                    draw.rectangle(
                        (
                            0,
                            height - banner_height,
                            width,
                            height
                        ),
                        fill=bg_color
                    )

                    # Caption selection

                    caption = captions[
                        min(i, len(captions) - 1)
                    ]

                    # Load font

                    try:

                        font_size = (
                            38 if height > width else 34
                        )

                        font = ImageFont.truetype(
                            "C:/Windows/Fonts/arial.ttf",
                            font_size
                        )

                    except OSError:

                        font = ImageFont.load_default()

                    # Add decorative gold line

                    draw.rectangle(
                        (
                            35,
                            height - banner_height + 15,
                            width - 35,
                            height - banner_height + 19
                        ),
                        fill=(204, 172, 112)
                    )

                    # Draw caption

                    lines = textwrap.wrap(
                        caption,
                        width=24 if height > width else 45
                    )

                    y = height - banner_height + 35

                    for line in lines[:3]:

                        draw.text(
                            (40, y),
                            line,
                            fill=text_color,
                            font=font
                        )

                        y += font_size + 10

                    # Convert image into video clip

                    clip = ImageClip(
                        np.array(photo)
                    ).with_duration(3)

                    # Fade each incoming scene for a smooth crossfade
                    if i > 0 and transition_duration > 0:
                        clip = clip.with_effects([
                            vfx.CrossFadeIn(transition_duration)
                        ])

                    clips.append(clip)

                # Join scenes with a small overlap for crossfade transitions
                overlap = min(transition_duration, 0.9)
                final_video = concatenate_videoclips(
                    clips,
                    method="compose",
                    padding=-overlap if len(clips) > 1 else 0
                )

                # Add uploaded background music, trimmed/looped to video length
                if music_file is not None:
                    suffix = os.path.splitext(music_file.name)[1] or ".mp3"
                    with tempfile.NamedTemporaryFile(
                        delete=False, suffix=suffix
                    ) as temp_music:
                        temp_music.write(music_file.getvalue())
                        music_temp_path = temp_music.name

                    audio_clip = AudioFileClip(music_temp_path)

                    if audio_clip.duration < final_video.duration:
                        from moviepy import concatenate_audioclips
                        repeats = int(final_video.duration // audio_clip.duration) + 1
                        audio_clip = concatenate_audioclips(
                            [audio_clip] * repeats
                        )

                    audio_clip = audio_clip.subclipped(
                        0, final_video.duration
                    ).with_volume_scaled(0.18)

                    final_video = final_video.with_audio(audio_clip)

                # Set output path

                video_path = os.path.abspath(
                    "output/HomeFrame_AI_Video.mp4"
                )

                # Export MP4

                final_video.write_videofile(
                    video_path,
                    fps=24,
                    codec="libx264",
                    audio=music_file is not None,
                    logger=None
                )

            # Success

            st.success(
                "🎉 Your HomeFrame AI property video is ready!"
            )

            st.subheader("🎬 Final Video Preview")

            st.video(video_path)

            # Download

            with open(video_path, "rb") as video_file:

                st.download_button(
                    label="⬇️ Download HomeFrame AI Video",
                    data=video_file.read(),
                    file_name="HomeFrame_AI_Video.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )

        except Exception as e:

            st.error(
                f"Video generation failed: {e}"
            )

        finally:

            if final_video is not None:
                final_video.close()

            if audio_clip is not None:
                audio_clip.close()

            for clip in clips:
                clip.close()

            if music_temp_path and os.path.exists(music_temp_path):
                os.remove(music_temp_path)


# ==================================================
# 9. FOOTER
# ==================================================

st.divider()

st.markdown(
    "<h3 style='text-align:center; color:#D9BD83;'>"
    "🏡 HomeFrame AI"
    "</h3>",
    unsafe_allow_html=True
)

st.caption(
    "LUXURY REAL ESTATE VIDEO STUDIO"
)

st.caption(
    "Your Property. Your Vision. Our Creation."
)