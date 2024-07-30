from django.db.models import CharField, ForeignKey, Model, RESTRICT


class Cat(Model):
    breed = ForeignKey(
        'Breed',
        related_name='cats',
        on_delete=RESTRICT
    )
    name = CharField(
        null=False,
        blank=False,
        max_length=255
    )
    description_from_owner = CharField(
        null=False,
        blank=False,
        max_length=1020
    )

    def __str__(self):
        return f'{self.name} of breed {self.breed.name}'


class Breed(Model):
    name = CharField(
        null=False,
        blank=False,
        max_length=255
    )

    def __str__(self):
        return f'breed {self.name}'
