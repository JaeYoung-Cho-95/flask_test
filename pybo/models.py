from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    # 답변과 질문을 연결하기 위해 추가한 속성이다.
    # 어떤 질문에 대한 답변인지 알아야하므로 질문의 id 속성이 필요하다.
    # 모델을 서로 연결할 때는 아래와 같이 db.ForeignKey 를 사용한다.
    # question.id 는 question 테이블의 id column 을 의미한다.
    # ondelete 는 삭제 연동 설정이다. 즉, ondelete = 'CASCADE' 는 질문을 질문에 달린 답변도 함께 삭제된다는 말이다.
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'CASCADE'))

    # 답변모델에서 질문 모델을 참조하기 위해 추가했다. 아래와 같이 db.relationship 으로
    # question 속성을 생성하면 답변 모델에서 연결된 질문의 제목을 answer.question.subject 처럼 참조할 수 있다.
    # db.backref 역참조 설정.
    question = db.relationship('Question', backref = db.backref('answer_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
