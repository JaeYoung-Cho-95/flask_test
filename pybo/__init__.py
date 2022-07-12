from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config
db = SQLAlchemy()
migrate = Migrate()

# create_app 은 flask 의 내부에 정의된 함수로 애플리케이션 팩토리이다.
# 다른 이름으로 하면 작동하지 않으며 app 객체를 생성하고 반환하게 한다.

def create_app():
    app = Flask(__name__)

    # config 파일에 작성한 항목을 읽기 위해서 아래 코드 추가
    app.config.from_object(config)

    # ORM
    # 플라스크는 이러한 패턴을 자주 사용한다.
    # db 객체를 create_app 함수 안에서 생성하면 블루프린트와 같은 다른 모듈에서 사용할 수 없기 때문에
    # db, migrate 와 같은 객체를 create_app 함수 밖에 생성하고, 해당 객체를 앱에 등록할 때는 init_app 함수로 진행
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # 블루프린트
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app