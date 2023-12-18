using Microsoft.SemanticKernel;
using System.ComponentModel;

namespace CoreLogic.Plugins
{
    public class EmailPlugin
    {
        [KernelFunction]
        [Description("Sends an email to a recipient")]
        public async Task SendEmailAsync(Kernel kernel, [Description("Semicolon delimitated list of email of the recipients")] string recipients, string subject, string body)
        {
            // Logic to trigger emails.
            Console.WriteLine("Email sent");
        }
    }
}
