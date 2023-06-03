"""
This type stub file was generated by pyright.
"""

CookieLoadError = ...
class YouTubeTranscriptApi:
    @classmethod
    def list_transcripts(cls, video_id, proxies=..., cookies=...): # -> TranscriptList:
        """
        Retrieves the list of transcripts which are available for a given video. It returns a `TranscriptList` object
        which is iterable and provides methods to filter the list of transcripts for specific languages. While iterating
        over the `TranscriptList` the individual transcripts are represented by `Transcript` objects, which provide
        metadata and can either be fetched by calling `transcript.fetch()` or translated by calling
        `transcript.translate('en')`. Example::

            # retrieve the available transcripts
            transcript_list = YouTubeTranscriptApi.get('video_id')

            # iterate over all available transcripts
            for transcript in transcript_list:
                # the Transcript object provides metadata properties
                print(
                    transcript.video_id,
                    transcript.language,
                    transcript.language_code,
                    # whether it has been manually created or generated by YouTube
                    transcript.is_generated,
                    # a list of languages the transcript can be translated to
                    transcript.translation_languages,
                )

                # fetch the actual transcript data
                print(transcript.fetch())

                # translating the transcript will return another transcript object
                print(transcript.translate('en').fetch())

            # you can also directly filter for the language you are looking for, using the transcript list
            transcript = transcript_list.find_transcript(['de', 'en'])

            # or just filter for manually created transcripts
            transcript = transcript_list.find_manually_created_transcript(['de', 'en'])

            # or automatically generated ones
            transcript = transcript_list.find_generated_transcript(['de', 'en'])

        :param video_id: the youtube video id
        :type video_id: str
        :param proxies: a dictionary mapping of http and https proxies to be used for the network requests
        :type proxies: {'http': str, 'https': str} - http://docs.python-requests.org/en/master/user/advanced/#proxies
        :param cookies: a string of the path to a text file containing youtube authorization cookies
        :type cookies: str
        :return: the list of available transcripts
        :rtype TranscriptList:
        """
        ...
    
    @classmethod
    def get_transcripts(cls, video_ids, languages=..., continue_after_error=..., proxies=..., cookies=..., preserve_formatting=...): # -> tuple[dict[Unknown, Unknown], list[Unknown]]:
        """
        Retrieves the transcripts for a list of videos.

        :param video_ids: a list of youtube video ids
        :type video_ids: list[str]
        :param languages: A list of language codes in a descending priority. For example, if this is set to ['de', 'en']
        it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if it fails to
        do so.
        :type languages: list[str]
        :param continue_after_error: if this is set the execution won't be stopped, if an error occurs while retrieving
        one of the video transcripts
        :type continue_after_error: bool
        :param proxies: a dictionary mapping of http and https proxies to be used for the network requests
        :type proxies: {'http': str, 'https': str} - http://docs.python-requests.org/en/master/user/advanced/#proxies
        :param cookies: a string of the path to a text file containing youtube authorization cookies
        :type cookies: str
        :param preserve_formatting: whether to keep select HTML text formatting
        :type preserve_formatting: bool
        :return: a tuple containing a dictionary mapping video ids onto their corresponding transcripts, and a list of
        video ids, which could not be retrieved
        :rtype ({str: [{'text': str, 'start': float, 'end': float}]}, [str]}):
        """
        ...
    
    @classmethod
    def get_transcript(cls, video_id, languages=..., proxies=..., cookies=..., preserve_formatting=...):
        """
        Retrieves the transcript for a single video. This is just a shortcut for calling::

            YouTubeTranscriptApi.list_transcripts(video_id, proxies).find_transcript(languages).fetch()

        :param video_id: the youtube video id
        :type video_id: str
        :param languages: A list of language codes in a descending priority. For example, if this is set to ['de', 'en']
        it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if it fails to
        do so.
        :type languages: list[str]
        :param proxies: a dictionary mapping of http and https proxies to be used for the network requests
        :type proxies: {'http': str, 'https': str} - http://docs.python-requests.org/en/master/user/advanced/#proxies
        :param cookies: a string of the path to a text file containing youtube authorization cookies
        :type cookies: str
        :param preserve_formatting: whether to keep select HTML text formatting
        :type preserve_formatting: bool
        :return: a list of dictionaries containing the 'text', 'start' and 'duration' keys
        :rtype [{'text': str, 'start': float, 'end': float}]:
        """
        ...
    

