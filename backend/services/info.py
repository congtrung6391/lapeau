from flask import Blueprint, request, jsonify, json, Response

bp = Blueprint('info', __name__, url_prefix='/info')

sicknessData = {
  '0': {
    'id': 1,
    'name': 'Kiến ba khoang',
    'reason': 'Tiếp xúc với dịch cơ thể có chứa pederin của kiến ba khoang.',
    'description': 'Viêm da khi bị côn trùng đốt',
    'symptom': [
      {
        'id': 1,
        'description': 'Đỏ da, phồng rộp, mụn nước, mụn bỏng, đau rát, để lâu tiến tới loét da, nhiễm trùng.',
      }
    ],
    'trailer': 'https://vcdn-suckhoe.vnecdn.net/2019/10/12/kien-ba-khoang-3-3239-1570889743.jpg?fbclid=IwAR1i_kGxIi7nsjTxgvJh51bYq7nHwkDzVbcfaKE24NHW2219I_Dq420A3BU'
  },
  '1': {
    'id': 2,
    'name': 'Bệnh zona hay herpes zoster',
    'reason': 'Bệnh do sự tái hoạt của virus Varicella zoster (VZV) tiềm ẩn ở rễ thần kinh cảm giác cạnh cột sống, chính là virus gây bệnh thủy đậu',
    'description': 'Bệnh da do virus',
    'symptom': [
      {
        'id': 4,
        'name': 'ho',
        'description': 'Lâm sàng. Trước khi tổn thương mọc 2-3 ngày thường có cảm giác báo hiệu như: rát dấm dứt, đau vùng sắp mọc tổn thư­ơng kèm theo triệu chứng toàn thân ít hoặc nhiều như mệt mỏi, đau đầu... Hạch ngoại vi lân cận có thể sưng và đau.',
      },
      {
        'id': 5,
        'name': 'ho',
        'description': 'Vị trí: thường khu trú tập trung ở những vị trí đặc biệt và chỉ có một bên của cơ thể dọc theo các đường dây thần kinh, như­ng cá biệt có thể bị cả hai bên hay lan toả.',
      },
      {
        'id': 6,
        'name': 'ho',
        'description': 'Tổn thương cơ bản: thường bắt đầu là các mảng đỏ, nề nhẹ, gờ cao hơn mặt da, hình tròn, bầu dục lần l­ượt nổi dọc dây thần kinh, rải rác hoặc cụm lại thành dải, thành vệt, sau 1-2 giờ trên mảng đỏ xuất hiện những mụn n­ước chứa dịch trong, căng khó vỡ, các mụn nước tập trung thành cụm (như­ chùm nho), về sau đục, vỡ, xẹp để lại sẹo (nếu nhiễm khuẩn). Tr­ước hoặc cùng với mọc tổn thương ở da thư­ờng nổi hạch sưng và đau ở vùng tư­ơng ứng và là dấu hiệu quan trọng để chẩn đoán.'
      }
    ],
    'trailer': 'https://soyte.hanoi.gov.vn/documents/3672249/4984478/H%C6%B0%C6%A1ng+6.2+tri%E1%BB%87u+ch%E1%BB%A9ng+b%E1%BB%87nh+zona+th%E1%BA%A7n+kinh.jpg/f5a7c7dc-ff9e-4690-bbc9-ba33c86a433a?t=1581002026448&fbclid=IwAR1Y-HjFiObd_eRG-EkHiin3XgNllpZeZ-xfGdfGcKYKsG7KXdKgayR7TVg'
  },
  '2': {
    'id': 3,
    'name': 'Vẩy nến',
    'reason': 'Di truyền, nhiễm khuẩn, stress, hiện tượng Koebner',
    'description': 'Bệnh đỏ da có vảy',
    'symptom': [
      {
        'id': 7,
        'name': 'ho',
        'description': 'Thương tổn da: da đỏ giới hạn rõ với da lành, trên da phủ vảy trắng dễ bong.',
      }
    ],
    'trailer': 'https://ehib.org/wp-content/uploads/2020/10/dieu-tri-benh-vay-nen.jpg?fbclid=IwAR3VnEBNZJtyxkPlsJYmwAChD0ju4vCOgTW-0Ff_TUJT7Y4a1vWtRuytDBk'
  },
  '3': {
    'id': 4,
    'name': 'Da vảy cá',
    'reason': 'Di truyền hoặc mắc phải khi da không loại bỏ được các tế bào chết của nó. Điều này làm cho các tế bào da chết khô đi, tích tụ thành các mảng bám trên bề mặt da như vảy cá, thường liên quan đến các bệnh khác như ung thư, bệnh tuyến giáp hoặc HIV/AIDS..',
    'description': 'Bệnh có vảy',
    'symptom': [
      {
        'id': 10,
        'name': 'ho',
        'description': 'Da khô, đóng vảy, các vảy nhỏ, xếp lớp. Vảy có màu trắng, xám bẩn hoặc nâu – vảy sẫm màu thường ở da sẫm màu',
      },
      {
        'id': 11,
        'name': 'ho',
        'description': 'Da đầu bong từng mảng',
      },
      {
        'id': 12,
        'name': 'ho',
        'description': 'Các vết nứt sâu và đau ở da'
      }
    ],
    'trailer': 'https://img.over-blog-kiwi.com/2/52/04/36/20180721/ob_95f2fe_benh-vay-ca-thong-thuong.jpg?fbclid=IwAR1d6ji4-nN_9iAgKe4OLV_STi6QFAjPunV1_mqM6yfK4KQ9RwU1KHl_pdQ'
  }
}

medicalCenterData = {
  '0': {
    'id': 1,
    'name': 'thien hanh',
    'address': '01 le dai hanh',
    'phone': '03958900',
  },
  '1': {
    'id': 2,
    'name': 'van lang',
    'address': '1345 ngo tat to',
    'phone': 'xx23514423',
  }
}

@bp.route('sickness')
def getSickness():
  return sicknessData, 200

@bp.route('medicalcenter')
def getMedicalCenter():
  return medicalCenterData, 200