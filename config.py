import os

BASE_DIR = os.path.dirname(__file__)


# 보통 sqlite 는 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 데이터베이스이다.
# SQLite 로 개발하고 실제 운영시스템에서는 좀 더 규모가 큰 데이터베이스로 교체한다.
# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# SQLALCHEMY 의 이벤트를 처리하는 옵션인데 이 프로젝트에는 필요하지 않기 때문에 비활성화
SQLALCHEMY_TRACK_MODIFICATIONS = False

