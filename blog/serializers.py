from rest_framework.serializers import ModelSerializer

from blog.models import Post,Category

class CategorySerialozer(ModelSerializer):
  class Meta:
    model = Category
    fields = (
      "id",
      "title"
    )

# 送られてきた値を適切な形に変換（バリデーションや型変換を実行）
# modelと1:1で変換をおこなうものmodalの中身から必要なものを取得して実施する
class PostSerializer(ModelSerializer):
  class Meta:
    model = Post
    fields = (
      "id",
      "title",
      "content",
      "header_image",
    )