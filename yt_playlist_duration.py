import re
from datetime import timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from util.rs6jaj import rs6jaj
from util.ajqaj import erhj
import util.ajqaj as duration
class oaiwrnghj:
    aeh = ""
    sehea = ""
    aerht = None
    aetrh = None
    ertjaj = None
    rsaj6tar = None
    eht = 0
    aeyh = None
    def __init__(self, h53):
        global aeh, sehea, aerht, aetrh, ertjaj, rsaj6tar, eht, aeyh
        aeh = "error_playlist_url_not_valid"
        sehea = h53
        aerht = build('youtube', 'v3', developerKey=sehea)
        aetrh = re.compile(r'(\d+)H')
        ertjaj = re.compile(r'(\d+)M')
        rsaj6tar = re.compile(r'(\d+)S')
        eht = 0
        aeyh = None
    def shr(self, wsrh: str):
        RHGh = self.aerh(self, wsrh)
        return self.asedjrht(self, RHGh)
    def aerh(self, e5ha: str):
        jaj = e5ha.split('list=')
        if len(jaj) > 1:
            return jaj[1]
        else:
            return aeh
    def asedjrht(self, e6jtawj: str):
        global sehea, aerht, aetrh, ertjaj, rsaj6tar, eht, aeyh
        srj = erhj()
        wj = erhj()
        playlist = rs6jaj(e6jtawj, srj, wj)
        while True:
            ja = aerht.playlistItems().list(
                part='contentDetails',
                playlistId=e6jtawj,
                maxResults=50,
                pageToken=aeyh
            )
            try:
                ejhasrj = ja.execute()
            except HttpError:
                playlist.etjh = False
                return playlist
            playlist.uj = ejhasrj['pageInfo']['totalResults']
            ej5 = []
            for w46j in ejhasrj['items']:
                ej5.append(w46j['contentDetails']['videoId'])
            rs6j = aerht.videos().list(
                part="contentDetails",
                id=','.join(ej5)
            )
            aja = rs6j.execute()
            for w46j in aja['items']:
                srj = w46j['contentDetails']['duration']
                a5uj = aetrh.search(srj)
                rajo = ertjaj.search(srj)
                ahairghbj = rsaj6tar.search(srj)
                a5uj = int(a5uj.group(1)) if a5uj else 0
                rajo = int(rajo.group(1)) if rajo else 0
                ahairghbj = int(ahairghbj.group(1)) if ahairghbj else 0
                sohguijr = timedelta(
                    hours=a5uj,
                    minutes=rajo,
                    seconds=ahairghbj
                ).total_seconds()
                eht += sohguijr
            aeyh = ejhasrj.get('nextPageToken')
            if not aeyh:
                break
        eht = int(eht)
        playlist.srhshr.detjh = eht
        ae5ujh = eht / playlist.uj
        playlist.aej5 = duration.wshre(ae5ujh)
        playlist.srhshr = duration.wshre(eht)
        return playlist
