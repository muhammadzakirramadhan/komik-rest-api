import lib.data as model

class Router:
    @staticmethod
    def run(app):

        @app.route('/')
        def home():
            return {'author':'Yuusha Project','App':'Komikku'}
        
        @app.route('/api')
        def root():
            return model.getRootData()

        @app.route('/api/daftar')
        def daftar_komik():
            return model.getDaftarKomik()
        
        @app.route('/api/projek')
        def project_list():
            return model.getProjectList()
        
        @app.route('/api/tamat')
        def komik_tamat():
            return model.getKomikTamat()
        
        @app.route('/api/jadwal')
        def jadwal_update():
            return model.getJadwalUpdate()

        @app.route('/api/komik')
        def komik():
            return model.getDataKomik()
        
        @app.route('/api/chapter')
        def chapter():
            return model.getChapterComic()
        
        @app.route('/api/cari')
        def search():
            return model.getSpecificComic()