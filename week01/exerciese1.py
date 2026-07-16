name = input("Enter your name: ")
m_time = int(input("Minutes studied today: "))
h_time = float(m_time) / 60
focus = int(input("How focused were you on a scale of 1-10? "))
effort = m_time * focus
print("Hello " + name + ", you studied for " + str(m_time) + " minutes today, which is " + str(h_time) + " hours. Your focus level was " + str(focus) + ", resulting in an effort score of " + str(effort) + ".")

