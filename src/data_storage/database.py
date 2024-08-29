from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class NetworkMetric(Base):
    __tablename__ = 'network_metrics'
    id = Column(Integer, primary_key=True)
    metric_name = Column(String)
    value = Column(Integer)

engine = create_engine('sqlite:///network_metrics.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_metric(metric_name, value):
    """Add a new network metric to the database."""
    new_metric = NetworkMetric(metric_name=metric_name, value=value)
    session.add(new_metric)
    session.commit()

if __name__ == "__main__":
    # Example usage
    add_metric('latency', 50)
    print("Metric added to database")