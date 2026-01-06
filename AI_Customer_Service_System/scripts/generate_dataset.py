import json
import random
import os

# Configuration
OUTPUT_FILE = "../data/intents_large.json"
TOTAL_PATTERNS_TARGET = 2000 
TYPO_RATE = 0.08

class Humanizer:
    def __init__(self):
        self.prefixes = {
            "en": ["Umm", "Excuse me,", "Hey,", "Hi,", "Hello,", "So,", "Basically,"],
            "id": ["Permisi", "Punten", "Min", "Kak", "Gan", "Sis", "Bro", "Halo min", "Woi", "Misi", "Mau tanya"]
        }
        self.suffixes = {
            "en": ["please", "thanks", "asap", "can you help?", "???", "!!", "right now"],
            "id": ["dong", "bisa ga?", "ya", "sih", "deh", "cepetan", "tolong", "plis", "gan", "kak", "min", "woy"]
        }
        self.slang_map_id = {
            "saya": ["sy", "aku", "gw", "gue", "ane"],
            "tidak": ["gak", "ga", "enggak", "kaga"],
            "bisa": ["bs", "bisa"],
            "yang": ["yg", "nu"],
            "sudah": ["udh", "sdh", "udah"],
            "bagaimana": ["gmn", "gimana", "kek mana"],
            "kamu": ["lu", "loe", "u"],
            "tolong": ["tlg", "plis", "bantu"],
            "kapan": ["kpn"],
            "dimana": ["dmn", "dimance"],
            "kenapa": ["knp", "napa"],
            "terima kasih": ["makasih", "thx", "tq", "tengkyu"],
            "selamat pagi": ["pagi", "met pagi"],
            "selamat malam": ["malem", "met malem"]
        }

    def humanize(self, text, lang):
        # 1. Slang injection (ID only)
        if lang == "id":
            words = text.split()
            new_words = []
            for w in words:
                lower_w = w.lower().strip("?!.,")
                if lower_w in self.slang_map_id and random.random() < 0.5:
                    replacement = random.choice(self.slang_map_id[lower_w])
                    # Preserve Case (simple)
                    if w[0].isupper(): replacement = replacement.capitalize()
                    new_words.append(replacement)
                else:
                    new_words.append(w)
            text = " ".join(new_words)

        # 2. Add Prefix/Suffix
        if random.random() < 0.3:
            prefix = random.choice(self.prefixes[lang])
            text = f"{prefix} {text}"
        
        if random.random() < 0.3:
            suffix = random.choice(self.suffixes[lang])
            text = f"{text} {suffix}"
            
        return text

# Typo Generator
def introduce_typo(text):
    if len(text) < 4: return text 
    chars = list(text)
    error_type = random.choice(['swap', 'delete', 'double', 'replace'])
    idx = random.randint(1, len(chars) - 2) 
    
    if error_type == 'swap':
        chars[idx], chars[idx+1] = chars[idx+1], chars[idx]
    elif error_type == 'delete':
        del chars[idx]
    elif error_type == 'double':
        chars.insert(idx, chars[idx])
    elif error_type == 'replace':
        nearby = {'a': 's', 's': 'a', 'e': 'r', 'r': 'e', 't': 'y', 'y': 't', 'i': 'o', 'o': 'i', 'n': 'm', 'm': 'n'}
        char = chars[idx].lower()
        if char in nearby:
            chars[idx] = nearby[char]
    return "".join(chars)

def apply_augmentations(patterns, lang, humanizer):
    new_patterns = []
    # Keep originals
    new_patterns.extend(patterns)
    
    # Generate variations
    for p in patterns:
        # 1. Humanized Version
        h_p = humanizer.humanize(p, lang)
        new_patterns.append(h_p)
        
        # 2. Typo Version (on original or humanized)
        if random.random() < TYPO_RATE:
            target = h_p if random.random() < 0.5 else p
            words = target.split()
            if words:
                idx = random.randint(0, len(words)-1)
                words[idx] = introduce_typo(words[idx])
                new_patterns.append(" ".join(words))
                
    # Remove duplicates
    return list(set(new_patterns))

