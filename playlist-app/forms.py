# forms.py
"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Playlist Name', validators=[InputRequired()])
    description = TextAreaField('Description')

class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Song Title', validators=[InputRequired()])
    artist = StringField('Artist', validators=[InputRequired()])

class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""
    song = SelectField('Song To Add', coerce=int)
