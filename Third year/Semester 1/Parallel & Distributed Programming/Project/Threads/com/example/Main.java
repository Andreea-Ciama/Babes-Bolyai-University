package com.example;

import com.example.Colors;
import com.example.Graph;
import com.example.GraphColoring;

public class Main {
    public static void main(String[] args) {

        int threadsNumber = 10;

        // Example 1
        Graph graph1 = new Graph(4);
        graph1.addEdge(0, 1);
        graph1.addEdge(1, 2);
        graph1.addEdge(0, 3);

        Colors colors1 = new Colors(2);
        colors1.addColor(0, "pink");
        colors1.addColor(1, "black");

        try {
            long startTime = System.nanoTime();
            //GraphColoring.getColoredGraph(threadsNumber, graph1, colors1);
            System.out.println("Example 1 - Original Graph:");
            System.out.println(graph1);
            System.out.println("Colored Graph:");
            System.out.println(GraphColoring.getColoredGraph(threadsNumber, graph1, colors1));  // Use the toString method of the Colors class

            long endTime = System.nanoTime();
            System.out.println("Execution time: " + (endTime - startTime) / 1000000 + " ms");
        } catch (Exception e) {
            System.out.println(e);
        }

        // Example 2
        Graph graph2 = new Graph(5);
        graph2.addEdge(0, 1);
        graph2.addEdge(1, 2);
        graph2.addEdge(2, 3);
        graph2.addEdge(3, 4);
        graph2.addEdge(4, 0);
        graph2.addEdge(2, 0);
        graph2.addEdge(0, 4);
        graph2.addEdge(4, 3);
        graph2.addEdge(3, 1);

        Colors colors2 = new Colors(3);
        colors2.addColor(0, "red");
        colors2.addColor(1, "green");
        colors2.addColor(2, "blue");

        try {
            long startTime = System.nanoTime();
            //GraphColoring.getColoredGraph(threadsNumber, graph2, colors2);
            System.out.println("Example 2 - Original Graph:");
            System.out.println(graph2);
            System.out.println("Colored Graph:");
            System.out.println(GraphColoring.getColoredGraph(threadsNumber, graph2, colors2));

            long endTime = System.nanoTime();
            System.out.println("Execution time: " + (endTime - startTime) / 1000000 + " ms");
        } catch (Exception e) {
            System.out.println(e);
        }

        // Example 3
        Graph graph3 = Graph.generateRandomConnectedGraph(10);
        Colors colors3 = new Colors(5);
        colors3.addColor(0, "red");
        colors3.addColor(1, "green");
        colors3.addColor(2, "blue");
        colors3.addColor(3, "yellow");
        colors3.addColor(4, "pink");

        try {
            long startTime = System.nanoTime();
            //GraphColoring.getColoredGraph(threadsNumber, graph3, colors3);
            System.out.println("Example 3 - Original Graph:");
            System.out.println(graph3);
            System.out.println("Colored Graph:");
            System.out.println(GraphColoring.getColoredGraph(threadsNumber, graph3, colors3));

            long endTime = System.nanoTime();
            System.out.println("Execution time: " + (endTime - startTime) / 1000000 + " ms");
        } catch (Exception exception) {
            exception.printStackTrace();
        }
        // Example 4
        Graph graph4 = Graph.generateRandomConnectedGraph(100);
        Colors colors4 = new Colors(20);
        colors4.addColor(0, "red");
        colors4.addColor(1, "green");
        colors4.addColor(2, "blue");
        colors4.addColor(3, "yellow");
        colors4.addColor(4, "pink");
        colors4.addColor(5, "pin");
        colors4.addColor(6, "pik");
        colors4.addColor(7, "abc");
        colors4.addColor(8, "cdf");
        colors4.addColor(9, "nk");
        colors4.addColor(10, "rd");
        colors4.addColor(11, "gren");
        colors4.addColor(12, "bue");
        colors4.addColor(13, "yelow");
        colors4.addColor(14, "pk");
        colors4.addColor(15, "pn");
        colors4.addColor(16, "pi");
        colors4.addColor(17, "ab");
        colors4.addColor(18, "cf");
        colors4.addColor(19, "cff");


        try {
            long startTime = System.nanoTime();
            //GraphColoring.getColoredGraph(threadsNumber, graph3, colors3);
            System.out.println("Example 4 - Original Graph:");
            System.out.println(graph4);
            System.out.println("Colored Graph:");
            System.out.println(GraphColoring.getColoredGraph(threadsNumber, graph4, colors4));

            long endTime = System.nanoTime();
            System.out.println("Execution time: " + (endTime - startTime) / 1000000 + " ms");
        } catch (Exception exception) {
            exception.printStackTrace();
        }


    }
}