# Data Templates
templates = {
    "order_status": {
        "en": [
            "Where is my {0}?", "Track my {0}", "Check status of {0} #{1}", 
            "I want to know where my {0} is", "Any update on {0}?", 
            "Has my {0} shipped?", "Delivery status for {0}", "Is my {0} arriving soon?",
            "Can you locate my {0}?", "Status update for order #{1}",
            "Where is order #{1}?", "When will I get my {0}?"
        ],
        "id": [
            "Dimana {0} saya?", "Lacak {0} saya", "Cek status {0} #{1}",
            "Saya ingin tahu posisi {0} saya", "Ada update untuk {0}?",
            "Apakah {0} sudah dikirim?", "Status pengiriman {0}", "Kapan {0} sampai?",
            "Bisa cek posisi {0}?", "Update status pesanan #{1}",
            "Paket {0} kok belum sampai?", "Cek resi {0}"
        ],
        "responses": {
            "en": [
                "I can help you check your order status. Please provide your Order ID.",
                "Let me look that up for you. Do you have your tracking number?",
                "You can track your order directly on our 'My Orders' page."
            ],
            "id": [
                "Saya bisa bantu cek status pesanan Anda. Mohon informasikan ID Pesanan Anda.",
                "Biar saya cek sebentar. Apakah Anda memiliki nomor resi?",
                "Anda bisa melacak pesanan langsung di halaman 'Pesanan Saya'."
            ]
        },
        "slots": {
            "0": ["order", "package", "item", "delivery", "shipment", "parcel", "goods", "shoes", "shirt", "laptop", "phone", "book"],
            "1": ["12345", "999", "AB-123", "XYZ", "001", "ORD-888", "TRACK-01"]
        }
    },
    "return_request": {
        "en": [
            "I want to return {0}", "How do I return a {0}?", "Return policy for {0}",
            "Can I send back this {0}?", "Refund for {0}", "The {0} is broken, return please",
            "Exchange {0}", "I don't like this {0}, return it", "Process a return for {0}",
            "Start return process"
        ],
        "id": [
            "Saya mau kembalikan {0}", "Cara retur {0} gimana?", "Kebijakan pengembalian {0}",
            "Bisa balikin {0} ini?", "Minta refund {0}", "{0} nya rusak, mau retur",
            "Tukar {0}", "Saya gak suka {0} ini, balikin", "Proses retur {0}",
            "Mulai proses pengembalian", "Barang {0} cacat, mau ganti"
        ],
        "responses": {
            "en": [
                "We accept returns within 30 days of purchase. Please visit our Returns Center to start.",
                "I'm sorry to hear that. You can initiate a return or exchange from your account dashboard.",
                "For damaged items, please upload a photo in the return form."
            ],
            "id": [
                "Kami menerima pengembalian dalam 30 hari pembelian. Silakan kunjungi Pusat Retur kami.",
                "Maaf mendengarnya. Anda bisa memulai proses retur atau tukar dari dashboard akun Anda.",
                "Untuk barang rusak, mohon unggah foto di formulir pengembalian."
            ]
        },
        "slots": {
            "0": ["item", "product", "shirt", "shoes", "phone", "laptop", "bag", "dress", "pants"]
        }
    },
    "cancel_order": {
        "en": [
            "Cancel my order", "I want to stop the delivery", "Cancel order #{0}", 
            "Don't send the package", "Mistake order, cancel please", "Stop shipment #{0}",
            "Can I cancel?", "Abort order #{0}", "Void transaction", "Cancel purchase"
        ],
        "id": [
            "Batalkan pesanan saya", "Saya mau stop pengiriman", "Cancel order #{0}",
            "Jangan kirim paketnya", "Salah pesan, tolong cancel", "Stop pengiriman #{0}",
            "Bisa batalkan?", "Batalkan pesanan #{0}", "Batalkan transaksi", "Cancel belanjaan",
            "Gajadi beli {0}", "Mau batalin aja"
        ],
        "responses": {
            "en": [
                "Orders can be cancelled within 1 hour of placement. Please check your order details.",
                "I can help with that. Please confirm your Order ID so I can process the cancellation.",
                "If the order hasn't shipped yet, we can cancel it for a full refund."
            ],
            "id": [
                "Pesanan dapat dibatalkan dalam 1 jam setelah pemesanan. Mohon cek detail pesanan Anda.",
                "Saya bisa bantu. Mohon konfirmasi ID Pesanan agar saya bisa memproses pembatalan.",
                "Jika pesanan belum dikirim, kami bisa membatalkannya untuk pengembalian dana penuh."
            ]
        },
        "slots": {
            "0": ["123", "555", "A1", "B2", "Order-X", "Transaction"]
        }
    },
    "payment_issue": {
        "en": [
            "Payment failed", "Cannot pay with {0}", "Credit card error", "My {0} was rejected",
            "How to pay using {0}?", "Payment method not working", "Transaction declined",
            "I was charged twice", "Refund my money", "Payment status pending"
        ],
        "id": [
            "Pembayaran gagal", "Gabisa bayar pakai {0}", "Kartu kredit error", "{0} saya ditolak",
            "Cara bayar pakai {0} gimana?", "Metode pembayaran gangguan", "Transaksi ditolak",
            "Saya tertagih dua kali", "Kembalikan uang saya", "Status pembayaran pending",
            "Kok gabisa bayar ya?"
        ],
        "responses": {
            "en": [
                "We are sorry for the inconvenience. Please try a different payment method or contact your bank.",
                "For double charges, the extra amount is usually refunded automatically within 24 hours.",
                "Please ensure your card details are correct and you have sufficient funds."
            ],
            "id": [
                "Mohon maaf atas ketidaknyamanannya. Silakan coba metode pembayaran lain atau hubungi bank Anda.",
                "Untuk tagihan ganda, jumlah berlebih biasanya dikembalikan otomatis dalam 24 jam.",
                "Pastikan detail kartu Anda benar dan saldo mencukupi."
            ]
        },
        "slots": {
            "0": ["credit card", "debit card", "PayPal", "OVO", "GoPay", "Dana", "Transfer", "Bank"]
        }
    },
    "human_agent": {
        "en": [
            "I want to speak to a human", "Connect me to support agent", "Real person please",
            "Are you a robot?", "I need human help", "Transfer to operator", "Customer service person",
            "Talk to staff", "Live agent", "Not a bot"
        ],
        "id": [
            "Saya mau bicara sama manusia", "Sambungkan ke CS", "Orang beneran dong",
            "Kamu robot ya?", "Butuh bantuan manusia", "Transfer ke operator", "Petugas CS",
            "Bicara sama staf", "Agen langsung", "Bukan bot", "Mana orang aslinya?"
        ],
        "responses": {
            "en": [
                "Connecting you to a customer service agent. Please wait a moment...",
                "I understand. Let me transfer this chat to a human specialist.",
                "Our agents are available Mon-Fri 9AM-5PM. I will create a ticket for you."
            ],
            "id": [
                "Menghubungkan Anda dengan agen layanan pelanggan. Mohon tunggu sebentar...",
                "Saya mengerti. Biarkan saya mentransfer obrolan ini ke spesialis manusia.",
                "Agen kami tersedia Senin-Jumat 09.00-17.00. Saya akan buatkan tiket untuk Anda."
            ]
        },
        "slots": {}
    },
    "promotions": {
        "en": [
            "Any promotions today?", "Discount code please", "Do you have vouchers?",
            "Promo for {0}", "Is {0} on sale?", "Coupons available?", "Best deals for {0}",
            "I want a discount", "Sale info", "Offers for new users"
        ],
        "id": [
            "Ada promo hari ini?", "Minta kode diskon dong", "Punya voucher ga?",
            "Promo untuk {0} ada?", "Apakah {0} lagi diskon?", "Kupon tersedia?", "Penawaran terbaik {0}",
            "Mau diskon dong", "Info sale", "Penawaran pengguna baru"
        ],
        "responses": {
            "en": [
                "Check out our 'Deals of the Day' page for the latest discounts!",
                "New users can use code WELCOME10 for 10% off their first order.",
                "Yes, we have ongoing promotions. Visit the homepage to see them."
            ],
            "id": [
                "Cek halaman 'Promo Hari Ini' kami untuk diskon terbaru!",
                "Pengguna baru bisa pakai kode WELCOME10 untuk diskon 10% pesanan pertama.",
                "Ya, kami ada promo yang sedang berlangsung. Kunjungi beranda untuk melihatnya."
            ]
        },
        "slots": {
            "0": ["shoes", "bag", "laptop", "iphone", "samsung", "clothes", "membership", "shipping"]
        }
    },
    "shipping_info": {
        "en": [
            "How much is shipping to {0}?", "Shipping cost to {0}", "Do you ship to {0}?",
            "Delivery fee for {0}", "Free shipping available?", "How long to ship to {0}?",
            "Courier options for {0}", "Shipping rates", "Delivery time to {0}", "Send to {0}"
        ],
        "id": [
            "Berapa ongkir ke {0}?", "Biaya kirim ke {0}", "Bisa kirim ke {0}?",
            "Ongkos kirim {0}", "Ada gratis ongkir?", "Berapa lama kirim ke {0}?",
            "Pilihan kurir ke {0}", "Tarif pengiriman", "Waktu pengiriman ke {0}", "Kirim ke {0}"
        ],
        "responses": {
            "en": [
                "Shipping costs depend on weight and location. You can estimate it in your cart.",
                "We offer free shipping on orders over $50!",
                "Standard delivery takes 3-5 business days. Express options are available."
            ],
            "id": [
                "Ongkos kirim tergantung berat dan lokasi. Anda bisa estimasi di keranjang belanja.",
                "Kami menawarkan gratis ongkir untuk pesanan di atas Rp 500rb!",
                "Pengiriman standar memakan waktu 3-5 hari kerja. Tersedia opsi Ekspres."
            ]
        },
        "slots": {
            "0": ["Jakarta", "Bali", "Bandung", "Surabaya", "Medan", "Singapore", "USA", "my house", "office"]
        }
    },
    "account_issue": {
        "en": [
            "Cannot login", "Forgot password", "Reset my account", "Change email to {0}",
            "Update profile", "Delete my account", "Account hacked", "Login failed",
            "Sign up issue", "Register help"
        ],
        "id": [
            "Gabisa login", "Lupa password", "Reset akun saya", "Ganti email ke {0}",
            "Update profil", "Hapus akun saya", "Akun dibajak", "Gagal masuk",
            "Masalah daftar", "Bantuan registrasi", "Susah masuk akun"
        ],
        "responses": {
            "en": [
                "You can reset your password by clicking 'Forgot Password' on the login screen.",
                "To update your profile, go to Account Settings > Edit Profile.",
                "If you suspect your account is compromised, please contact support immediately."
            ],
            "id": [
                "Anda bisa reset password dengan klik 'Lupa Password' di layar login.",
                "Untuk update profil, buka Pengaturan Akun > Edit Profil.",
                "Jika Anda curiga akun dibajak, segera hubungi support kami."
            ]
        },
        "slots": {
            "0": ["gmail", "yahoo", "new email", "phone number"]
        }
    }
}

