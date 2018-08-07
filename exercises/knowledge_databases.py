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
	    topic_ratings=article_rating)
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
	session.query(Knowledge).all().delete()
	session.commit()   

	

def edit_article_rating(student_id,topic_ratings):
	t = session.query(
       Knowledge).filter_by(
       topic_ratings=article_rating).all()
    





add_article("https://en.wikipedia.org/wiki/Theology", "Theology", 8)

print(query_all_articles())

delete_article_by_topic("Theology")

print(query_all_articles())
