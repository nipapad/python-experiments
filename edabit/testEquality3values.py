import test

Test.assert_equals(equal(2,3,4), 0, "All values are differents")
Test.assert_equals(equal(7,3,7), 2, "Two values are equal")
Test.assert_equals(equal(4,4,4), 3, "All 3 values are equal")
Test.assert_equals(equal(7,3,4), 0, "All values are differents")
Test.assert_equals(equal(3,3,6), 2, "Two values are equal")
Test.assert_equals(equal(1,1,1), 3, "All 3 values are equal")
Test.assert_equals(equal(1,7,6), 0, "All values are differents")
Test.assert_equals(equal(7, 7, 7), 3, "All 3 values are equal")
Test.assert_equals(equal(6, 3, 3), 2, "Two values are equal")