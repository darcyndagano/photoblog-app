from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'le mot de passe doit contenir une lettre',
                code='password_no_letters')

    def get_help_text(self):
        return 'votre mot de passe doit contenir au moins une lettre majucule ou minuscule'


class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(character.isdigit() for character in password):
            raise ValidationError('le mot de passe doit contenir un chiffre',
                                  code='password_no_number')

    def get_help_text(self):
        return 'votre mot de passe doit contenir au moins un chiffre'
