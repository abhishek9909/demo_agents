using CoreLogic.Planners;
using CoreLogic.Plugins;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;

namespace DemoConsole.Agents
{
    public static class EmailAgent
    {
        public static async Task ExecuteEmailAgent()
        {
            var builder = Kernel.CreateBuilder();
            builder.Services.AddAzureOpenAIChatCompletion(endpoint: "<<end_point>>", deploymentName: "<<deployment_name>>", apiKey: "<<api_key>>");
            builder.Plugins.AddFromType<EmailPlanner>();
            builder.Plugins.AddFromType<EmailPlugin>();
            Kernel kernel = builder.Build();

            // Retrieve the chat completion service.
            var chatCompletionService = kernel.GetRequiredService<IChatCompletionService>();

            // Create tha chat history.
            ChatHistory chatMessages = new ChatHistory("You are a friendly assistant who likes to follow the rules. You will complete required steps\r and request approval before taking any consequential actions. If the user doesn't provide\r enough information for you to complete a task, you will keep asking questions until you have\r enough information to complete the task.");
            
            while(true)
            {
                // Get user input
                Console.Write("User > ");
                chatMessages.AddUserMessage(Console.ReadLine()!);

                var result = chatCompletionService.GetStreamingChatMessageContentsAsync(
                    chatMessages,
                    kernel: kernel);

                // Stream the results
                string fullMessage = "";
                await foreach (var content in result)
                {
                    if (content.Role.HasValue)
                    {
                        Console.Write("Assistant > ");
                    }
                    Console.Write(content.Content);
                    fullMessage += content.Content;
                }
                Console.WriteLine();

                // Add the message from the agent to the chat history
                chatMessages.AddAssistantMessage(fullMessage);
            }
        }
    }
}
