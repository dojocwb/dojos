# Fixnum, push test.

class Fixnum
 
  def to_roman
    case self
      when 0
        ""
      when 1..3
      	"I"*self
      when 4
        "IV"
      when 5..8
        "V" + (self-5).to_roman
      when 9
        "IX"
      when 10..13
        "X" + (self-10).to_roman
      when 14
        "XIV"
      when 19
        "XIX"
      when 20
        "XX"
    end
  end
end
