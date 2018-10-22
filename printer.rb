# def printer
#     puts "Hello"
# end

# def menseki_calculater(radius)
#     menseki = radius ** 2 * 3.14
#     puts "半径#{radius}cmの円の面積は#{menseki}㎠です"
# end


# menseki_calculater(20)

# number = 20
# if number > 30 then
#     puts "大吉"
# elsif 30 >= number > 20 then
#      puts "中吉"
# elsif 20 >= number > 10 then
#      puts "末吉"
#  else
#      puts "凶"
#  end

# for num in 1..10
#     puts num
# end

# number = 1
# while number % 10 != 0
#     puts number
#     number += 1
# end


class People
	def set_profile
      puts "名前を入力してください"
      @name = gets.chomp
      puts "性別を入力してください"
      @sex = gets.chomp
      puts "年齢を入力してください"
      @age = gets.chomp
   end
   
   def show_profile
   		line = "---------------------------"
    	puts "名前 : #{@name}\n#{line}\n"
    	puts "性別 : #{@sex}\n#{line}\n"
    	puts "年齢 :\n#{@age}\n#{line}\n"
   end
end

# インスタンスの生成
person = People.new
person.set_profile
person.show_profile/