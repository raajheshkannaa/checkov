resource "aws_cognito_user_pool" "pass" {
  name = "pass"

  user_pool_add_ons {
    advanced_security_mode = "ENFORCED"
  }
}

resource "aws_cognito_user_pool" "audit" {
  name = "audit"

  user_pool_add_ons {
    advanced_security_mode = "AUDIT"
  }
}

resource "aws_cognito_user_pool" "off" {
  name = "off"

  user_pool_add_ons {
    advanced_security_mode = "OFF"
  }
}

resource "aws_cognito_user_pool" "missing" {
  name = "missing"
}
