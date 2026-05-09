from moviepy.editor import VideoFileClip


def video_to_gif(input_path, output, duration=5, fps=10):
    clip = VideoFileClip(input_path).subclip(0, duration)
    clip.write_gif(output, fps=fps)
