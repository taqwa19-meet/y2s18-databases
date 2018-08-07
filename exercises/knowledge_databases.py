from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_link, article_topic, article_rating):
	Knowledge_object = Knowledge(
		article_link=article_link,
	    article_topic=article_topic,
	    topic_rating=article_rating)
	session.add(Knowledge_object)
	session.commit()


	

def query_all_articles():
	article = session.query(
       #Knowledge).filter_by(
       Knowledge).all()
	return article


def query_article_by_topic(topic):
	#Knowledge).filter_by(
      # article_topic=their_name).all()
	x=session.query(Knowledge).filter_by(
       article_topic=topic).all()
	return x



def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
       article_topic=topic).delete()
	session.commit()




def delete_all_articles():
	

def edit_article_rating(student_id,topic_rating):
	student_object = session.query(
       Student).filter_by(
       name=name).first()
   student_object.finished_lab = finished_lab
   session.commit()





add_article("https://en.wikipedia.org/wiki/Theology", "Theology", 8)

print(query_all_articles())

delete_article_by_topic("Theology")

print(query_all_articles())