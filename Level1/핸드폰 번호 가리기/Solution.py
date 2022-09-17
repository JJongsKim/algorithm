def solution(phone_number):
  text = phone_number[:len(phone_number)-4]
  answer = phone_number.replace(text, "*"*len(text))

  return answer