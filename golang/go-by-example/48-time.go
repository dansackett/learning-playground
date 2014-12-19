package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// We can get the current datetime
	now := time.Now()
	p(now)

	// Or we can build our own custom time
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	// We can extract any portion of the date string
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	// We can find the actual day of the week
	p(then.Weekday())

	// We can test if a date is before, after, or equal to another
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// We can final an interval between two times (difference)
	diff := now.Sub(then)
	p(diff)

	// We can see the parts of this difference
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// We can add or subtract these date values from another
	p(then.Add(diff))
	p(then.Add(-diff))
}
