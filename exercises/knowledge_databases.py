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

add_article("https://en.wikipedia.org/wiki/Theology", "Theology", 8)
	

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
