// See https://aka.ms/new-console-template for more information
using DemoConsole.Agents;

public static class Program
{
    public static async Task Main()
    {
        await EmailAgent.ExecuteEmailAgent().ConfigureAwait(false);
    }
}