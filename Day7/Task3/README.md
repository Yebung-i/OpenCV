<img width="1024" height="797" alt="image" src="https://github.com/user-attachments/assets/c75395f3-3bb8-4b17-a7c0-ca990937628e" />

<img width="218" height="37" alt="image" src="https://github.com/user-attachments/assets/f14545c2-830a-4c7b-8e7d-745349d82c58" />


- 화면은 픽셀들의 배열로서, 픽셀들의 좌표는 각각 정수를 가지게 된다. 하지만 영상을 회전시키면 삼각함수 계산으로 인해 좌표가 소수점 단위로 쪼개지게 되는데 (ex: x = 10.4) << 여기서 10.4 번째 픽셀이라는 것은 존재하지 않으므로 10번째와 11번째 픽셀을 섞어서 채우게 된다. (보간법)
- 이로인해 영상이 미세하게 뭉개지고 흐려지는 현상이 발생하게 된다. 이러한 보간법이 중첩되어 결과적으로는 크게 왜곡되는 것이다.

- 때문에 이를 해결하기 위해서는 항상 원본에서 회전을 시켜야 한다.
