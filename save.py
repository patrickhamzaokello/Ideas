from pytube import YouTube
YouTube("https://www.youtube.com/watch?v=Pmkrn2AR9W0").streams.first().download('~/Downloads')