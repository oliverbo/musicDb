from apptools.data_handler import DataHandler
import musicdb.music_data_handler

# Initialize Data Handlers
DataHandler.register("venue", music_data_handler.VenueHandler())
DataHandler.register("artist", music_data_handler.ArtistHandler())