# Base Intents
base_intents = [
    {
        "tag": "greeting",
        "patterns": {
            "en": ["Hi", "Hello", "Good morning", "Hey there", "Is anyone there?", "Hola", "Greetings", "Yo", "Hiya", "Good evening", "Good afternoon", "Hey", "Hi bot", "Hello support", "Start chat"],
            "id": ["Halo", "Hai", "Selamat pagi", "Selamat siang", "Ada orang?", "Permisi", "Woi", "Met pagi", "Pagi", "Siang", "Sore", "Malam", "Halo min", "Hai bot", "Mulai chat", "P", "Assalamualaikum", "Tes"]
        },
        "responses": {
            "en": ["Hello! How can I help you?", "Hi there! Welcome."],
            "id": ["Halo! Ada yang bisa dibantu?", "Hai! Selamat datang."]
        }
    },
    {
        "tag": "goodbye",
        "patterns": {
            "en": ["Bye", "See you", "Goodbye", "Exit", "Quit", "End", "Done", "No more help", "Leaving now", "Goodnight"],
            "id": ["Dah", "Sampai jumpa", "Dadah", "Keluar", "Selesai", "Udah", "Cukup", "Pergi dulu", "Met malam", "Bye", "Makasih min"]
        },
        "responses": {
            "en": ["Goodbye!", "See you soon."],
            "id": ["Sampai jumpa!", "Dadah."]
        }
    },
    {
        "tag": "thanks",
        "patterns": {
            "en": ["Thanks", "Thank you", "Thx", "Appreciate it", "Thanks a lot", "Good job", "Helpful", "Cool thanks", "Ty", "Tysm"],
            "id": ["Makasih", "Terima kasih", "Tq", "Maksih", "Mantap", "Sangat membantu", "Ok thanks", "Suwun", "Hatur nuhun", "Trims", "Thank you"]
        },
        "responses": {
            "en": ["You're welcome!", "Glad to help."],
            "id": ["Sama-sama!", "Senang bisa membantu."]
        }
    }
]

