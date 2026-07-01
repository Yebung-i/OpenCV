## a 값이 너무 클 경우 << 20
<img width="1536" height="542" alt="image" src="https://github.com/user-attachments/assets/3e09845c-0c65-47ed-bb2c-add334ff539a" />

- dst = a * (image - 128) + 128  << a는 기울기 이기에, 중간값인 128보다 조금만 커도 결과값이 255를 쉽게 초과하며, 반대로 조금만 작아도 결과값이 0 미만으로 떨어지게 된다. 결과적으로는 중간값인 회색이 거의 소실되어 새하얗거나 새까만 흑백 이미지처럼
변형된다.

# a 값이 너무 작을 경우 << 0
<img width="1538" height="539" alt="image" src="https://github.com/user-attachments/assets/002a2e63-ed94-4f23-9ddd-73ae9c2f01eb" />

- 너무 작을 경우에는, 반대로 이미지의 명암 대비가 급격히 줄어들어 평면의 회색 이미지가 되어 버린다.
