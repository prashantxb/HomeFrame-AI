# HomeFrame AI – Luxury Property Video Generator

## 1. Project Overview

HomeFrame AI is a Python-based web application that automatically creates promotional real estate videos using property details and uploaded images.

It helps real estate agents create attractive property marketing videos without manually editing photos in a video editor.

## 2. Features

- Enter property name, location, price and property type.
- Add property features and contact information.
- Upload 4–8 property images.
- Automatically generate promotional scripts using Python templates.
- Generate captions for video scenes.
- Add readable text overlays to property images.
- Combine images into an MP4 video.
- Add cinematic crossfade transitions between scenes.
- Upload background music (MP3, WAV or M4A).
- Add a customizable HomeFrame AI watermark.
- Choose Landscape (16:9) or Instagram Reel (9:16) format.
- Select different luxury video themes.
- Preview and download the generated video.
- Validate inputs and display useful error messages.

## 3. Technologies Used

- Python
- Streamlit
- MoviePy
- Pillow (PIL)
- NumPy

**AI Approach:** This version uses rule-based Python templates to generate promotional scripts and captions. No external AI API or trained machine-learning model is currently used.

## 4. Project Structure

```text
HomeFrame AI/
├── .venv/
├── demo_video/
│   └── Sample_Property_Video.mp4
├── output/
├── app.py
├── README.md
└── requirements.txt
```

The `output` folder is created automatically when the application generates a video.

## 5. Installation Requirements

- Python
- Visual Studio Code (recommended)

Open the project folder in VS Code.

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## 6. How to Run the Application

Open the terminal in the project folder and run:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

Enter property details, upload 4–8 images, choose video settings and click **Generate Luxury Property Video**.

The application generates a promotional script, captions and an MP4 video.

## 7. Sample Input

- Property Name: Royal Palace Villa
- Location: Chandigarh
- Price: ₹1.5 Crore
- Property Type: Villa
- Features: Swimming pool, garden, modular kitchen and parking
- Contact Message: Book Your Private Visit Today
- Images: Four to eight sample property images

Synthetic property details and sample images can be used for testing.

## 8. Expected Output

The application generates:

- A promotional property script.
- Scene captions.
- A promotional MP4 video.
- Text overlays and HomeFrame AI watermark.
- Cinematic transitions.
- Optional background music.

The generated video is saved as:

`output/HomeFrame_AI_Video.mp4`

Each property image is displayed for approximately three seconds before transitions are applied.

## 9. Error Handling

The application checks that:

- Property name, location and price are provided.
- Property features and contact information are provided.
- Between four and eight images are uploaded.

It displays an error message when required information is missing or invalid.

## 10. Limitations

- Promotional scripts use predefined Python templates rather than an external generative AI model.
- The video uses static property images with text overlays.
- Background music must be uploaded by the user.
- Video quality depends on the uploaded images and supplied information.

## 11. Future Improvements

- Integrate a generative AI API for more flexible promotional scripts.
- Add text-to-speech narration.
- Add more video themes and customization options.
- Provide additional social media export formats.

## 12. Conclusion

HomeFrame AI demonstrates how Python and multimedia libraries can automate the creation of real estate promotional videos.

It combines property information, uploaded images, captions, transitions, optional background music and branding into a downloadable MP4 video, reducing the manual effort required to create property marketing content.

## 13. Libraries and External Services

- Python: Application programming language.
- Streamlit: Web application interface.
- MoviePy: Video creation and editing.
- Pillow: Image processing and text overlays.
- NumPy: Image array processing.

No external AI API or trained machine-learning model is used in this version.
