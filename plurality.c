/*
** Plurality voting is an electoral system in which each voter
** is allowed to vote for only one candidate,
** and the candidate who polls the most among
** their counterparts (a plurality) is elected
*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    int counter = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
        }

        else
        {
            counter++;
        }

    }

    if (counter <  candidate_count)
    {
        return true;
    }

    else
    {
        return false;
    }

}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int winners[candidate_count];
    int n = 0;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes >= n)
        {
            winners[i] = 1;
            n = candidates[i].votes;
        }

        else
        {
            winners[i] = 0;
            n = candidates[i].votes;
        }
    }

    for (int j = 0; j < candidate_count; j++)
    {
        if (winners[j] == 1)
        {
            printf("%s\n", candidates[j].name);
        }
    }
    return;
}
