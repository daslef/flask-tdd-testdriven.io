from flask.cli import FlaskGroup

from project import create_app, db
from project.api.users.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    mock_users = [
        {"username": "Mommy", "email": "malekseicik0@constantcontact.com"},
        {"username": "Kerrin", "email": "kdugald1@bloomberg.com"},
        {"username": "Hendrika", "email": "hbridgman2@nba.com"},
        {"username": "Rowland", "email": "rkleinlerer3@weather.com"},
        {"username": "Georgiana", "email": "gmunnings4@auda.org.au"},
        {"username": "Merrily", "email": "mhentze5@exblog.jp"},
        {"username": "Georgianne", "email": "gpitney6@phpbb.com"},
        {"username": "Eal", "email": "echaudhry7@hao123.com"}
        ]

    for user in mock_users:
        db.session.add(User(username=user['username'], email=user['email']))

    db.session.commit()


if __name__ == '__main__':
    cli()
