package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

type res struct {
	index  int
	result int
}

func prepareInput(file string) ([]int, [][]int) {
	rows := strings.Split(file, "\n")

	var results []int
	var numbers [][]int

	for _, row := range rows {
		split := strings.Split(row, ": ")
		result, err := strconv.Atoi(split[0])
		if err != nil {
			fmt.Println(err)
		}
		results = append(results, result)
		split = strings.Split(split[1], " ")
		var number []int
		for _, i := range split {
			x, err := strconv.Atoi(i)
			if err != nil {
				fmt.Println(err)
			}
			number = append(number, x)
		}
		numbers = append(numbers, number)
	}
	return results, numbers
}

func task1(results []int, numbers [][]int) (int, map[int]bool) {
	var wg sync.WaitGroup
	c1 := make(chan res, len(results))

	for idx, result := range results {
		wg.Add(1)
		go func(idx int, result int, numbers []int) {
			defer wg.Done()
			checkCombinationsX(result, numbers, idx, c1, 2)
		}(idx, result, numbers[idx])
	}

	wg.Wait()
	close(c1)

	sum := 0
	resultMap := make(map[int]bool)
	for element := range c1 {
		sum += element.result
		if element.result == 0 {
			resultMap[element.index] = false
		} else {
			resultMap[element.index] = true
		}
	}

	return sum, resultMap
}

func concatenate(a, b int) int {
	concat, err := strconv.Atoi(fmt.Sprintf("%d%d", a, b))
	if err != nil {
		fmt.Println(err)
	}
	return concat
}

func task2(results []int, numbers [][]int, resultMap map[int]bool) int {

	results, numbers = filterList(results, numbers, resultMap)

	var wg2 sync.WaitGroup
	c2 := make(chan res, len(results))

	for idx, result := range results {
		wg2.Add(1)
		go func(idx int, result int, numbers []int) {
			defer wg2.Done()
			checkCombinationsX(result, numbers, idx, c2, 3)
		}(idx, result, numbers[idx])
	}

	wg2.Wait()
	close(c2)

	sum := 0
	for num := range c2 {
		sum += num.result
	}

	return sum
}

func filterList(results []int, numbers [][]int, resultMap map[int]bool) ([]int, [][]int) {
	removed := 0
	for idx := range results {
		if resultMap[idx] {
			results = remove(results, (idx - removed))
			numbers = remove(numbers, (idx - removed))
			removed += 1
		}
	}
	return results, numbers
}

func remove[T any](slice []T, index int) []T {
	return append(slice[:index], slice[index+1:]...)
}

func checkCombinationsX(solution int, numbers []int, idx int, channel chan res, options int) {
	n := len(numbers)

	maxMask := 1
	for i := 0; i < n-1; i++ {
		maxMask *= options
	}

	for mask := 0; mask < maxMask; mask++ {
		result := numbers[0]
		currentMask := mask

		for i := 0; i < n-1; i++ {
			operation := currentMask % options
			currentMask /= options

			switch operation {
			case 0: // Addieren
				result += numbers[i+1]
			case 1: // Multiplizieren
				result *= numbers[i+1]
			case 2: // Verketten
				result = concatenate(result, numbers[i+1])
			}
		}

		if result == solution {
			channel <- res{index: idx, result: result}
			return
		}
	}

	channel <- res{index: idx, result: 0}
	return
}

func main() {
	file, err := os.ReadFile("input")
	if err != nil {
		fmt.Println(err)
	}
	results, numbers := prepareInput(string(file))

	task1Result, resultMap := task1(results, numbers)
	fmt.Printf("Das Ergebnis für Task 1 lautet: %d\n", task1Result)

	task2Result := task2(results, numbers, resultMap)
	task2Result += task1Result
	fmt.Printf("Das Ergebnis für Task 2 lautet: %d\n", task2Result)
}
