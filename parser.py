import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""

S -> NP[rn=?x] VP[rn=?x]
S -> NP[rn=?x] VP[rn=?x] PP[rn=?x]
NP[rn=?x] -> NN[rn=?x] NN[rn=?x]
NP[rn=?x] -> CP NP[rn=?x]
NP[rn=?x] -> NP[rn=?x] PP
NP[rn=?x] -> NN[rn=?x] NNP[rn=?x]
NP[rn=?x] -> UNN NN[rn=?x]
NP[rn=?x] -> NN[rn=?x]
NP[rn=?x] -> NNP[rn=?x]
NP[rn=?x] -> NP[rn=?x] ADJP[rn=?x]
NP[rn=?x] -> DT NP[rn=?x]
NP[rn=?x] -> NN[rn=?x] ADJP[rn=?x]
NP[rn=?x] -> NP[rn=?x] CC NP[rn=?x]
NP[rn=?x] -> NN[rn=?x] VP[rn=?x]
VP[rn=?x] -> VP[rn=?x] PP
VP[rn=?x] -> MD VB[rn=?x]
VP[rn=?x] -> VB[rn=?x] NP[rn=?x] VP[rn=?x]
VP[rn=?x] -> ADVP PP[rn=?x]
VP -> ADVP VB[rn=?x]
VP[rn=?x] -> VB[rn=?x]
VP[rn=?x] -> VB[rn=?x] NP[rn=?x]
VP[rn=?x] -> VB[rn=?x, rd=?y] NP[rn=?y]
VP[rn=?x] -> NP[rn=?x] PP[rn=?x]

VP[rn=?x] -> VP[rn=?x] NP

VP[rn=?x] -> VB[rn=?x] VB[rn=?x]
VP[rn=?x] -> VB[rn=?x] VB
ADJP[rn=?x] -> JJ[rn=?x]
ADJP[rn=?x] -> JJ[rn=?x] JJ[rn=?x]
PP[rn=?x] -> IN NP[rn=?x]

NN[] ->'trời' | 'sắt' |'bột'  
NN[rn=thoigian] -> 'sáng' 
NN[rn=diadiem] ->'đất' |'sa_mạc'|'chợ' |'sân'
NNP -> 'Hà_Nội'
NNP[rn=nguoi] ->'Mai'| 'Lan' | 'Sơn' | 'Quang_Hải' | 'Hùng_Dũng' | 'Minh' | 'Sơn_Tùng' | 'Tuấn'
NN[rn=nguoi] -> 'chàng'|'trai'|'bố_mẹ'|'cậu'|'bé'|'tên_cướp'|'anh'|'người_máy'|'người'|'bạn'|'mẹ'|'tôi'|'cô'|'gái'|'con'
NN[rn=dongvat]  -> 'lạc_đà'|'chuột'|'mèo'
NN[rn=chim] -> 'hải_âu' 
NN[rn=hoa] -> 'hoa'|'sen'
NN[rn=suvat] -> 'cây_bút'|'quyển_sách'|'hàng'|'cửa_sổ'|'chậu'|'hoa'|'câu_lạc_bộ'|'phim'|'thư'|'tò_he' |'bài_hát'|'cơm' |'nhà'
NN[rn=xe] ->'xe'
NN[rn=thethao]->'bóng đá'|'bóng bàn'
VB[rn=nguoi] -> 'theo'| 'đi' | 'chạy' | 'hát' | 'nói' | 'ngủ' | 'làm' | 'đánh'| 'nấu' |  'chơi' | 'thi_đấu'  | 'sợ' |'nhảy' | 'học' | 'yêu'  |'bắt_nạt'|'gặp'|'dừng' |'bắt' |'vỡ' |'gửi' |'thích'  |'xem'|'nấu'
VB[rn=chim]  -> 'bay' | 'đi' | 'chạy' |'ngủ' | 'nhảy'  | 'sợ'
VB[rn=dongvat] ->'đi' | 'chạy' |'ngủ' | 'nhảy'  | 'sợ' |'bắt' |'theo'
VB[rn=hoa] -> 'nở'
VB[rn=xe] ->'lái'
VB[rn=diadiem] -> 'xuống'
VB[rn=nguoi,rd=suvat] -> 'có'
VB[rn=nguoi,rd=suvat] -> 'mở'
VB[rn=nguoi,rd=thethao] -> 'choi' | 'the_thao'
JJ[rn=nguoi] -> 'xinh_đẹp' | 'cao' | 'to' | 'đen' | 'nghịch_ngợm' | 'hung_hãn'
JJ[rn=dongvat] -> 'cao' | 'to' | 'đen' | 'nghịch_ngợm' | 'hung_hãn'
IN -> 'của' | 'trên' | 'bằng' | 'trong' | 'ở'  | 'cho' | 'giữa' | 'ra'  | 'lúc' |'trước'
IN[rn=diadiem] -> 'trước' | 'giữa'|| 'ở'
IN[rn=thoigian] ->'lúc' | 'trước' |'từ' 
DT -> 'những'|'các'|'một'
ADVP -> 'có_thể' |'đều'
CC -> 'lẫn' | 'và' | 'hoặc' 
UNN -> 'con'
MD ->'bị'
""")

parser = nltk.parse.FeatureChartParser(grammar)

sentences=[
"Minh đi học lúc sáng"
]

for sent in sentences:
	print(sent)
	words = sent.split()
	for tree in parser.parse(words):
		tree.draw()
		
	