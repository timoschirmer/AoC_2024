package main

import (
	"bufio"
	"fmt"
	"os"
)

type Position struct {
	row int
	col int
	dir direction
}

type direction int

const (
	up direction = iota
	right
	down
	left
)

func turn(pos Position) Position {
	newDirection := (pos.dir + 1) % 4
	return Position{row: pos.row, col: pos.col, dir: newDirection}
}

func move(pos Position) Position {
	switch pos.dir {
	case up:
		pos.row--
	case right:
		pos.col++
	case down:
		pos.row++
	case left:
		pos.col--
	}
	return pos
}

func isInBounds(pos Position, grid [][]rune) bool {
	return pos.row >= 0 && pos.row < len(grid) && pos.col >= 0 && pos.col < len(grid[0])
}

func removeDuplicates(positions []Position) []Position {
	seen := make(map[string]bool)
	uniquePositions := []Position{}

	for _, pos := range positions {
		key := fmt.Sprintf("%d,%d", pos.row, pos.col)
		if !seen[key] {
			seen[key] = true
			uniquePositions = append(uniquePositions, pos)
		}
	}

	return uniquePositions
}

func findStartPosition(grid [][]rune) Position {
	for row := 0; row < len(grid); row++ {
		for col := 0; col < len(grid[row]); col++ {
			if grid[row][col] == '^' {
				return Position{row: row, col: col}
			}
		}
	}
	return Position{row: -1, col: -1}
}

func removeStartPosition(grid [][]rune, positions []Position) []Position {
	filtered := []Position{}
	target := findStartPosition(grid)
	for _, pos := range positions {
		if pos.row == target.row && pos.col == target.col {
			continue
		}
		filtered = append(filtered, pos)
	}
	return filtered
}

func traverse(grid [][]rune, start Position) ([]Position, bool) {
	current := start
	visited := []Position{}

	for {
		visited = append(visited, current)

		grid[current.row][current.col] = 'X'

		next := move(current)

		if !isInBounds(next, grid) {
			// fmt.Println("Ende erreicht: außerhalb der Grenzen")
			break
		}

		if checkForLoop(visited, next) {
			return removeDuplicates(visited), true
		}

		if grid[next.row][next.col] == '#' {
			// fmt.Printf("Hindernis bei Position (%d, %d) gefunden\n", next.row, next.col)
			next = turn(current)
		}

		current = next
		// fmt.Printf("Bewegt zu Position (%d, %d)\n", current.row, current.col)
	}
	return removeDuplicates(visited), false
}

func createsLoop(grid [][]rune, path []Position, start Position) []bool {
	c := make(chan bool)

	for idx, pos := range path {
		if idx != 0 {
			start = path[idx-1]
		}
		go simulateMovementWithObstacle(grid, pos, start, c)
	}

	isLoop := make([]bool, len(path))
	for i := range isLoop {
		isLoop[i] = <-c
	}

	return isLoop
}

func simulateMovementWithObstacle(grid [][]rune, obstaclePos Position, start Position, c chan bool) {
	tempGrid := copySlice(grid)
	tempGrid[obstaclePos.row][obstaclePos.col] = '#'

	_, loopDetected := traverse(tempGrid, start)

	c <- loopDetected
}

func checkForLoop(path []Position, currentPosition Position) bool {
	for _, pos := range path {
		if pos == currentPosition {
			return true
		}
	}
	return false
}

func copySlice(src [][]rune) [][]rune {
	dest := make([][]rune, len(src))
	for i := range src {
		dest[i] = make([]rune, len(src[i]))
		copy(dest[i], src[i])
	}
	return dest
}

func countTrueIndices(bools []bool) int {
	var indices int
	for _, b := range bools {
		if b {
			indices++
		}
	}
	return indices
}

func printGrid(grid [][]rune) {
	for _, line := range grid {
		for _, char := range line {
			fmt.Printf(" %c", char)
		}
		fmt.Println()
	}
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		fmt.Println("Fehler beim Öffnen der Datei:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var array [][]rune

	for scanner.Scan() {
		line := scanner.Text()
		characters := []rune(line)
		array = append(array, characters)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Fehler beim Lesen der Datei:", err)
		return
	}

	startPosition := findStartPosition(array)

	visitedPositions, _ := traverse(array, startPosition)
	// printGrid(array)
	fmt.Printf("Anzahl der besuchten Positionen: %d\n", len(visitedPositions))

	path := removeStartPosition(array, visitedPositions)
	loops := countTrueIndices(createsLoop(array, path, startPosition))
	fmt.Printf("Anzahl der gefundenen Loops: %d\n", loops)
}
