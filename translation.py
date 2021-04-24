class Translation(object):
    START_TEXT = """Haii 😊
Jika Kamu Ingin Membuat App ID sama Api HASH Pada Akun Telegram Kamu,
Silahkan ketik Nomor HP Anda disini, Wajib (+62) ya 😁
/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """✔️ Berhasil...
Silahkan Cek Pesan Masuk di Telegram Kamu, Ambil Kode Yang Telah Dikirim Oleh Pihak Telegram!
Jika Sudah Di Copy, Silahkan Kirim Kode Kamu Disini.
/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "Mendapatkan Kode. Scarpping web page ..."
    ERRED_PAGE = "Terjadi error. Gagal untuk mendapatkan app id. \n\nSilahkan Hubungi @SyndicateTwenty4"
    CANCELLED_MESG = "Goodbye! Mohon re /start Bot Untuk Memulai Ulang Kembali."
    IN_VALID_CODE_PVDED = "Mohon Maaf, Kode Dari Telegram Yang Kamu Masukkan Tidak Valid.\n Mohon Periksa Kembali, Terimakasih."
    IN_VALID_PHNO_PVDED = "Mohon Maaf, Masukkan Nomor Telepon Kamu Dengan Awalan Kode Negara, Seperti +62857"
