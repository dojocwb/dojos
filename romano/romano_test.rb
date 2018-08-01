require "test/unit"
require "romano"

class RomanoTest < Test::Unit::TestCase
  NUMEROS = {0 => "",
             1 => "I",
             3 => "III",
             5 => "V",
             6 => "VI",
             10 => "X"}  

  def test_numero
    NUMEROS.each{|k,v|assert_equal(k.to_roman, v)}
  end
  
  def test_numero_0
    assert_equal(0.to_roman, "")
  end
  
  def test_numero_1
    assert_equal(1.to_roman, "I")
  end

  def test_numero_2
    assert_equal(2.to_roman, "II")
  end

  def test_numero_3
    assert_equal(3.to_roman, "III")
  end

  def test_numero_4
    assert_equal(4.to_roman, "IV")
  end

  def test_numero_5
    assert_equal(5.to_roman, "V")
  end

  def test_numero_6
    assert_equal(6.to_roman, "VI")
  end

  def test_numero_7
    assert_equal(7.to_roman, "VII")
  end

  def test_numero_8
    assert_equal(8.to_roman, "VIII")
  end

  def test_numero_9
    assert_equal(9.to_roman, "IX")
  end

  def test_numero_10
    assert_equal(10.to_roman, "X")
  end

  def test_numero_11
    assert_equal(11.to_roman, "XI")
  end

  def test_numero_13
    assert_equal(13.to_roman, "XIII")
  end

  def test_numero_14
    assert_equal(14.to_roman, "XIV")
  end

  def test_numero_19
    assert_equal(19.to_roman, "XIX")
  end
  
  def test_numero_20
    assert_equal(20.to_roman, "XX")
  end


end
