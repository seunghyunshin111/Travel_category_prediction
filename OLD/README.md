# Final_project_practice
<br>

## 참고 

[Flickr API-reference](https://github.com/alexis-mignon/python-flickr-api/wiki/API-reference)

사진 태그
사진에는 0개 이상의 태그가 있을 수 있습니다. 각 태그에는 사용자가 사용할 수 있도록 리턴된 수많은 필드가 있습니다.

<tag id="1234" author="12037949754@N01" raw="woo yay">wooyay</tag>

id

이 사진에 있는 이 태그의 고유 ID. 이는 flickr.photos.removeTag 메소드를 사용하여 단일 태그를 삭제할 때 사용할 수 있습니다.

author

태그를 추가한 사용자의 NSID입니다. 이는 사진 소유자와 같은 NSID가 아닐 수도 있습니다.

raw

사용자가 입력한 대로 태그의 '원본' 버전입니다. 이 버전에는 공백과 구두점이 포함될 수 있습니다.

tag-body

Flickr가 처리한 대로 태그의 '클린' 버전입니다. 이 버전은 url을 작성하는 데 사용됩니다.

