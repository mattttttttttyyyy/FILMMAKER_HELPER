VIDEO_FORMATS = ['3g2', '3gp', 'aaf', 'asf', 'avchd', 'avi', 'drc', 'flv', 'm2v', 'm4p', 'm4v', 'mkv', 'mng', 'mov',
                 'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv', 'mxf', 'nsv', 'ogv', 'ogm', 'qt', 'rm', 'rmvb', 'roq',
                 'srt', 'svi', 'vob', 'webm', 'wmv', 'yuv', 'braw', 'r3d', 'mts', 'ts', 'f4v', 'mve', 'vob']
AUDIO_FORMATS = ['aac', 'aif', 'aiff', 'ape', 'au', 'flac', 'gsm', 'it', 'm3u',
                 'm4a', 'mid', 'mod', 'mp3', 'mpa', 'ogg', 'pls', 'ra', 's3m', 'sid', 'wav', 'wma', 'xm', 'spx', 'alac']
IMAGE_FORMATS = ['3dm', '3ds', 'max', 'bmp', 'dds', 'gif', 'jpg', 'jpeg', 'png', 'psd', 'xcf', 'tga', 'thm', 'tif',
                 'tiff', 'yuv', 'ai', 'eps', 'ps', 'svg', 'dwg', 'dxf', 'gpx', 'kml', 'kmz', 'webp', 'heic', 'heif', 'ico', 'exr']
PROJECT_FILES = ['prproj', 'aep', 'veg', 'fcp', 'fcpx']
TEXT_FILES = ['txt', 'docx', 'rtf', 'odt', 'pdf']

FILE_CATEGORIES = {
    "VIDEO": VIDEO_FORMATS,
    "AUDIO": AUDIO_FORMATS,
    "GFX": IMAGE_FORMATS,
    "PROJECT": PROJECT_FILES,
    "TEXT": TEXT_FILES,
}


def recognize_format(file_name):
    file_name = file_name.lower()

    if '.' not in file_name or file_name.startswith('.'):
        return "UNKNOWN"

    extension = file_name.split('.')[-1]

    for category, formats in FILE_CATEGORIES.items():
        if extension in formats:
            return category

    return "UNKNOWN"




