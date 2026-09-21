package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func main(){
	reader :=  bufio.NewReader(os.Stdin)

	words, _ := reader.ReadString('\n')
	words = strings.TrimSpace(words)

	start := 0

	for i, c := range words{
		if c == ' ' {
			fmt.Println(words[start:i+1])
			start = i + 1
		}
	}
	fmt.Println(words[start:])
}