def generate_expanded_intents():
    final_intents = []
    humanizer = Humanizer()
    
    # 1. Process Base Intents
    for intent in base_intents:
        # Augment base patterns too
        p_en = apply_augmentations(intent["patterns"]["en"], "en", humanizer)
        p_id = apply_augmentations(intent["patterns"]["id"], "id", humanizer)
        intent["patterns"]["en"] = p_en
        intent["patterns"]["id"] = p_id
        final_intents.append(intent)

    # 2. Process Template Intents
    for tag, data in templates.items():
        patterns_en = []
        patterns_id = []
        
        # Generate EN
        for tmpl in data["en"]:
            if "{0}" in tmpl:
                for item in data["slots"].get("0", ["item"]):
                    s = tmpl.replace("{0}", item)
                    if "{1}" in s:
                        for id_val in data["slots"].get("1", ["123"]):
                            patterns_en.append(s.replace("{1}", id_val))
                    else:
                        patterns_en.append(s)
            else:
                patterns_en.append(tmpl)
                
        # Generate ID
        for tmpl in data["id"]:
            if "{0}" in tmpl:
                for item in data["slots"].get("0", ["item"]):
                    s = tmpl.replace("{0}", item)
                    if "{1}" in s:
                        for id_val in data["slots"].get("1", ["123"]):
                            patterns_id.append(s.replace("{1}", id_val))
                    else:
                        patterns_id.append(s)
            else:
                patterns_id.append(tmpl)

        # Apply Augmentations (Humanize + Typo)
        aug_en = apply_augmentations(patterns_en, "en", humanizer)
        aug_id = apply_augmentations(patterns_id, "id", humanizer)

        final_intents.append({
            "tag": tag,
            "patterns": {
                "en": aug_en,
                "id": aug_id
            },
            "responses": data["responses"],
            "context_set": ""
        })

    # Stats
    total_count = 0
    for intent in final_intents:
        count = len(intent["patterns"]["en"]) + len(intent["patterns"]["id"])
        total_count += count
        print(f"Intent '{intent['tag']}': {count} patterns")

    print(f"Total Patterns Generated: {total_count}")
    
    # Structure
    output_data = {"intents": final_intents}
    
    # Write
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output_data, f, indent=2)
    print(f"Dataset saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_expanded_intents()
