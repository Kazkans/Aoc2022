package main

import (
	"bufio"
	"strings"
	"os"
	"strconv"
	"fmt"
)

type file struct {
	name string
	size int
	parent *file
	children []*file
}

func (f *file) calc() int {
	for _, c := range f.children {
		f.size+=c.calc()
	}
	if f.size <= 100000 && f.children != nil  {
		below100k += f.size
	}

	return f.size
}

func (f *file) search() {
	if f.size >= needed && f.size < expected{
		expected = f.size
	}

	for _, c := range f.children {
		c.search()
	}

}

var below100k int = 0
var expected int = 70000000000
var needed int = 0 

func main() {
	f, err := os.Open("data.txt")

	if err != nil {
		fmt.Println(err)
	}
	fScan := bufio.NewScanner(f)

	fScan.Split(bufio.ScanLines)

	root := file{"/",0, nil, nil}
	cur := &root

	for fScan.Scan() {
		params := strings.Split(fScan.Text(), " ")
		if params[1]=="cd" {
			switch params[2] {
			case "/":
				cur = &root
			case "..":
				cur = cur.parent
			default:
				for _, c := range cur.children {
					if c.name==params[2] {
						cur=c
						break
					}
				}
			}
		} else if params[1] != "ls" {
			if params[0] == "dir" {
				cur.children = append(cur.children, &(file{params[1],0,cur, nil}))
			} else {
				v, _ := strconv.Atoi(params[0])
				cur.children = append(cur.children, &(file{params[1],v,cur, nil}))
			}
		
		}
	}
	needed=30000000-70000000+root.calc()
	root.search()
	fmt.Printf("1: %v\n", below100k)
	fmt.Printf("2: %v\n", expected)
	f.Close()
}
