import streamlit as st
    if menu == "Video Cutter":
        st.header("✂ Video Cutter")

        start = st.number_input("Start Time (sec)", min_value=0)
        end = st.number_input("End Time (sec)", min_value=1)

        if st.button("Cut Video"):
            output = os.path.join(OUTPUT_DIR, "cut_video.mp4")
            cut_video(input_path, start, end, output)

            st.success("Video Cut Successfully")
            st.video(output)

            with open(output, "rb") as file:
                st.download_button("Download", file, file_name="cut_video.mp4")

    # GIF CONVERTER
    elif menu == "GIF Converter":
        st.header("🎞 Video to GIF")

        duration = st.slider("GIF Duration", 1, 15, 5)
        fps = st.slider("FPS", 5, 30, 10)

        if st.button("Convert to GIF"):
            output = os.path.join(OUTPUT_DIR, "output.gif")
            video_to_gif(input_path, output, duration, fps)

            st.image(output)

            with open(output, "rb") as file:
                st.download_button("Download GIF", file, file_name="output.gif")

    # FRAME EXTRACTOR
    elif menu == "Frame Extractor":
        st.header("🖼 Frame Extractor")

        interval = st.slider("Extract Every N Frames", 10, 100, 30)

        if st.button("Extract Frames"):
            extract_frames(input_path, interval)
            st.success("Frames Extracted")

    # FORMAT CONVERTER
    elif menu == "Format Converter":
        st.header("🔄 Format Converter")

        format_choice = st.selectbox("Convert To", ["mp4", "avi", "mov"])

        if st.button("Convert Format"):
            output = os.path.join(OUTPUT_DIR, f"converted.{format_choice}")
            convert_format(input_path, output)

            st.success("Conversion Completed")

            with open(output, "rb") as file:
                st.download_button("Download Converted Video", file)

    # SPEED CONTROLLER
    elif menu == "Speed Controller":
        st.header("⚡ Video Speed Controller")

        factor = st.slider("Speed Factor", 0.25, 4.0, 1.0)

        if st.button("Apply Speed"):
            output = os.path.join(OUTPUT_DIR, "speed_output.mp4")
            change_speed(input_path, factor, output)

            st.video(output)

            with open(output, "rb") as file:
                st.download_button("Download", file)

    # METADATA VIEWER
    elif menu == "Metadata Viewer":
        st.header("📄 Video Metadata")

        metadata = get_metadata(input_path)

        st.json(metadata)
