import pytz
from random import randint
from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from blog.models import Post


class Command(BaseCommand):
    help = 'create fake users and posts for testing'
    default_count = 10

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

        parser.add_argument('--clear',
            action='store_true',
            help='clear the data base before adding new records')


    def handle(self, *args, **options):
        if options.get('clear'):
            self.stdout.write('Clearing the database...', ending='\n')
            self.stdout.write('Deleting all users except for admins...', ending='\n')
            users = User.objects.all()
            for user in users:
                if user.is_superuser:
                    continue
                else:
                    user.delete()
            Post.objects.all().delete()
        
        self.stdout.write('Creating Users...', ending='\n')
        self.create_users(options.get('count')[0])
        self.stdout.write('Creating Posts...', ending='\n')
        self.create_posts(options.get('count')[0])

    def create_users(self, count):
        fake = Faker()
        for _ in range(count):
            u = User(email=fake.email(), username=fake.user_name())
            u.set_password('testpass1')
            u.save()
    
    def create_posts(self, count):
        fake = Faker()
        users_count = User.objects.count()
        last_user = User.objects.latest('pk')
        created = 0
        while created < count:
            try:
                u = User.objects.get(id=randint(1, last_user.id))
                p = Post(title=fake.sentence(), content=fake.text(), 
                    author=u, date=fake.past_datetime(tzinfo=pytz.UTC))
                p.save()
                created += 1
            except (User.DoesNotExist):
                pass
        
            
