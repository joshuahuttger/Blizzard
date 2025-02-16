package com.huttger.joshua.snowman.signup;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CreateUserController {
	private final AtomicLong counter = new AtomicLong();

	@GetMapping("/createUser")
	public User createUser(@RequestParam(value = "first_name") String firstName,
			@RequestParam(value = "last_name") String lastName) {
		return new User(counter.incrementAndGet(), firstName, lastName);
	}
}
