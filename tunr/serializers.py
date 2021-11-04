# region non-REST CRUD

# from rest_framework import serializers
# from .models import Artist, Song

# class ArtistSerializer(serializers.HyperlinkedModelSerializer):
#     songs = serializers.HyperlinkedRelatedField(
#         view_name='song_detail',
#         many=True,
#         read_only=True
#     )

#     # Meta class is supposed to be inside ArtistsSerializer class
#     class Meta:
#         model = Artist
#         fields = ('id', 'photo_url', 'nationality', 'name', 'songs',)


# class SongSerializer(serializers.HyperlinkedModelSerializer):
#     artists = serializers.HyperlinkedRelatedField(
#         view_name='song_detail',
#         read_only=True
#     )
    
#     # Meta class is supposed to be inside SongsSerializer class
#     class Meta:
#         model = Song
#         fields = ('id', 'title', 'album', 'preview_url', 'artists')

# endregion


# region REST CRUD

from rest_framework import serializers
from .models import Artist, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=True,
        read_only=True
    )

    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )

    # Meta class is supposed to be inside ArtistsSerializer class
    class Meta:
        model = Artist
        fields = ('id', 'artist_url', 'photo_url', 'nationality', 'name', 'songs',)


class SongSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=False,
        read_only=True
    )

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )
    
    # Meta class is supposed to be inside SongsSerializer class
    class Meta:
        model = Song
        fields = ('id', 'artists', 'artist_id', 'title', 'album', 'preview_url')

# endregion