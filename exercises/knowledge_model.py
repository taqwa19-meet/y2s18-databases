from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	
    __tablename__="Knowledge"
    student_id=Column(Integer, primary_key=True)
    article_link=Column(String)
    article_topic=Column(String)
    topic_rating=Column(Integer)

	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

    def __repr__(self):
        return ("If you want to learn about :{}, you should look at the Wikipedia article called :{}."
				"We gave this article a rating of {} out of 10!").format(self.article_topic, self.article_link, self.topic_rating)
		#return (" article_link: {}\n"
				#" article_topic: {}\n"
				#" topic_rating: {}".format(
					#self.article_link, self.article_topic, self.topic_rating)
x=Knowledge(article_link="https://en.wikipedia.org/wiki/Plastic_surgery", article_topic="Plastic_surgery", topic_rating=8)
y=Knowledge(article_link="https://en.wikipedia.org/wiki/Theology", article_topic="Theology", topic_rating=9)
print(x)
print(y)