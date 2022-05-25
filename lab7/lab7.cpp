// Dijkstra's shortest path algorithm using priority queue
// Author: Shagufta Anjum
// 19XJ1A0568

#include<bits/stdc++.h>
using namespace std;
# define INF 0x3f3f3f3f
  
// Integer Pair
typedef pair<int, int> iPair;
  
// Function to add an edge of weight wt between given nodes u and v
void addEdge(vector <pair<int, int> > adj[], int u,
                                     int v, int wt)
{
    adj[u].push_back(make_pair(v, wt));
    adj[v].push_back(make_pair(u, wt));
}
   
  
// Function to print the shortest paths from src node to all other nodes
void shortestPath(vector<pair<int,int> > adj[], int V, int src)
{
    // Create a priority queue to store vertices that are being preprocessed
    priority_queue< iPair, vector <iPair> , greater<iPair> > pq;
  
    // Create a vector for distances and initialize all distances as infinite (INF)
    vector<int> dist(V, INF);
  
    // Insert source itself in priority queue and initialize its distance as 0.
    pq.push(make_pair(0, src));
    dist[src] = 0;
  
    //Looping till priority queue becomes empty (or all distances are not finalized)
    while (!pq.empty())
    {
        // The first vertex in pair is the minimum distance
        // vertex, extract it from priority queue.
        // vertex label is stored in second of pair (it
        // has to be done this way to keep the vertices
        // sorted distance (distance must be first item
        // in pair)
        int u = pq.top().second;
        pq.pop();
  
        // Get all adjacent of u. 
        for (auto x : adj[u])
        {
            // Get vertex label and weight of current adjacent
            // of u.
            int v = x.first;
            int weight = x.second;
  
            // If there is shorted path to v through u.
            if (dist[v] > dist[u] + weight)
            {
                // Updating distance of v
                dist[v] = dist[u] + weight;
                pq.push(make_pair(dist[v], v));
            }
        }
    }
  
    // Print shortest distances stored in dist[]
    printf("Source is vertex 0\n");
    printf("Vertex \t\t Distance\n");
    for (int i = 0; i < V; ++i)
        printf("%d \t\t %d\n", i, dist[i]);
}
  
// Driver program
int main()
{
    int V = 7;
    vector<iPair > adj[V];
  
    // making the graph
    addEdge(adj, 0, 1, 2);
    addEdge(adj, 0, 2, 6);
    addEdge(adj, 1, 3, 5);
    addEdge(adj, 2, 3, 8);
    addEdge(adj, 3, 5, 15);
    addEdge(adj, 3, 4, 10);
    addEdge(adj, 4, 5, 6);
    addEdge(adj, 5, 6, 6);
    addEdge(adj, 4, 6, 2);
  
    shortestPath(adj, V, 0);
  
    return 0;
}