from django.contrib import admin
from .models import Choice, Question  # 🌟 Choiceも忘れずにインポート

# 1. 選択肢を「インライン（埋め込み）」で表示するための設定
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 最初から入力欄を3つ出しておく

# 2. 質問の管理画面のカスタマイズ設定
class QuestionAdmin(admin.ModelAdmin):
    # ここに「選択肢をインラインで表示する」設定を紐づけます
    inlines = [ChoiceInline]

# 3. Questionを登録するときに、上で作った特別な設定（QuestionAdmin）を適用する
admin.site.register(Question, QuestionAdmin)