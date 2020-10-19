'''from django.contrib.auth.tokens import PasswordResetTokenGenerator
# passwordresettokengenerator: 장고에서 제공하는 class. 비밀번호를 재설정할 때 token을 발급하고 해당 기능을 처리
# import six의 six Library에서 토큰을 만들어냈는데 3.0에서 six를 지원하지 않는다고 한다
# six 대신 str로 pk와 time stamp

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (str(user.pk) + str(timestamp)) + str(user.is_active)
        # text_type: 유니코드 정수로부터 유니코드 문자열을 가져옴. user의 pk, 현재 시간, user의 활성화를 합쳐 tokens를 생성

account_activation_token = AccountActivationTokenGenerator()
'''

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) + six.text_type(user.is_active)
        
account_activation_token = AccountActivationTokenGenerator()