from sqlmodel import create_engine


def connect():
    engine = create_engine("sqlite:///bbdd/koreanpop")
    return engine